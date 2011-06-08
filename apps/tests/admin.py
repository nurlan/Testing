from django.contrib import admin

from apps.tests.models import Test

class TestAdmin(admin.ModelAdmin):
    list_display = ('name','author','description','status','created_date')
    list_filter = ['status','created_date']
    search_fields = ['name','description']
    date_hierarchy = 'created_date' 
    
admin.site.register(Test, TestAdmin)
