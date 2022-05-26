from django.db import IntegrityError
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.serializers import (
    ModelSerializer,
)
from ..models import (
    User
)
import logging
import bcrypt


logger = logging.getLogger(__name__)


class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

    def user_login(self, username, password):

        try:
            login_user = User.objects.get_record_by_username(username)
            if login_user is not None:

                try:
                    if login_user.check_password(password):

                        refresh = RefreshToken.for_user(login_user)

                        user_details = {
                            'first_name': login_user.first_name,
                            'last_name': login_user.last_name,
                            'email': login_user.email,
                            'username': login_user.username,
                            'contact_number': login_user.contact_number

                        }

                        return True, {
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                            'user': user_details
                        }
                    else:
                        return False, {
                            "error": "Invalid Password"
                        }

                except Exception as err:
                    logger.error("authenticate_user : error ")
                    logger.error(err)
            else:
                return False, {"error": "Invalid Username"}
        except IntegrityError as err:
            logger.error('User not found')
            logger.error(str(err))
            return False, {"error": "User not found"}


class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            # 'username',
            # 'email',
            'contact_number',
            # 'password'
        ]

    def user_registration(self, data):

        try:
            record = User.objects.create_user(**data)
            return True, record

        except Exception as err:
            logging.info(err)
            return False


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def users_list(self):
        try:
            record = User.objects.get_all_user_list()
            return True, record
        except:
            return False