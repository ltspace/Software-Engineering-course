from rest_framework.views import APIView
from rest_framework.response import Response
from acatdog.models import UserInfo
from django.contrib.auth.models import User


class UserInfoSelfChge(APIView):
    def post(self, request):
        # permission_classes = ([IsAuthenticated])
        
        data = request.POST
        # id = request.POST.get('user_id', "")
        # id = data.get("id", "").strip()
        username = data.get("username", "").strip()
        phonum = data.get("phonum", "").strip()
        email = data.get("email", "").strip()
        addr = data.get("addr", "").strip()
        job = data.get("job", "").strip()
        photo = data.get("photo", "").strip()
        sex = data.get("sex", "").strip()
        crepoint = data.get("crepoint","").strip()
        obj = User.objects.get(username=username)

        if len(phonum) > 13 :
            return Response({
                'result' : "手机号位数超出限制"
            })
        if email.find("@") == -1 or not email.endswith('.com'):
            return Response({
                'result' : "邮箱格式不正确"
            })
            
        ok = UserInfo.objects.filter(id=obj.userinfo.id).update(sex=sex,phonum=phonum,photo=photo,email=email,addr=addr,job=job,crepoint=crepoint)

        return Response({
            'result': str(ok)
        })


        # if not username or not password:
        #     return Response({
        #         'result': "用户名和密码不能为空"
        #     })
        # if password != password_confirm:
        #     return Response({
        #         'result': "两个密码不一致",
        #     })
        # if User.objects.filter(username=username).exists():
        #     return Response({
        #         'result': "用户名已存在"
        #     })

