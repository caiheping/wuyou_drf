from rest_framework import serializers
from .models import Users


# 版本1
class UsersSerializer(serializers.ModelSerializer):
    """
    area
    """
    class Meta:
        model = Users
        fields = "__all__"
