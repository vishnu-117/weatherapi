from django.db import models

class Weather(models.Model):
    day = models.CharField(max_length=522, null=True, blank=True)
    description = models.CharField(max_length=522, null=True, blank=True)
    temperature = models.CharField(max_length=522, null=True, blank=True)

    class Meta:
        db_table = "guest"

    def __str__(self):
        return self.day
