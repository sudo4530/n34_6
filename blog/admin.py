from django.contrib import admin
from .models import Blog, Comments, Tags

# admin.site.register(BlogTest)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "author", "status", "publish_date", "update_date")


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "blog", "create_date")

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("name", )
