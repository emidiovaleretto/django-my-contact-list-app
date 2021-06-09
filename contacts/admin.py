from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact', 'creation_date', 'category', 'to_show',)
    list_editable = ('contact', 'to_show',)
    list_display_links = ('name', 'category',)
    list_per_page = 10


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
