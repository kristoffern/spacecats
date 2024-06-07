from django.db import models

class SpaceCat(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)  # Tester, Developer, etc.
    age = models.IntegerField()
    mission_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.role})"

class Mission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    launch_date = models.DateField()
    spacecats = models.ManyToManyField(SpaceCat, related_name='missions')

    def __str__(self):
        return self.name