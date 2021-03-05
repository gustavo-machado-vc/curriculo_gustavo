from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    text = models.TextField()
    image = models.ImageField()
    tools = models.CharField(max_length=300)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
