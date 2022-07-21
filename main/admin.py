from django.contrib import admin
from main.models import loginfo
# Register your models here.
class Loginfo_admin(admin.ModelAdmin):
    list_display= ['email','uname','address','city','user_key']
    readonly_fields = ['unique_code']
    raw_id_fields = ['user_key']
    

admin.site.register(loginfo, Loginfo_admin)