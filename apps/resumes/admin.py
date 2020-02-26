from django.contrib import admin
from resumes.models import Resume, ResumeProjectExperience, ResumeWorking, ResumeJob, ResumeEducation

# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'pic', 'sex', 'experience', 'is_open')

    ordering = ('id',)

    list_per_page = 50


class ResumeWorkingAdmin(admin.ModelAdmin):
    list_display = ('resume', 'company', 'position', 'start_time', 'end_time')

    ordering = ('id',)
    search_fields = ('company',)
    list_per_page = 50


class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ('resume', 'school', 'enrollment_time', 'graduation_time', 'major', 'education')

    ordering = ('id',)
    search_fields = ('school',)
    list_per_page = 50


class ResumeJobAdmin(admin.ModelAdmin):
    list_display = ('resume', 'industry', 'work_type', 'function', 'place')

    ordering = ('id',)
    list_per_page = 50


class ResumeProjectExperienceAdmin(admin.ModelAdmin):
    list_display = ('resume', 'name', 'affiliated_company', 'start_time', 'end_time')

    ordering = ('id',)
    search_fields = ('name',)
    list_per_page = 50


admin.site.register(Resume, ResumeAdmin)
admin.site.register(ResumeWorking, ResumeWorkingAdmin)
admin.site.register(ResumeProjectExperience, ResumeProjectExperienceAdmin)
admin.site.register(ResumeJob, ResumeJobAdmin)
admin.site.register(ResumeEducation, ResumeEducationAdmin)
