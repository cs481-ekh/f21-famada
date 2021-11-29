from django.db import models


# Create your models here.
class FilesModel(models.Model):
    csv = models.FileField(upload_to='csvs/')
