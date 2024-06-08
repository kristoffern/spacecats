from django.db import models

class SpaceCat(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    age = models.IntegerField()
    mission_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.role})"