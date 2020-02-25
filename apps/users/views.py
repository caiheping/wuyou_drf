from rest_framework import viewsets
from rest_framework import mixins
from .serializers import UsersSerializer

from .models import Users


class UsersView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_serializer_class(self):
        """获取当前序列化类的方法"""
        """不同的版本使用不同的序列化类"""
        return UsersSerializer