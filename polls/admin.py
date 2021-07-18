from django.contrib import admin

from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date')


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass
