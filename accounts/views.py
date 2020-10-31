from django.shortcuts import render
import jwt
from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.permissions import *
from core.helpers.methods import get_type_user
#from accounts.serializers import ProfileSerializer, ListProfileSerializer
from accounts.serializers import UserSerializer
from core.helpers.email import *


class Index(TemplateView):
    template_name = "index.html"


class RegisterUserProfileViewSet(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        user_data = None
        is_super = False
        type_data = get_type_user(request.data.get('type'))
        host = request._current_scheme_host
        password = request.data.get('password')

        try:
            user_data = User.objects.get(username=request.data.get('username'))
        except:
            pass

        if user_data:
            return Response({"response": {"Error": "User Already Exist"}})
        if type_data == None:
            return Response({"response": {"Error": "Invalid type user"}})
        if type_data == 'ADM':
            is_super = True

        user = User.objects.create_user(
            username=request.data.get('username'),
            email=request.data.get('email'),
            is_active=True,
            is_superuser = is_super,
            is_staff = is_super,
            password = password,
            first_name = request.data.get('first_name'),
            last_name = request.data.get('last_name')
        )

        token_user = jwt.encode(
            {'user_id': user.id, 'url':host}, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
        token_user = str(token_user)
        token_user = token_user[2:len(token_user) - 1]

        url_active = host + '/accounts/activate/?token=' + token_user

        objs = {
            'email': user.email,
            'name': str(user.first_name) + ' ' + str(user.last_name),
            'password': password,
            'url': url_active,
        }

        send_email = Email(types=WELCOME,to=user.email,data=objs).send()

        return Response({"response": {"success": "Registration Complete", 'status_email':send_email}})


def ActivateUserProfileViewSet(request):
    try:
        token = request.GET.get('token')
        token_user = jwt.decode(token, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
        User.objects.filter(id=token_user['user_id']).update(is_active=True)
        d_user = User.objects.get(id=token_user['user_id'])
        datas = {'status': 200, 'email': d_user.email, 'url_red': token_user['url']}
        return render(request, 'verify_registrations.html', datas)
    except Exception as e:
        print(e)
        datas = {'status': 400, 'email': '', 'url_red': None}
        return render(request, 'verify_registrations.html', datas)


class GetUserData(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        data = User.objects.get(pk=request.user.id)
        serializer = UserSerializer(data)
        data = serializer.data
        return Response(data)

