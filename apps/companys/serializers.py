from rest_framework import serializers

from .models import Company, Job, Welfare


class CompanySerializer(serializers.ModelSerializer):
    """
    公司
    """
    class Meta:
        model = Company
        fields = "__all__"


class JobSerializer(serializers.ModelSerializer):
    """
    职位
    """

    class Meta:
        model = Job
        fields = "__all__"


class WelfareSerializer(serializers.ModelSerializer):
    """
    职位
    """

    class Meta:
        model = Welfare
        fields = "__all__"
