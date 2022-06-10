from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import AdoptInfo
from acatdog.models import AnimalInfo
from django.contrib.auth.models import User
import datetime


# 先存动物 后存救助单


class SaveAdopt(APIView):
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
        can_adopt = data.get("can_adopt","").strip()

        # 存动物
        
        if not cd and can_adopt=="可":
            return Response({
                'result': "选择可领养，需要填写您的电话信息，方便领养人与您联系"
            })
        if not addr and can_adopt=="可":
            return Response({
                'result': "选择可领养，需要填写您的地址，方便领养人与您联系"
            })

        ani=AnimalInfo.objects.create(name=name,photo=photo,fur=fur,age=age,chara=chara,
        type=type,vacc=vacc,ill=ill,addr=addr,sex=sex,cd=cd,jveyu=jveyu,can_adopt=can_adopt)
        

        # 存救助表
        obj = User.objects.get(username=username)  # 获取user username
        ass = AssistInfo.objects.create(动物id=ani.动物id,救助日期=datetime.datetime.now(),用户名=username)

        return Response({
            'result': "填写救助单成功!您救助的动物id是:"+str(ani.动物id)+"。"
        })

