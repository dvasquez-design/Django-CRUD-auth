from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('', views.tareas, name='tareas'),
    path('create/', views.create_tarea, name='create_tarea'),
    path('completed/', views.tareas_completed, name='tareas_completed'),
    path('<int:tarea_id>/', views.tarea_detail, name='tarea_detail'),
    path('<int:tarea_id>/complete/', views.complete_tarea, name='complete_tarea'),
    path('<int:tarea_id>/delete/', views.delete_tarea, name='delete_tarea'),
    
]