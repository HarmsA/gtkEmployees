from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=800, blank=True)
    job_title = models.CharField(max_length=100, blank=True, verbose_name='Job Title')
    dob = models.DateField(null=True, blank=True, verbose_name='Date of Birth')
    boss = models.CharField(max_length=200, blank=True)
    work_group = models.CharField(max_length=200, blank=True)
    portrait = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.email


class Buisness(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)