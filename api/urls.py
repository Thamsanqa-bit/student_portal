from django.urls import path
from . import views

urlpatterns = [
    path('notes_list/', views.notes_list, name='notes-list'),
    path('notes_create/', views.notesCreate, name='notes-create'),
    path('notes_update/<str:pk>/', views.notesUpdate, name='notes-update'),
    path('notes_delete/<str:pk>/', views.notesDelete, name='notes-delete'),
]
