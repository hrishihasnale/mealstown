from django.db import models
import uuid
from .managers.foodMenuManager import (
    CuisineManager,
    CuisineItemManager
)

class Cuisine():

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cuisine_name = models.TextField(null=False)
    cuisine_image = models.TextField(null=True)
    cuisine_type = models.TextField(null=True) # It can be premium, regular or office
    cuisine_description = models.CharField(max_length=100, null=True)

    objects = CuisineManager()

    def __str__(self):
        return self.cuisine_name



class CuisineItem():

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dish_name = models.CharField(max_length=20, null=False)
    dish_price = models.IntegerField(null=False)
    dish_description = models.CharField(max_length=100, null=True)
    dish_image = models.TextField(null=True)
    dish_type = models.TextField(null=True) # Here type can be veg, non-veg or egg
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, blank=False)

    objects = CuisineItemManager()

    def __str__(self):
        return self.dish_name