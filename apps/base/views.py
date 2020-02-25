from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Areas, Banners
from .serializers import AreasSerializer, BannersSerializer


class BannerPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class AreasView(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    区域View
    """
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('is_hot', )


class BannersView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    轮播图View
    """
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Banners.objects.all()
    serializer_class = BannersSerializer
    pagination_class = BannerPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    search_fields = ('url',)
    ordering_fields = ('index', )


class TestView(APIView):
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """
        测试jwt token
        """
        return Response('xxx')


