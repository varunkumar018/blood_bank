from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is an admin
        return request.user.is_authenticated and request.user.role == 'admin'

class IsAdminOrDonor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is either a staff user or admin
        return request.user.is_authenticated and request.user.role in ['admin', 'donor']

class IsAdminOrpatient(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is either a student, staff user, or admin
        return request.user.is_authenticated and request.user.role in ['patient', 'admin']

class IsDonor(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a donor
        return request.user.is_authenticated and request.user.role == 'donor'
    
class IsPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is a patient
        return request.user.is_authenticated and request.user.role == 'patient'
