from django.contrib import admin

from app.models import Answer, Survey, User, Question


# Register your models here.
@admin.register(Survey)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Question)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(User)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['name']