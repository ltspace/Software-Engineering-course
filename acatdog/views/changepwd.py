from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login
from acatdog.models import UserInfo
from django.contrib.auth.models import User


class ChangePwd(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        new_password = data.get("new_password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        
        verification=User.check_password(User.objects.get(username=username),password)
        if verification==False:
          return Response({
              'result': "密码不正确！请重新输入！"
              })
        if not new_password or not password_confirm:
            return Response({
                'result': "新密码不能为空"
            })
        if new_password != password_confirm:
            return Response({
                'result': "两个密码不一致",
            })

        u = User.objects.get(username=username)
        u.set_password(new_password)
        u.save()

        return Response({
            'result': "success"
        })
