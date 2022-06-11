from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import WaitAdopt


# 用来存入

class RHomeView(APIView):
    def post(self, request):
        data = request.POST
        pho = data.get("pho","").strip()
        ill = data.get("ill","").strip()
        loc = data.get("loc","").strip()

        WaitAdopt.objects.create(pho=pho,ill=ill,loc=loc)

        return Response({
            'result': "发帖成功！"
        })


