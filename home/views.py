from django.shortcuts import render
from home.models import Club
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        name=request.POST.get('club-name')
        head=request.POST.get('head-name')
        description=request.POST.get('club-desc')
        upcoming_events=request.POST.get('events')
        members=request.POST.get('members')
        projects=request.POST.get('projects')
        club = Club(name=name, head=head, description=description, upcoming_events=upcoming_events, members=members, projects=projects)
        club.save()
        messages.success(request, 'Your club has been registered successfully.')

    return render(request, 'index.html')
