from django.db import models
from django.apps import apps
from django.contrib.auth.hashers import make_password
import logging
logger = logging.getLogger(__name__)



class UserManager(models.Manager):
    '''
    creating a manager for a custom user model
    '''

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def create_user(self, **kwargs):
        return self.get_queryset().create_user(**kwargs)

    def get_record_by_username(self,username):
        return self.get_queryset().get_record_by_username(username)

    def get_all_user_list(self):
        return self.get_queryset().get_all_user_list()

    def send_otp(self,mobile_number):
        return self.get_queryset().send_otp(mobile_number)

    def otp_verification(self,mobile_number, otp):
        return self.get_queryset().otp_verification(mobile_number, otp)

class UserQuerySet(models.QuerySet):
    """
    Users QuerySet.
    """

    def create_user(self, **kwargs):

        try:
            user_data_serializer = kwargs['user_params']
            first_name = user_data_serializer['first_name']
            last_name = user_data_serializer['last_name']
            # username = user_data_serializer['contact_number']
            # email = user_data_serializer['email']
            contact_number = user_data_serializer['contact_number']
            # password = make_password(user_data_serializer['password'])

            mdl_user = apps.get_model(app_label='accounts', model_name='User')
            user = mdl_user()
            user.first_name = first_name
            user.last_name = last_name
            user.username = contact_number
            # user.email = email
            user.contact_number = contact_number
            # user.password = password
            user.save()

            return True, user
        except Exception as e:
            return False


    def get_record_by_username(self, username):

        try:
            return self.get(is_active=1, username=username)

        except Exception as err:
            logger.error("UserQuerySet : get_record_by_user_name : error ")
            logger.error(err)

            return None

    def get_all_user_list(self):
        return self.filter().values('username','email','contact_number')


    def send_otp(self,mobile_number):
        try:

            otp_value = '1212'

            user = self.get(contact_number=mobile_number)
            user.otp = otp_value
            user.save()
            return True, {"message": "Otp Has Been Sent"}

        except Exception as err:
            logger.error("UserQuerySet : send_otp : error ")
            logger.error(err)
            return False, {"message": "Invalid Mobile Number"}


    def otp_verification(self,mobile_number, otp):
        try:
            check_otp = self.filter(contact_number=mobile_number, otp=otp)
            if check_otp:
                return True, {"message":"Otp Has Been Verified"}
            else:
                return False, {"message": "Invalid Otp, Please Check Again"}

        except Exception as err:
            logger.error("UserQuerySet : otp_verification : error ")
            logger.error(err)
            return False, {"message": "Something Went Wrong"}


class UserAddressBookManager(models.Manager):
    '''
    creating a manager for a user address model
    '''

    def get_queryset(self):
        return UserAddressBookQuerySet(self.model, using=self._db)


class UserAddressBookQuerySet(models.QuerySet):

    pass