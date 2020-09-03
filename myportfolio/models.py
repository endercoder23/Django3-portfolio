from django.db import models

# Create your models here.
class personalport(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='portfolioo/pictures/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title