from django.shortcuts import render, redirect
from . import forms
from task.models import Task
# Create your views here.
def addTask(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
        
    else:
        task_form = forms.TaskForm()
    return render(request,'task.html',{'form':task_form})

def showTask(request):
    data = Task.objects.all()
    return render(request,'show_task.html',{'data':data})


def editTask(request,id):
    task = Task.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST,instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    return render(request,'task.html',{'form':task_form})

def deleteTask(request,id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_task')