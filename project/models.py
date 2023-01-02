from django.db import models
import uuid
import sys
sys.path.append("..")
from accounts.models import User

STATUS = (
    ('Cancelled', 'CANCELLED'),
    ('Completed', 'COMPLETED'),
    ('In Progress', 'IN PROGRESS'),
    ('Not Started', 'NOT STARTED'),
    ('On Hold', 'ON HOLD'),
    ('Past Due', 'PAST DUE'),
)


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE,related_name='assign_to')
    project_name = models.CharField(max_length=1000)
    project_description = models.CharField(max_length=5000)
    project_status = models.CharField(choices=STATUS, max_length=55)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    started_on = models.DateField()
    completion_date = models.DateField()
    def __str__(self):
        return self.project_name
