from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import PlantForm
from .models import Plant


@login_required
def plant_list(request):
    plants = Plant.objects.filter(owner=request.user).order_by('name')
    return render(request, 'plant_agent/list.html', {'plants': plants})


@login_required
def plant_create(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.owner = request.user
            plant.save()
            messages.success(request, 'Plant added successfully.')
            return redirect('plant_agent:list')
    else:
        form = PlantForm()
    return render(request, 'plant_agent/create.html', {'form': form})


@login_required
def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk, owner=request.user)
    return render(request, 'plant_agent/detail.html', {'plant': plant})
