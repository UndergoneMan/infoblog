from django.contrib import admin

# Register your models here.
from posts.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'active')
    list_filter = ("active",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'body', 'author', 'created_on', 'active')
    list_filter = ("active",)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
