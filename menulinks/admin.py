from django.contrib import admin
from menulinks.models import MenuLink

class MenuLinkAdmin(admin.ModelAdmin):
    """View for the Admin page"""
    list_display = ('title', 'url', 'weight')

admin.site.register(MenuLink, MenuLinkAdmin)
