from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import AdoptInfo
from acatdog.models import AnimalInfo
# from acatdog.models import AssistInfo
# from django.contrib.auth.models import User
import datetime


# 存领养单 给用户返回领养单编号


class SaveAdopt(APIView):
    def get(self, request):
        aniid = int(request.GET.get('aniid', 1))
        username = request.GET.get('username', 1)
        animal = AnimalInfo.objects.filter(动物id=aniid).update(can_adopt=2)
        # assit = AssistInfo.objects.get(动物id=aniid)

        # 存领养表
        ass = AdoptInfo.objects.create(动物id=aniid,领养日期=datetime.datetime.now(),用户名=username,领养状态="正在领养")

        return Response({
          'adoptid':ass.领养单编号
        })
            #         return Response({
            #     # 'aniid' : aniid,
            #     'name': animals.name,
            #     'photo': animals.photo,
            #     'fur': animals.fur,
            #     'age': animals.age,
            #     'chara': animals.chara,
            #     'type': animals.type,
            #     'vacc': animals.vacc,
            #     'ill': animals.ill,
            #     'addr': animals.addr,
            #     'sex': animals.sex,
            #     'cd': animals.cd,
            #     'jveyu': animals.jveyu,
            # })

