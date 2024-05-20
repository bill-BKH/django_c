from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def todo(request):
    data = Todo.objects.all().order_by('priority')
    return render(request,'todo/todo.html',{'todos':data})