from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('add_task', views.add, name='addTask'),
    path('remove_task/<int:id>', views.remove, name='removeTask'),
    path('compl_task/<int:id>', views.complete, name='removeTask'),
    path('edit_task/<int:Tid>', views.editTask, name='editask'),
]