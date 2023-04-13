from django.db import models

# Create your models here.

class SoftwareEngineer(models.Model):
    name = models.CharField(max_length=255)
    skills = models.TextField()
    information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class DataEngineer(models.Model):
    name = models.CharField(max_length=255)
    skills = models.TextField()
    information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SecurityEngineer(models.Model):
    name = models.CharField(max_length=255)
    skills = models.TextField()
    information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class GameEngineer(models.Model):
    name = models.CharField(max_length=255)
    skills = models.TextField()
    information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name