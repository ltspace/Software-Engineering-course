from acatdog.models import AnimalInfo
from rest_framework.views import APIView
from rest_framework.response import Response


class AniOne(APIView):
    def get(self, request):
      try:
            aniid = int(request.GET.get('aniid', 1))
            # me_id = request.user.id
            animals = AnimalInfo.objects.get(动物id=aniid)
            return Response({
                # 'aniid' : aniid,
                'name': animals.name,
                'photo': animals.photo,
                'fur': animals.fur,
                'age': animals.age,
                'chara': animals.chara,
                'type': animals.type,
                'vacc': animals.vacc,
                'ill': animals.ill,
                'addr': animals.addr,
                'sex': animals.sex,
                'cd': animals.cd,
                'jveyu': animals.jveyu,
            })
      except:
          return Response({
              'result': "输入参数错误"
          })


        
