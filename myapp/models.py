from django.db import models
import uuid


class Task(models.Model):
    # db_table = 'sgsdgf'
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    text = models.CharField(max_length=50)
    checked = models.BooleanField()
    # unique=True
    # null=True,
    # blank=True,
    # default=False,
    # verbose_name="Check"

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        # unique_together = ['text', 'checked']
