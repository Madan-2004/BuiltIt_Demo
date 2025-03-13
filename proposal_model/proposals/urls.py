from django.urls import path
from django.contrib import admin
from .views import upload_proposal, admin_dashboard, mark_as_viewed

urlpatterns = [
    path('upload/', upload_proposal, name='upload_proposal'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('mark-viewed/<int:proposal_id>/', mark_as_viewed, name='mark_as_viewed'),
]
