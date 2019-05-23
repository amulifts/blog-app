from django.contrib import admin
from apps.post.models import Post, Comment

# Register your models here.

# admin.site.register(Post)
admin.site.register(Comment)


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "created_at", "author"]
    date_hierarchy = "created_at"
    search_fields = ["title"]
    ordering = ["created_at"]
    list_filter = ["author"]
    # fields = [""]


admin.site.register(Post, PostAdmin)
