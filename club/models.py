# models.py

from django.db import models
from home.models import Club  # Import the Club model from the other app
from django.core.exceptions import ValidationError

def validate_image_file(value):
    if not value.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.webp')):
        raise ValidationError('Only image files (PNG, JPG, JPEG, GIF, BMP, SVG, WEBP) are allowed.')


class Member(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=100, default="Unknown")
    designation = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='members_home')
    profile_picture = models.FileField(upload_to='member_images/', blank=True, null=True,validators=[validate_image_file])

    def __str__(self):
     return self.name  

