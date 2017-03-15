from rest_framework import permissions

class UserHeSelf(permissions.BasePermission):
	"""Permission to just the logged user changes he self"""
	def has_object_permission(self, request, view, obj):
		return request.user == obj