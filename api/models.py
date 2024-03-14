from django.db import models

# Create your models here.
class Room(models.Model):
    room_number=models.IntegerField(default=True)
    available=models.BooleanField(default=True)

    def __str__(self):
        return str(self.room_number)
