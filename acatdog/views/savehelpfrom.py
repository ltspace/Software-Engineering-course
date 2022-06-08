from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import AssistInfo
# from acatdog.models import UserInfo
from django.contrib.auth.models import User

# 先存动物 后存救助单

class SaveAssist(APIView):
    def post(self, request):      
        data = request.POST
        username = data.get("username", "").strip()
        phonum = data.get("phonum", "").strip()
        email = data.get("email", "").strip()
        addr = data.get("addr", "").strip()
        job = data.get("job", "").strip()
        photo = data.get("photo", "").strip()
        sex = data.get("sex", "").strip()


        # 存动物
        





        obj = User.objects.get(username=username) # 获取user username
        # ok = UserInfo.objects.get(id=obj.userinfo.id) 

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

