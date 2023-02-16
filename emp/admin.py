from django.contrib import admin
from .models import Emp
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','working','phone','address','emp_id','department')         #list_display is a tuple
    list_editable=('working','phone')
    search_fields=('name',)
    list_filter=('working',)

admin.site.register(Emp,EmpAdmin)        # this means full work will happen on Emp model but customization will happen on Class EmpAdmin
