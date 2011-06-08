from django.contrib import admin

from apps.questions.models import Question,Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    field_sets = [
                  (None,        {'fields':['text']}),
                  ('Date info', {'fields':['created_date']} )
                  ]
    
    inlines = [AnswerInline]
    list_display = ('text','author','test','created_date')
    list_filter = ['created_date']
    search_fields = ['text']
    date_hierarchy = 'created_date'
    
admin.site.register(Question,QuestionAdmin)

