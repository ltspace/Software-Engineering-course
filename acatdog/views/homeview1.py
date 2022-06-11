from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import WaitAdopt



class HomeView1(APIView):
    def get(self, request):

        animals = WaitAdopt.objects.filter().order_by('-num')[1:3]
        anii = []
        for animal in animals:
            anii.append({
                'id': animal.num,
                'sym': animal.ill,
                'img': animal.pho,
                'addr': animal.loc
            })
        return Response(anii)


