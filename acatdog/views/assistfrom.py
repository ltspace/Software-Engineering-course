from acatdog.models import AssistInfo
# from acatdog.models import UserInfo
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.contrib.auth.models import User


class AssistOne(APIView):
    def get(self, request):
    #   try:
            assistid = int(request.GET.get('assistid', 1))

            assist = AssistInfo.objects.get(救助单编号=assistid) # 救助者用户名
            # user = User.objects.get(username=assist.用户名)
            # player = UserInfo.objects.get(id=user.id) # 救助者信息

            return Response({
                # 'phonum':player.phonum,
                'day':assist.救助日期
            })
    #   except:
    #       return Response({
    #           'result': "输入参数错误"
    #       })


        
