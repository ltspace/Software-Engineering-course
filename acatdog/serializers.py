from rest_framework import serializers
from .models import AdoptInfo, AnimalInfo, AssistInfo, UserInfo, ManagerInfo


class UserInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class AssistInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AssistInfo
        fields = '__all__'

class AnimalInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimalInfo
        fields = '__all__'

class AdoptInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdoptInfo
        fields = '__all__'

class ManagerInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ManagerInfo
        fields = '__all__'