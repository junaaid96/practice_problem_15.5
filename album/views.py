from django.shortcuts import render, redirect
from .models import Album
from . import forms

# Create your views here.


def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'album_form': album_form})


def edit_album(request, id):
    album = Album.objects.get(pk=id)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    else:
        album_form = forms.AlbumForm(instance=album)
    return render(request, 'add_album.html', {'album_form': album_form})


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home')
