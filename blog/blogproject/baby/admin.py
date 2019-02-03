from django.contrib import admin
from .models import Picture, Category

class PicAdmin(admin.ModelAdmin):
    list_display = ['picurl', 'title', 'created_time', 'modified_time', 'category']

admin.site.register(Picture, PicAdmin)
admin.site.register(Category)