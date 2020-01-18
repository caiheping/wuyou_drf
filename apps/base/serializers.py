from rest_framework import serializers
from .models import Banners, Areas


class AreasSerializer(serializers.ModelSerializer):
    """
    区域
    """
    class Meta:
        model = Areas
        fields = "__all__"


class BannersSerializer(serializers.HyperlinkedModelSerializer):
    """
    banner
    """
    url = serializers.CharField(label='url地址', error_messages={'blank': 'url地址不能为空'})
    index = serializers.CharField(required=True, label='索引')

    class Meta:
        model = Banners
        fields = "__all__"
