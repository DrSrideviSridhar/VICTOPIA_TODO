from django.urls import path
from .views import TaskCreate, TaskList, TaskUpdate, TaskDelete     
urlpatterns = [
    # Define your URL patterns here
    # Example: path('', views.index, name='index'),
    # path('tasks/', views.task_list, name='task_list'),
    # path('tasks/<int:id>/', views.task_detail, name='task_detail'),

    path('',TaskList.as_view(), name='task_list'),
    path('add/', TaskCreate.as_view(), name='task_create'),
    path('<int:pk>/edit/', TaskUpdate.as_view(), name='task_edit'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task_delete')
]

