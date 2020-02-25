from rest_framework import viewsets
from rest_framework import mixins
from .serializers import ResumeSerializer, ResumeEducationSerializer, ResumeJobSerializer, ResumeWorkingSerializer, ResumeProjectExperienceSerializer
from .models import Resume, ResumeWorking, ResumeProjectExperience, ResumeJob, ResumeEducation


class ResumeView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeEducationView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ResumeEducation.objects.all()
    serializer_class = ResumeEducationSerializer


class ResumeJobView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ResumeJob.objects.all()
    serializer_class = ResumeJobSerializer


class ResumeWorkingView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ResumeWorking.objects.all()
    serializer_class = ResumeWorkingSerializer


class ResumeProjectExperienceView(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ResumeProjectExperience.objects.all()
    serializer_class = ResumeProjectExperienceSerializer