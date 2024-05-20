from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def todo(request):
    data = Todo.objects.all().order_by('priority')
    return render(request,'todo/todo.html',{'todos':data})


# TODO: show single taks update view with dynamic link
def add_todo(request):
    if request.method == 'POST':
        x = request.POST.get('priority')
        y = request.POST.get('todo_text')
        new_todo = Todo(text=y,priority=int(x))
        new_todo.save()
        return redirect(reverse('todo:todo'))
    return render(request,'todo/add.html')


def delete_todo(request,todo_id):
    Todo.objects.filter(id=todo_id).delete()
    return redirect(reverse('todo:todo'))

def edit_todo(request,todo_id):
    if request.method == 'POST':
        x = request.POST.get('priority')
        y = request.POST.get('todo_text')
        edit_todo = Todo.objects.get(id=todo_id)
        edit_todo.text = y
        edit_todo.priority = int(x)     
        edit_todo.save()
        return redirect(reverse('todo:todo'))

    todo = Todo.objects.get(id=todo_id)
    return render(request,'todo/edit.html',{'todo':todo})
    