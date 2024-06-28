from django.urls import path
from . import views

urlpatterns = [
    path('add_task/',views.addTask, name='add_task'),
    path('show_task/',views.showTask, name='show_task'),
    path('edit_task/<int:id>',views.editTask, name='edit_task'),
    path('delete_task/<int:id>',views.deleteTask, name='delete_task'),
]
