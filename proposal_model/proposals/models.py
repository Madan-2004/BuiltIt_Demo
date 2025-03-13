from django.db import models
from django.contrib.auth.models import User

class Proposal(models.Model):
    club_head = models.ForeignKey(User, on_delete=models.CASCADE)  # Who uploaded
    pdf = models.FileField(upload_to='proposals/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)  # Status

    def __str__(self):
        return f"Proposal by {self.club_head.username} - {'Viewed' if self.is_viewed else 'Unviewed'}"
