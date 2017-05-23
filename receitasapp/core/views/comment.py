from rest_framework import generics
from rest_framework.views import APIView
from core.models import Comment
from core.serializers import CommentSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class CommentList(generics.ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer


class CommentCreate(generics.CreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	authentication_classes = (TokenAuthentication, SessionAuthentication)
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	
	def perform_update(self, serializer):
		serializer.save(user=self.request.user)