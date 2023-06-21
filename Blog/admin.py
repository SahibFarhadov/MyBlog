from django.contrib import admin
from .models import Blog,Category

class BlogAdmin(admin.ModelAdmin):
    list_display=("title","is_active","is_home","slug")
    list_editable=("is_home","is_active")
    readonly_fields=("slug",)


class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","slug")
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)
