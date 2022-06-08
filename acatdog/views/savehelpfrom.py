from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import AssistInfo
from acatdog.models import UserInfo
from django.contrib.auth.models import User

from pcatdog.acatdog.models import AnimalInfo

# 先存动物 后存救助单


class SaveAssist(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        name = data.get("name","").strip()
        photo = data.get("photo","").strip()
        fur = data.get("fur","").strip()
        age = data.get("age","").strip()
        chara = data.get("chara","").strip()
        type = data.get("type","").strip()
        vacc = data.get("vacc","").strip()
        ill = data.get("ill","").strip()
        addr = data.get("addr","").strip()
        sex = data.get("sex","").strip()
        cd = data.get("cd","").strip()
        jveyu = data.get("jveyu","").strip()


        # 存动物
        ani=AnimalInfo.objects.create(name=name,photo=photo,fur=fur,age=age,chara=chara,
        type=type,vacc=vacc,ill=ill,addr=addr,sex=sex,cd=cd,jveyu=jveyu)
        

        # 存救助表
        obj = User.objects.get(username=username)  # 获取user username
        # ok = UserInfo.objects.get(id=obj.userinfo.id)
        ass = AssistInfo.objects.create()
        # user.set_password(password)
        # user.save()
        # UserInfo.objects.create(user=user, photo="https://img2.baidu.com/it/u=2161949891,656888789&fm=26&fmt=auto")
        return Response({
            'result': str(ani)+str()
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
