from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published', 'status')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author', )
    date_hierarchy = 'published'
    ordering = ('status', 'published')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved', 'id', 'post', 'created')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
