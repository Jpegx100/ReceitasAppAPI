from rest_framework import generics
from rest_framework.views import APIView
from core.models import Feel
from core.serializers import FeelSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class FeelList(generics.ListAPIView):
	queryset = Feel.objects.all()
	serializer_class = FeelSerializer


class FeelCreate(generics.CreateAPIView):
	queryset = Feel.objects.all()
	serializer_class = FeelSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class FeelDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Feel.objects.all()
	serializer_class = FeelSerializer

	def perform_update(self, serializer):
		serializer.save(user=self.request.user)