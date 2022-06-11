from acatdog.models import AssistInfo
from acatdog.models import AnimalInfo
from rest_framework.views import APIView
from rest_framework.response import Response


class AssistList(APIView):
    def get(self, request):
        username = request.GET.get('username', 1)
        assists = AssistInfo.objects.filter(用户名=username).order_by('-救助单编号')

        ass = []
        for assist in assists:
            photo = AnimalInfo.objects.get(动物id=assist.动物id)
            ass.append({
                'id': assist.动物id,
                'num': assist.救助单编号,
                'day': assist.救助日期,
                'photo':photo.photo
            })
        return Response(ass)
