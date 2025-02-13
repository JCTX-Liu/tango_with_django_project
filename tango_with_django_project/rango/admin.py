from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

admin.site.register(Page, PageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)