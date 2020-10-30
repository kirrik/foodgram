from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    measurement_unit = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    style = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class TagedManager(models.Manager):
    def filter_for_tags(self, tags=None):
        if not tags:
            return self
        return self.filter(tag__slug__in=tags)


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор')
    name = models.CharField(
        max_length=200,
        verbose_name='Название рецепта')
    image = models.ImageField(
        upload_to='recipes/images/',
        verbose_name='Выбрать файл')
    text = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient,
        through='Amount',
        through_fields=('recipe', 'ingredient'),
        verbose_name='Ингредиенты')
    tag = models.ManyToManyField(
        Tag,
        related_name='recipes')
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления')
    slug = models.SlugField(blank=True, null=True, unique=True)
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True)

    objects = models.Manager()
    taged = TagedManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']


class Amount(models.Model):
    units = models.IntegerField(default=1)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='amounts')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following')

    def __str__(self):
        return f'({self.user} подписался на {self.author})'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorited_user')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorited_recipe')

    def __str__(self):
        return f'({self.user} добавил в избранное {self.recipe})'


class ToShop(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shoper')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_to_shop')

    def __str__(self):
        return f'({self.user} добавил в список покупок {self.recipe})'
