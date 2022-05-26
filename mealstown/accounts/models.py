from django.db import models
from django.contrib.auth.models import (
    AbstractUser
)
import uuid
from .managers.userManager import (
    UserManager,
    UserAddressBookManager
)
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contact_number = models.CharField(max_length=13,unique=True,null=False,error_messages={
            'unique': _("A user with this contact number already exists.")
        },)
    otp = models.TextField(null=True)
    otp_verified = models.BooleanField(default=False)
    profile_picture = models.TextField(null=True)


    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.contact_number


class UserAddressBook(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    longitude = models.TextField(null=False)
    latitude = models.TextField(null=False)
    house_no = models.CharField(max_length=20, null=False)
    road = models.CharField(max_length=20, null=True)
    address_directions = models.CharField(max_length=50, null=True)
    tag = models.TextField(null=False) # Here tag can be Home, Work or Other

    objects = UserAddressBookManager()

    def __str__(self):
        return self.user