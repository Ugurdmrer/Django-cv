from django.db import models

# Create your models here.
class project(models.Model):
    
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField()