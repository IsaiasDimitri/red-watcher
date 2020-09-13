from django.db import models
from enum import Enum
import graphene

# Create your models here.


class Event(models.Model):
    class EVENTS_TYPES(Enum):
        fire = ('fire', 'Incêndio')
        drowning = ('drowning', 'Afogamento')
        accident = ('accident', 'Acidente Trânsito')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    class STATUS(Enum):
        waiting = ('waiting', 'waiting avaliable team')
        send = ('send', 'team was sent')
        done = ('done', 'event already solved')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    locality_address = models.TextField(blank=True, null=True)

    event_type = models.CharField(
        max_length=32,
        choices=[x.value for x in EVENTS_TYPES])
    event_time = models.DateTimeField(blank=True, null=True)
    event_status = models.CharField(
        max_length=32,
        choices=[x.value for x in STATUS],
        default=STATUS.get_value('waiting'))

    team_confirmation = models.BooleanField(default=False)  # avaliable team
    team_time = models.DateTimeField(
        blank=True, null=True)  # when find a avaliable team
    team = models.JSONField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ": " + self.locality_address
