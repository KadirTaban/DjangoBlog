from django.db import models
# Create your models here.

def upload_path(instance,filename):
    return '/'.join(['covers',str(instance.title),filename])

class Article (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(blank=True, null=True, upload_to=upload_path)
    def __str__(self):
        return self.title