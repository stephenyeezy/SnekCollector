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
]

