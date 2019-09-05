from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Event(models.Model):
    name = models.CharField('Event name', max_length=60)
    event_date = models.DateField('Event date')
    time_start = models.TimeField('Event start time')
    time_end = models.TimeField('Event end time')
    venue = models.CharField(max_length=120)
    description = models.TextField(max_length=240)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    date_created = models.DateTimeField(default=timezone.now)
    attendee = models.ManyToManyField(User, related_name='event_attendations')

    class Meta:
        indexes = [models.Index(fields=['creator'])]
        verbose_name = 'event'
        verbose_name_plural = 'events'

    def get_absolute_url(self):
        return f"/events/{self.pk}"

    def __str__(self):
        return self.name
