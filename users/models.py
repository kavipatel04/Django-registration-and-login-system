from django.utils import timezone
from typing import Any
from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Event(models.Model):
    sponsor = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(default='Title TBA', max_length=200)
    pub_date = models.DateTimeField('Publish Date ', default=timezone.now())
    event_date = models.DateTimeField('Event Date')
    points = models.FloatField(default=0.0)
    event_s_code = models.IntegerField(unique=True, null=True)
    description = models.TextField(default=None, null=True)

    def __str__(self):
        return self.title

    
    

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class PointReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submitter")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, unique=False)
    report_date = models.DateTimeField('Report Date', default=timezone.now())
    points_requested = models.DecimalField(decimal_places=1, max_digits=10)
    points_granted = models.DecimalField(decimal_places=1,max_digits=10, default = 0.0)
    notes = models.TextField(default=None, null=True)
    verified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="verifier", null=True)

    def __str__(self):
        return "Point Submission for " + self.user.username + " Event: " + self.event.title

    
   
    