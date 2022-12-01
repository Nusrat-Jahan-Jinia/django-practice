from django.db import models
from autoslug import AutoSlugField

class Service(models.Model):
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des=models.TextField()

    service_slug=AutoSlugField(populate_from='service_title',unique=True,null=True,default=None)

# Create your models here.
