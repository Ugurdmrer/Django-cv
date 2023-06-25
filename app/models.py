from django.db import models

# Create your models here.
class project(models.Model):
    
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField()
    
    
class About(models.Model):
    
    def __str__(self) -> str:
        return self.header
    
    header = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    icon = models.TextField(max_length=50)
    date = models.DateField()
    
class Service(models.Model):
    
    def __str__(self) -> str:
        return self.header
    
    header = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    icon = models.TextField(max_length=50)
    link = models.URLField(100)
    
class Portfolio(models.Model):
    
    def __str__(self) -> str:
        return self.header
    
    header = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField()
    
    
class Comment(models.Model):
    
    def __str__(self) -> str:
        self.name
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    
class Blog(models.Model):
    
    def __str__(self) -> str:
        return self.header
    
    header = models.CharField(max_length=50)
    subHeader = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    
