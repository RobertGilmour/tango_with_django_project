from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['category', 'title', 'url']}),
    ('Page Statistics', {'fields': ['views']}),
    ]

    list_display = ('title', 'category', 'url')

    list_filter = ['category']

    search_fields = ['title']

admin.site.register(Page, PageAdmin)
