from django.db import models


# Create your models here.
class FilesAdmin(models.Model):
    objects = None
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=100)

    def _str_(self):
        return self.title
