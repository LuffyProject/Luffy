from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from . import models
from app01.utils.commons import gen_token
from rest_framework.views import Response
from rest_framework import serializers

class LoginView(APIView):
    """
    登录
    """

    def get(self, request, *args, **kwargs):
        return HttpResponse('OK')

    # def options(self, request, *args, **kwargs):
    #     response = {}
    #     # print('option')
    #     return JsonResponse(response)

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        user = request.data.get("user")
        print(request.data)
        pwd = request.data.get("pwd")
        user_obj = models.UserInfo.objects.filter(username=user, password=pwd).first()

        if user_obj:
            tk = gen_token(user)  # 生成token
            models.Token.objects.update_or_create(user=user_obj, defaults={"token": tk})
            ret['code'] = 1001
            ret['token'] = tk
            ret['name'] = user
        else:
            ret['msg'] = '用户或密码错误'
        response = JsonResponse(ret)
        return response


class IndexView(APIView):
    """
    主页

    """
    pass

class CourseSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'level_name', 'brief']


class CourseDetailSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name')
    level = serializers.CharField(source='course.get_level_display')
    # level = serializers.SerializerMethodField()
    class Meta:
        model = models.CourseDetail
        fields = ['id', 'hours', 'level', 'course_name', 'why_study', 'prerequisite']
    # def get_level(self,obj):
    #     return '中级'


class CourseView(APIView):
    """
    课程类列表
    """
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': {}}
        pk = kwargs.get('pk')

        if pk:

            detail_obj = models.CourseDetail.objects.get(course_id=pk)
            ser = CourseDetailSerializer(instance=detail_obj, many=False)
            response['data']['coursedetail'] = ser.data
        else:
            course_obj = models.Course.objects.all()
            ser = CourseSerializer(instance=course_obj, many=True, context={'request': request})
            response['data'] = ser.data
        return Response(response)
        # return HttpResponse(ser)

    def post(self, request, *args, **kwargs):

        pass





class RouterSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.UserInfo
        fields = "__all__"


class RouterView(APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk')
        if pk:
            obj = models.UserInfo.objects.filter(pk=pk).first()
            ser = RouterSerializer(instance=obj, many=False)
        else:
            user_list = models.UserInfo.objects.all()
            ser = RouterSerializer(instance=user_list, many=True)
        return HttpResponse(ser.data)
