from django.db import models

# Create your models here.

class Articles(models.Model):
    url = models.CharField(max_length=300)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField()


class UploadFileModel(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(null=True, upload_to='result/')