from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import AnimalInfo
from acatdog.models import AdoptInfo



class AdoFail(APIView):
    def post(self, request):
      try:
          data = request.POST
          adoptid = data.get("adoptid", "").strip()
          aniid = data.get("aniid", "").strip()

          AdoptInfo.objects.filter(领养单编号=adoptid).update(领养状态="领养失败")

          AnimalInfo.objects.filter(动物id=aniid).update(can_adopt=1)

          return Response({
              'result': "success"
          })
      except:
          return Response({
                'result': "failed"
            })



