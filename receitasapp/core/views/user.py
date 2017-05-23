from rest_framework import generics
from rest_framework.views import APIView
from core.models import User
from core.serializers import UserCreateSeralizer, UserThinSeralizer, UserSeralizer
from core.permissions import UserHeSelf


class UserCreate(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserCreateSeralizer


class UserDetail(generics.RetrieveUpdateAPIView):
	queryset = User.objects.all()
	serializer_class = UserThinSeralizer
	permission_classes=(UserHeSelf, )


class UserLogin(APIView):
    """Request to get the token for user login"""
    permission_classes=()
    serializer_class = UserSeralizer
    token = None

    def post(self, request, format=None):
        data = request.data
        try:
            usuario = self.authenticate(data['email'], data['password'])
            if usuario:
                try:
                    old_token = Token.objects.get(user=usuario)
                    if old_token:
                        old_token.delete()
                except:
                    pass
                self.token = Token.objects.create(user=usuario)
            else:
                return Response({'errors': [{'error': "User not found or email and password don't macth"}]}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'errors': [{'error': 'User is already logged.'}]}, status=status.HTTP_200_OK)

        if self.token:
            serializer = UserSeralizer(usuario)
            return Response({'token': self.token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
        return Response({'errors': [{'error': 'Error in authentication.'}]}, status=status.HTTP_200_OK)

    def authenticate(self, username=None, password=None, **kwargs):
        """Authentication method."""

        if '@' in username:  # se tiver @ no nome do usuário  username vai ser o email
            kwargs = {'email': username}
        else:
            return None
        try:
            # tentando buscar o usuário no banco
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None