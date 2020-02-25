from rest_framework import viewsets
from rest_framework import mixins

from .models import Company, Job, Welfare
from .serializers import CompanySerializer, JobSerializer, WelfareSerializer


class CompanyView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    公司
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class JobView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    职位
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class WelfareView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    福利
    """
    queryset = Welfare.objects.all()
    serializer_class = WelfareSerializer
