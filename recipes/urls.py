from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('new/', views.new_recipe, name='new_recipe'),
    path('recipes/<int:recipe_id>/edit/',
         views.recipe_edit, name='recipe_edit'),
    path('recipes/<int:recipe_id>/edit/delete/',
         views.recipe_delete, name='recipe_delete'),

    path('follow/', views.follow_index, name='follow_index'),
    path('recipes/<int:recipe_id>/', views.recipe_view, name='recipe'),
    path('favourites/', views.favourites, name='favourites'),
    path('shoping_list/', views.shoping_list, name='shoping_list'),
    path('shoping_list/print/', views.print_shoping_list,
         name='print_shoping_list'),
    path('del/purchases/<int:recipe_id>/',
         views.del_purchase, name='del_purchase'),

    # JS
    path('purchases/', views.Purchases.as_view(), name='add_purchase'),
    path('purchases/<int:recipe_id>/',
         views.Purchases.as_view(), name='delete_purchase'),
    path('favorites/', views.Favorites.as_view(), name='add_favorites'),
    path('favorites/<int:recipe_id>/',
         views.Favorites.as_view(), name='delete_favorites'),
    path('subscriptions/', views.Subscribe.as_view(), name='subscribe'),
    path('subscriptions/<int:author_of_recipe>/',
         views.Subscribe.as_view(), name='unsubscribe'),
    path('ingredients/', views.Ingredients.as_view(), name='ingredients'),

    path('<str:username>/', views.profile,
         name='profile'),

]
