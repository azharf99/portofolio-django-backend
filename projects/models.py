from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    year = models.IntegerField(max_length=4, default=2025)
    role = models.CharField(max_length=50, default='Fullstack Developer', null=True, blank=True)
    image = models.ImageField(upload_to="img", default='default.png',  null=True, blank=True)
    url = models.URLField(max_length=200, default='https://azharfa.my.id', null=True, blank=True)
    repo_url = models.URLField(max_length=200, default='https://azharfa.my.id', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title