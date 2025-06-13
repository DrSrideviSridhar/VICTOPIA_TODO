from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
#from .gemini_service import GeminiService

# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    

class TaskCreate(CreateView):
    model = Task
    template_name = 'todo/task_form.html'
    fields = ['title']
    success_url = reverse_lazy('task_list')

class TaskUpdate(UpdateView):
    model = Task
    template_name = 'todo/task_form.html'
    fields = ['title', 'completed']
    success_url = reverse_lazy('task_list')


class TaskDelete(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
