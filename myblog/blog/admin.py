from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','tag','pub_time')
    list_filter = ('tag',)

admin.site.register(Article,ArticleAdmin)


# admin.site.register(Article)