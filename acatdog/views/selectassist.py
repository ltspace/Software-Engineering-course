from acatdog.models import AssistInfo
from acatdog.models import UserInfo
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User


class AssOne(APIView):
    def get(self, request):
    #   try:
            aniid = int(request.GET.get('aniid', 1))
            # me_id = request.user.id
            assist = AssistInfo.objects.get(动物id=aniid) # 救助者用户名
            user = User.objects.get(username=assist.用户名)
            player = UserInfo.objects.get(id=user.id) # 救助者信息

            return Response({
                'phonum':player.phonum,
            })
    #   except:
    #       return Response({
    #           'result': "输入参数错误"
    #       })


        