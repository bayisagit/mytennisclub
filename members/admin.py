from django.contrib import admin
from .views import Member

# Register your models here.

class Memberadmin(admin.ModelAdmin):
    list_display=("firstname","lastname","joineddate")
    

admin.site.register(Member,Memberadmin)
