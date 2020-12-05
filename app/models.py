from django.db import models
from django.core.validators import MaxValueValidator
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Email(models.Model):
    MAX_DELAY = 60
    STATUS_CREATED = 1
    STATUS_SHCEDULED = 2
    STATUS_SENT = 3
    STATUS_SENT_ERROR = 4
    STATUS_CHOICES = [
        (STATUS_CREATED, "created"),
        (STATUS_SHCEDULED, "scheduled"),
        (STATUS_SENT, "sent"),
        (STATUS_SENT_ERROR, "error sending"),
    ]
    to_email = models.EmailField()
    body_text = models.CharField(max_length=2048)
    delay = models.PositiveIntegerField(
            validators=[MaxValueValidator(MAX_DELAY)],
            help_text=f'in seconds, max. {MAX_DELAY}',
            default=0,
    )
    status = models.SmallIntegerField(
            choices=STATUS_CHOICES,
            default=STATUS_CREATED,
    )
    created_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField(default=timezone.now)
    scheduled_for = models.DateTimeField()

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.id:
            self.last_update_date = timezone.now()
        else: 
            self.scheduled_for = self.created_date \
                    + timedelta(seconds=self.delay)
        return super(Email, self).save(*args, **kwargs)
