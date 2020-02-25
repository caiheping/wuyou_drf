from uuid import uuid4

from django.http import HttpResponse
from jwt import InvalidSignatureError
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from django.utils.deprecation import MiddlewareMixin


# 1.每次登录 response 处理 记录 jwt
# 2.每次请求判断 jwt是否与表中相等(相当于 用户 异设备登录获取了新的jwt)  不等 就修改uuid


class ValidTokenMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        self.get_response = get_response
        self.user_jwt = {
            "web": "",
            "mobile": "",
            "iPad": ""
        }

    def process_request(self, request):
        # 用于处理 所有带 jwt 的请求
        jwt_token = request.META.get('HTTP_AUTHORIZATION', None)
        if jwt_token is not None and jwt_token != '':
            data = {
                'token': request.META['HTTP_AUTHORIZATION'].split(' ')[1],
            }
            if self.user_jwt[request.headers._store['platform'][1]] != data['token']:
                return HttpResponse("{'msg','请重新登入'}", content_type='application/json', status=400)

    def process_response(self, request, response):
        # 仅用于处理 login请求
        if request.path_info == '/login':
            rep_data = response.data
            self.user_jwt[request.headers._store['platform'][1]] = rep_data['token']
            return response
        else:
            return response