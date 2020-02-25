from rest_framework import serializers
from .models import Resume, ResumeWorking, ResumeProjectExperience, ResumeJob, ResumeEducation


class ResumeSerializer(serializers.ModelSerializer):
    """
    area
    """
    class Meta:
        model = Resume
        fields = "__all__"


class ResumeWorkingSerializer(serializers.ModelSerializer):
    """
    area
    """
    class Meta:
        model = ResumeWorking
        fields = "__all__"


class ResumeProjectExperienceSerializer(serializers.ModelSerializer):
    """
    area
    """
    class Meta:
        model = ResumeProjectExperience
        fields = "__all__"


class ResumeJobSerializer(serializers.ModelSerializer):
    """
    area
    """
    class Meta:
        model = ResumeJob
        fields = "__all__"


class ResumeEducationSerializer(serializers.ModelSerializer):
    """
    area
    """
    class Meta:
        model = ResumeEducation
        fields = "__all__"
