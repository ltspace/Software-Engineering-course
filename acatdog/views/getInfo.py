from acatdog.models import UserInfo
# from game.models.myspace.follow import Follow
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# import traceback

class GetInfo(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id', 1))
            # me_id = request.user.id
            player = UserInfo.objects.get(user_id=user_id)
            return Response({
                'user_id' : user_id,
                'username': player.user.username,
                # 'id': player.id,
                # 'username': player.user.username,
                # 'photo': player.photo,
                # 'followerCount': player.followerCount,
                # 'is_followed': Follow.objects.filter(source=me_id, target=user_id).exists()
            })
        except:
            return Response({
                'result': "输入参数错误"
            })
