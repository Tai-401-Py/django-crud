from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Snack(models.Model):
    '''
    Snack Model
    '''
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])