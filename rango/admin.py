from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

#admin.site.register(Category)

#class PageAdmin(admin.ModelAdmin):
    #list_display = ('title', 'category', 'url')
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

#admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)


