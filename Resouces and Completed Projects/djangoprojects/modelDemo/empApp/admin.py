from django.contrib import admin
from empApp.models import Employee

# Register your models here.
class EmplolyeeAdmin(admin.ModelAdmin):
    list_display=['firstName','lastName','salary']

admin.site.register(Employee,EmplolyeeAdmin)
