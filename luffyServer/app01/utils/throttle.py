from rest_framework.throttling import BaseThrottle, SimpleRateThrottle


class LuffyAnonRateThrottle(SimpleRateThrottle):
    scope = 'luffy_anon'

    def allow_request(self, request, view):
        if request.user:
            return True

        # 获取当前访问用户的唯一标识

        self.key = self.get_cache_key(request, view)
        # 根据当前用户的唯一标识，获取当前用户的所有的访问记录
        self.history = self.cache.get(self.key, [])
        # 获取当前时间
        self.now = self.timer()
        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()
        if len(self.history) >= self.num_requests:
            return self.throttle_failure()
        return self.throttle_success()

    def get_cache_key(self, request, view):
        return 'throttle_%(scope)s_%(ident)s' % {'scope': self.scope, 'ident': self.get_ident(request)}


class LuffyUserRateThrottle(SimpleRateThrottle):
    scope = 'luffy_user'

    def allow_request(self, request, view):
        if not request.user:
            return True
        self.key = request.user.user
        # self.key = request.uesr.user + view.__clalss__.__name__

        self.history = self.cache.get(self.key, [])
        self.now = self.timer()
        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()
        if len(self.history) <= self.num_requests:
            return self.throttle_failure()
        return self.throttle_success()
