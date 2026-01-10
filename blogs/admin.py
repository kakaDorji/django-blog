from django.contrib import admin
from .models import Category,Blog

# for prepopulate field like slug

class BlogAdmin(admin.ModelAdmin):
    # this is tuple so we cannot i mean we cannot kept like that we need to used , to make tuple
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','author','status','is_featured')
    
    search_fields=('id','title','category__category_name','status')
    list_editable=('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)