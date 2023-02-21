from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

@csrf_exempt
def create_task(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'
    form = TaskForm()
    context = {'form': form,
               'error': error}
    return render(request, 'main/create_task.html', context)