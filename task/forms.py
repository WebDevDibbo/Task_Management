from django import forms 
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'task_assign_date' : forms.TextInput(attrs={'placeholder':'Please select the date this format year-month-date'}),
            'taskTitle' : forms.TextInput(attrs={'placeholder':'Please enter the name of the task'}),
            'taskDescription' : forms.Textarea(attrs={'placeholder':'Please enter the description of your task'}),
        }