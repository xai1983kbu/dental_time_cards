from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class DaysAtWork(models.Model):
    owner      = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    start_work = models.TimeField()
    end_work   = models.TimeField()
    date_work  = models.DateField()
    sum_day    = models.FloatField(default=0)

    def __str__(self):
        return str(self.date_work)

    class Meta:
        ordering = ['date_work']