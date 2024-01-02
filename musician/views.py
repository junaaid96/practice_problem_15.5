from django.shortcuts import render, redirect
from .models import Musician
from . import forms

# Create your views here.


def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    else:
        musician_form = forms.MusicianForm()
    return render(request, 'add_musician.html', {'musician_form': musician_form})


def edit_musician(request, id):
    musician = Musician.objects.get(pk=id)
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    else:
        musician_form = forms.MusicianForm(instance=musician)
    return render(request, 'add_musician.html', {'musician_form': musician_form})


def delete_musician(request, id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')
