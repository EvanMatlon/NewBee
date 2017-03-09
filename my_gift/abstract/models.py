from django.db import models


# Base models that have some common fields.

class CommonModel(models.Model):
    # Meta data for one object.
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True