from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('snakes/', views.snakes_index, name='index'),
    path('snakes/<int:snake_id>', views.snakes_detail, name='detail'),
    path('snakes/create/', views.SnakeCreate.as_view(), name='snakes_create'),
    path('snakes/<int:pk>/update/', views.SnakeUpdate.as_view(), name='snakes_update'),
    path('snakes/<int:pk>/delete/', views.SnakeDelete.as_view(), name='snakes_delete'),
    path('snakes/<int:snake_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('snakes/<int:snake_id>/add_photo/', views.add_photo, name='add_photo'),
    path('snakes/<int:snake_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),    
]

