from django.db import models

# Create your models here.
class Software(models.Model):
    Sub_branch = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Sub_branch

class Gaming(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Skill(models.Model):
    Branch = models.ForeignKey(Software, on_delete=models.CASCADE)
    Videos = models.TextField()
    Program_Language = models.TextField()
    Book_ref = models.TextField()
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # if len(self.text) >= 50:
        #     s = self.text
        #     s.upper()
        return self.Program_Language