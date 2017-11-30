from rest_framework.permissions import BasePermission



class LuffyPermission(BasePermission):
    """
    根据request.user来判断是否具有权限
    """
    def has_permission(self, request, view):
        if request.user:
            # 如果有值，代表当前用户已登录
            return True
        return False