from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

class UserHeSelf(permissions.BasePermission):
	"""Permission to just the logged user changes he self"""
	def has_object_permission(self, request, view, obj):
		return request.user == obj

class OnlyUserCanPostOrPut(permissions.BasePermission):
	"""Permission that allow all users to GET"""
	def has_object_permission(self, request, view, obj):
		if request.method == 'GET':
			return True
		return IsAuthenticated().has_object_permission(request, view, obj)