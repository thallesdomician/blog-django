from django.contrib import admin
# Register your models here.
from django.utils.translation import ugettext_lazy as _
from .models import Post, PostAdmin, Category, CategoryAdmin

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = _('Marcos\' Blog')
admin.site.index_title = _('Administration')
admin.site.site_title = _('Marcos\' Blog')
