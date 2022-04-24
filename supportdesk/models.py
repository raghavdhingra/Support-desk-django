from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class RESOLUTION_STATUS(models.TextChoices):
        IN_PROGRESS = 'progress', _('Progress')
        COMPLETED = 'completed', _('Completed')

# Create your models here.
class Request(models.Model):
  title = models.CharField(blank=False, null=False, max_length=200, default='')
  description = models.TextField(default="", null=True, blank=True)
  assigned_to = models.ForeignKey(User, primary_key=False, null=True, related_name="assignee", blank=True, on_delete=models.SET_NULL)
  created_by = models.ForeignKey(User, primary_key=False, null=True, related_name="creator", blank=True, on_delete=models.CASCADE)
  is_priority = models.BooleanField(blank=False, null=False, default=False)
  status = models.CharField(max_length=20, choices=RESOLUTION_STATUS.choices, default=RESOLUTION_STATUS.IN_PROGRESS)
  created_on = models.DateTimeField(blank=True, null=True, default=timezone.now)

  def publish(self):
        self.created_on = timezone.now()
        self.save()

  def __str__(self):
      return self.title