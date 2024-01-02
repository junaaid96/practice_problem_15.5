from django.urls import path
from .views import add_musician, edit_musician, delete_musician

urlpatterns = [
    path('add_musician/', add_musician, name='add_musician'),
    path('edit_musician/<int:id>/', edit_musician, name='edit_musician'),
    path('delete_musician/<int:id>/', delete_musician, name='delete_musician'),
]
