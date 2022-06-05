from rest_framework import viewsets
# from ...utils.Authentication import MyJWTAuthentication
from ..models import UserInfo
from acatdog.serializers import UserInfoSerializers
# from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializers
    # permission_classes = permission
    # authentication_classes = [MyJWTAuthentication, SessionAuthentication, BasicAuthentication]

