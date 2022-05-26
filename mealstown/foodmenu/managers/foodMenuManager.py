from django.db import models
from django.apps import apps
from django.contrib.auth.hashers import make_password
import logging
logger = logging.getLogger(__name__)



class CuisineManager(models.Manager):
    """
    creating a manager for menu category model
    """

    def get_queryset(self):
        return CuisineQuerySet(self.model, using=self._db)


class CuisineQuerySet(models.QuerySet):
    """
     Menu category QuerySet.
    """
    pass



class CuisineItemManager(models.Manager):
    """
    creating a manager for menu category model
    """

    def get_queryset(self):
        return CuisineItemQuerySet(self.model, using=self._db)


class CuisineItemQuerySet(models.QuerySet):

    pass