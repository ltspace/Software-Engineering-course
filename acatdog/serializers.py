from rest_framework import serializers
from .models import AdoptInfo, AnimalInfo, AssistInfo, UserInfo, ManagerInfo


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
