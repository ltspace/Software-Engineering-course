from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from acatdog.models import UserInfo
from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated


class UserInfoSelfChge(APIView):
    def post(self, request):
        # permission_classes = ([IsAuthenticated])
        
        data = request.POST
        # id = request.POST.get('user_id', "")
        # id = data.get("id", "").strip()
        username = data.get("username", "").strip()
        phonum = data.get("phonum", "").strip()
        email = data.get("email", "").strip()
        addr = data.get("addr", "").strip()
        job = data.get("job", "").strip()
        
        obj = User.objects.get(username=username)

        ok = UserInfo.objects.filter(id=obj.userinfo.id).update(phonum=phonum,email=email,addr=addr,job=job)

        # user.set_password(password)
        # user.save()
        # UserInfo.objects.create(user=user, photo="https://img2.baidu.com/it/u=2161949891,656888789&fm=26&fmt=auto")
        return Response({
            'result': str(ok)
        })


        # if not username or not password:
        #     return Response({
        #         'result': "用户名和密码不能为空"
        #     })
        # if password != password_confirm:
        #     return Response({
        #         'result': "两个密码不一致",
        #     })
        # if User.objects.filter(username=username).exists():
        #     return Response({
        #         'result': "用户名已存在"
        #     })

