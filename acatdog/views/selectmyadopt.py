from acatdog.models import AdoptInfo
from acatdog.models import AnimalInfo
from rest_framework.views import APIView
from rest_framework.response import Response


class AdoptList(APIView):
    def get(self, request):
        username = request.GET.get('username', 1)
        adopts = AdoptInfo.objects.filter(用户名=username).order_by('-领养单编号')

        ado = []
        for adopt in adopts:
            photo = AnimalInfo.objects.get(动物id=adopt.动物id)
            ado.append({
                'id': adopt.动物id,
                'num': adopt.领养单编号,
                'state': adopt.领养状态,
                'day': adopt.领养日期,
                'photo':photo.photo
            })
        return Response(ado)
