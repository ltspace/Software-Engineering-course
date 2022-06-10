from acatdog.models import AnimalInfo
from rest_framework.views import APIView
from rest_framework.response import Response


class AniList(APIView):
    def get(self, request):
        animals = AnimalInfo.objects.filter(can_adopt="1").order_by('动物id')[:6]
        ani = []
        for animal in animals:
            ani.append({
                'id': animal.动物id,
                'name': animal.name,
                'photo': animal.photo,
                'type': animal.type
            })
        return Response(ani)
