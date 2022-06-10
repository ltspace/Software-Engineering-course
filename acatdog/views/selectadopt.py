from acatdog.models import AdoptInfo
from rest_framework.views import APIView
from rest_framework.response import Response


class AdoOne(APIView):
    def get(self, request):
      try:
            adoptid = int(request.GET.get('adoptid', 1))
            # me_id = request.user.id
            adopt = AdoptInfo.objects.get(领养单编号=adoptid)
            return Response({
                'state':adopt.领养状态,
                'day':adopt.领养日期,
                'username':adopt.用户名,
                # 'aniid' : aniid,
                # 'name': animals.name,
                # 'photo': animals.photo,
                # 'fur': animals.fur,
                # 'age': animals.age,
                # 'chara': animals.chara,
                # 'type': animals.type,
                # 'vacc': animals.vacc,
                # 'ill': animals.ill,
                # 'addr': animals.addr,
                # 'sex': animals.sex,
                # 'cd': animals.cd,
                # 'jveyu': animals.jveyu,
            })
      except:
          return Response({
              'result': "输入参数错误"
          })


        
