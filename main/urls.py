from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo_list, name='home'),
        path('delete/<int:pk>/', views.DeleteTodo.as_view(), name='delete')
]
