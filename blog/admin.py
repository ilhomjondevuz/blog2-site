from django.contrib import admin

from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('-created_at',)
    list_filter = ('author', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)