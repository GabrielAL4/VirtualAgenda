from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    eventData = models.DateTimeField(verbose_name='Event Data')
    creationData = models.DateTimeField(auto_now=True, verbose_name= 'Creation Data')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Evento'

    def __str__(self):
        return self.title