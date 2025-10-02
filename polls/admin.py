from django.contrib import admin
from .models import Survey, Question, Choice, Response, Answer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'is_active']
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'survey', 'question_type', 'order']
    list_filter = ['survey', 'question_type']
    inlines = [ChoiceInline]

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['survey', 'created_at', 'user_ip']

admin.site.register(Choice)
admin.site.register(Answer)