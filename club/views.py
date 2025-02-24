from django.shortcuts import render,get_object_or_404, redirect
from .models import Member, Club

def add_member(request):
    from .member_forms import MemberForm  # Moved import inside function

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display_members')
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})

def remove_member(request):
    from .member_forms import MemberDeleteForm  # Import inside function

    if request.method == 'POST':
        form = MemberDeleteForm(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data['roll_no']  # Use roll_no instead of member_id
            try:
                member = Member.objects.get(roll_no=roll_no)  # Search by roll_no
                member.delete()
                return redirect('display_members')  # Redirect after successful deletion
            except Member.DoesNotExist:
                form.add_error('roll_no', 'Member not found')  # Show error if roll_no is invalid
    else:
        form = MemberDeleteForm()
    
    return render(request, 'remove_member.html', {'form': form})


def display_members(request):
    members = Member.objects.all()
    return render(request, 'display_members.html', {'members': members})

def edit_member(request, member_id):
    from .member_forms import MemberForm
    member = get_object_or_404(Member, id=member_id)

    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('display_members')  # Redirect to members list after update
    else:
        form = MemberForm(instance=member)

    return render(request, 'edit_member.html', {'form': form, 'member': member})
