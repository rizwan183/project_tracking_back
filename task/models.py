from django.db import models
import uuid
import sys

sys.path.append("..")
from accounts.models import User
from project.models import Project

STATUS = (
    ('Cancelled', 'CANCELLED'),
    ('Completed', 'COMPLETED'),
    ('In Progress', 'IN PROGRESS'),
    ('Not Started', 'NOT STARTED'),
    ('On Hold', 'ON HOLD'),
    ('Past Due', 'PAST DUE'),
)


class Task(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_created_by')
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_assign_to', default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=1000)
    task_description = models.CharField(max_length=5000)
    task_status = models.CharField(choices=STATUS, max_length=55)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    started_on = models.DateField()
    completion_date = models.DateField(default=None)

    def __str__(self):
        return self.task_name
