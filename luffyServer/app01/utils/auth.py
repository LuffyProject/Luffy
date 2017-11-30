from rest_framework.authentication import BaseAuthentication
from app01 import models


class LuffyAuthentication(BaseAuthentication):
    """
    自定义认证类
    """
    def authenticate(self, request):
        tk = request.query_parms.get('tk')
        if not tk:
            return (None, None)

        token_obj = models.Token.objects.filter(token=tk).first()
        if not token_obj:
            return (None, None)
        return (token_obj.user, token_obj)
