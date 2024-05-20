from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('',views.todo,name='todo'),
    path('add/',views.add_todo, name='add_todo'),
    path('delete/<int:todo_id>',views.delete_todo,name='delete_todo'),
    path('edit_todo/<int:todo_id>',views.edit_todo, name='edit_todo')
]
