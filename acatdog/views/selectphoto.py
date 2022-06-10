from acatdog.models import AdoptInfo
from rest_framework.views import APIView
from rest_framework.response import Response


class AdoList(APIView):
    def get(self, request):
        animals = AdoptInfo.objects.filter(领养状态='已领养').order_by('-领养单编号')[:6]
        ani = []
        for animal in animals:
            ani.append({
                'id': animal.动物id,
                'name': animal.用户名,
                'photo': animal.合照,
                # 'type': animal.type
            })
        return Response(ani)
