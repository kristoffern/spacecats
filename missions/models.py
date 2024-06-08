from django.db import models
from spacecats.models import SpaceCat

class Mission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    launch_date = models.DateField()
    spacecats = models.ManyToManyField(SpaceCat, related_name='missions')

    def __str__(self):
        return self.name