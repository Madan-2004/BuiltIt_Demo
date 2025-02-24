from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'roll_no', 'email','branch', 'designation', 'club', 'profile_picture']

class MemberDeleteForm(forms.Form):
    roll_no = forms.IntegerField()
