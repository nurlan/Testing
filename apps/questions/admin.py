from django.contrib import admin

from apps.questions.models import Question,Answer

admin.site.register(Question)
admin.site.register(Answer)
