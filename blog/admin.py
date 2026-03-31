from django.contrib import admin
from blog.models import Article, ArticleComment

class ArticleCommentInline(admin.TabularInline):
    model = ArticleComment
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'body')
    ordering = ('-created_at',)
    list_filter = ('author', 'created_at', 'updated_at')
    inlines = [ArticleCommentInline]   # MUHIM: Inline shu yerda qo‘shiladi

class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'author', 'created_at', 'updated_at')
    search_fields = ('article__title', 'author__username', 'body')
    ordering = ('-created_at',)
    list_filter = ('author', 'created_at', 'updated_at')

    def article_title(self, obj):
        return obj.article.title
    article_title.short_description = 'Article'

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleComment, ArticleCommentAdmin)
