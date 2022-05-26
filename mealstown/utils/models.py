import uuid
from django.db import models


class BaseModelUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    modified_date = models.DateTimeField(auto_now=True, verbose_name="Modified Date")
    created_by = models.CharField(max_length=255, null=True, blank=True)
    modified_by = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        abstract = True
