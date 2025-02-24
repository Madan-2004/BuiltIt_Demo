from django.contrib import admin
from django.urls import path
from club import views


urlpatterns = [
    path('add/', views.add_member, name='add_member'),
    path('remove/', views.remove_member, name='remove_member'),
    path('members/', views.display_members, name='display_members'),
    path('edit/<int:member_id>/', views.edit_member, name='edit_member'),
]

