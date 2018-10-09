from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class DaysAtWork(models.Model):
    # owner      = models.ForeignKey(User, default = 2)
    start_work = models.TimeField()
    end_work   = models.TimeField()
    date_work  = models.DateField()
    sum_day    = models.FloatField(default=0)
    def __str__(self):
        return str(self.date_work)

    class Meta:
        ordering = ['date_work']
