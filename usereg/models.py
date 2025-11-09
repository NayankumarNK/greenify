from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    # Link to Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Custom fields for your Greenify app
    eco_level = models.CharField(max_length=50, default='Beginner')
    user_points = models.IntegerField(default=0)
    waste_recycled = models.CharField(max_length=50, default='0 kg')
    distance_biked = models.CharField(max_length=50, default='0 km')
    solar_hours = models.CharField(max_length=50, default='0 hrs')
    sustain_score = models.CharField(max_length=10, default='0%')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()