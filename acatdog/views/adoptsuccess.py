from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import AnimalInfo
from acatdog.models import AdoptInfo



class AdoSuccess(APIView):
    def post(self, request):
      # try:
          data = request.POST
          photo = data.get("photo", "").strip()
          adoptid = data.get("adoptid", "").strip()
          aniid = data.get("aniid", "").strip()

          AdoptInfo.objects.filter(领养单编号=adoptid).update(领养状态="已领养",合照=photo)

          AnimalInfo.objects.filter(动物id=aniid).update(can_adopt=3)

          return Response({
              'result': "success"
          })
      # except:
      #     return Response({
      #           'result': "failed"
      #       })



