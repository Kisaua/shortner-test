from django.db import models
from datetime import datetime, timedelta

# Create your models here.


class Shortner(models.Model):
    urlHash = models.CharField('ULR Hash', max_length=16, blank=False)
    urlOriginal = models.URLField(max_length=512, blank=False)
    createdDate = models.DateTimeField(default=datetime.now(), blank=True)
    expirationDate = models.DateTimeField(default=datetime.now()+timedelta(hours=1), blank=True)
