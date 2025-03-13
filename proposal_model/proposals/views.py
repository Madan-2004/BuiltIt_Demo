from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Proposal
from .forms import ProposalForm

# Club Head uploads proposal
@login_required
def upload_proposal(request):
    if request.method == "POST":
        form = ProposalForm(request.POST, request.FILES)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.club_head = request.user
            proposal.save()
            return redirect('admin_dashboard')  # Redirects to admin after upload

    else:
        form = ProposalForm()
    return render(request, 'proposals/upload.html', {'form': form})

# Admin views proposals
@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('upload_proposal')  # Redirects to admin after upload


    unviewed_proposals = Proposal.objects.filter(is_viewed=False)
    viewed_proposals = Proposal.objects.filter(is_viewed=True)
    
    return render(request, 'proposals/admin_dashboard.html', {
        'unviewed_proposals': unviewed_proposals,
        'viewed_proposals': viewed_proposals
    })

# Mark proposal as viewed
@login_required
def mark_as_viewed(request, proposal_id):
    if request.user.is_superuser:
        proposal = Proposal.objects.get(id=proposal_id)
        proposal.is_viewed = True
        proposal.save()
    return redirect('admin_dashboard')
