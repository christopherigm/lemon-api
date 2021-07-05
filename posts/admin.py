from django.contrib import admin
from posts.models import (
    Category,
    Post,
    Hashtag
)

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'hashtag',
        'enabled'
    ]
    search_fields = ('title', 'slug', 'description',)
    list_filter = ('enabled',)
    readonly_fields = ('version',)
admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'category',
        'enabled'
    ]
    search_fields = ('title', 'slug', 'description', 'category')
    list_filter = ('enabled', 'category')
    readonly_fields = ('version',)
admin.site.register(Post, PostAdmin)


class HashtagAdmin(admin.ModelAdmin):
    list_display = [
        'hashtag',
    ]
    search_fields = ('hashtag',)
    readonly_fields = ('version',)
admin.site.register(Hashtag, HashtagAdmin)
