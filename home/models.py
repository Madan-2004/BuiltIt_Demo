from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=255)
    head = models.CharField(max_length=255)
    description = models.TextField()
    upcoming_events = models.TextField(blank=True, null=True)
    members = models.TextField()
    projects = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
 
