from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Tarea
from .forms import TareaForm

# Create your views here.

@login_required
def tareas(request):
    tareas = Tarea.objects.filter(user=request.user, date_completed__isnull=True).order_by('-created')
    return render(request, 'tareas/tareas.html', {'tareas': tareas})

def create_tarea(request):
    if request.method == 'POST':
        try:
            form = TareaForm(request.POST)
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.user = request.user
                tarea.save()
                return redirect('tareas')
        except ValueError:
            pass
    else:
        form = TareaForm()
    return render(request, 'tareas/create_tarea.html', {'form': form})

def tarea_detail(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    
    if request.method == 'POST':
        try:
            form = TareaForm(request.POST, instance=tarea)
            if form.is_valid():
                form.save()
                return redirect('tareas')
        except ValueError:
            pass
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'tareas/tarea_detail.html', {'tarea': tarea, 'form': form})

def complete_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    if request.method == 'POST':
        tarea.date_completed = timezone.now()
        tarea.save()
        return redirect('tareas')
    
def delete_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id, user=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')
    
def sign_up(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user) 
            return redirect('tareas') 
    else: 
        form = UserCreationForm() 
    return render(request, 'tareas/sign_up.html', {'form': form})

@login_required
def tareas_completed(request):
    tareas = Tarea.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'tareas/tareas_completed.html', {'tareas': tareas})
