from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from acatdog.models import UserInfo
from django.contrib.auth.models import User


class PlayerView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        if not username or not password:
            return Response({
                'result': "用户名和密码不能为空"
            })
        if password != password_confirm:
            return Response({
                'result': "两个密码不一致",
            })
        if User.objects.filter(username=username).exists():
            return Response({
                'result': "用户名已存在"
            })
        user = User(username=username)
        user.set_password(password)
        user.save()
        UserInfo.objects.create(user=user, photo="https://img2.baidu.com/it/u=2161949891,656888789&fm=26&fmt=auto")
        return Response({
            'result': "success"
        })

