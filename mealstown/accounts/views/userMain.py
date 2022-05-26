from rest_framework.response import Response
from rest_framework import (
    status,
    views
)
from ..serializers.userSerializer import (
    UserLoginSerializer,
    UserRegistrationSerializer,
    UserSerializer
)
from ..models import (
    User
)
from utils.common import get_query_param_value, get_request_value_body
from authentication.authentication import JWTAuthentication
import logging
logger = logging.getLogger(__name__)


class UserLogin(views.APIView):
    """
    description : User login API
    created by : <email>
    """
    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, *args, **kwargs):

        username = get_request_value_body(request, 'username', '')
        password = get_request_value_body(request, 'password', '')

        login_serializer = UserLoginSerializer()
        result_data = login_serializer.user_login(username,password)

        if not result_data[0]:
            return Response(result_data[1], status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(result_data[1], status=status.HTTP_200_OK)


class UserRegister(views.APIView):
    """
    description : User registration API
    created by : <email>
    """
    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, *args, **kwargs):

        serializer_add_user_data = UserRegistrationSerializer(data=request.data)
        serializer_add_user_data.is_valid(raise_exception=True)

        created = serializer_add_user_data.user_registration(data=dict(
            user_params=serializer_add_user_data.data))

        if created is False:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'User not created'})
        else:
            return Response({'status': status.HTTP_201_CREATED, 'message': 'User created successfully'})


class UserList(views.APIView):
    """
    description : User list API
    created by : <email>
    """
    authentication_classes = (JWTAuthentication,)

    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, *args, **kwargs):

        user_serializer = UserSerializer()
        result_data = user_serializer.users_list()

        if not result_data[0]:
            return Response(result_data[1], status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(result_data[1], status=status.HTTP_200_OK)



class SendOTP(views.APIView):
    """
    description : Send OTP to entered mobile number
    created by : <email>
    """

    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, *args, **kwargs):

        mobile_number = request.data['mobile_number']

        send_otp = User.objects.send_otp(mobile_number)
        if send_otp[0] ==  True:
            return Response(send_otp[1], status=status.HTTP_200_OK)
        else:
            return Response(send_otp[1], status=status.HTTP_401_UNAUTHORIZED)



class OTPVerification(views.APIView):
    """
    description : Verify OTP to get login
    created by : <email>
    """

    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, *args, **kwargs):

        mobile_number = request.data['mobile_number']
        otp = request.data['otp']

        verification = User.objects.otp_verification(mobile_number, otp)
        if verification[0] ==  True:
            return Response(verification[1], status=status.HTTP_200_OK)
        else:
            return Response(verification[1], status=status.HTTP_401_UNAUTHORIZED)