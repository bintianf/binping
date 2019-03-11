from django.contrib import admin
from .models import Picture, Age, Group

class PicAdmin(admin.ModelAdmin):
    list_display = ['picurl', 'title', 'created_time', 'modified_time', 'age', 'group']

admin.site.register(Picture, PicAdmin)
admin.site.register(Age)
admin.site.register(Group)