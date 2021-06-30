from . import views
from django.urls import path


app_name = 'superheroesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.display_data, name='display_data'),
    path('new/', views.create_new_superhero, name='create_new_superhero'),
    path('edit/<int:superhero_id>/', views.superhero_edit, name='superhero_edit'),
    path('update/<int:superhero_id>/', views.update_superhero, name='update_superhero'),
    path('delete/<int:superhero_id>/', views.delete_superhero, name='delete_superhero')
]