from django.db import models
from django.contrib import admin
from colorfield.fields import ColorField
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from tinymce.models import HTMLField


class Category(models.Model):
    TEXT_COLOR = (
        ('w', 'white'),
        ('b', 'black'),
    )

    class Meta:
        verbose_name_plural = _('Categories')

    name = models.CharField(max_length=15)
    color_text = models.CharField(max_length=1, choices=TEXT_COLOR, default=TEXT_COLOR[1][0])
    color_background = ColorField(default='#A5F8CE')

    def __str__(self):
        return self.name

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name',)

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    subtitle = models.CharField(max_length=255, verbose_name=_('Subtitle'))
    header_image = models.ImageField(upload_to='header/%Y/%m/', null=True, blank=True, verbose_name=_('Header Image'))
    thumbnail_image = models.ImageField(upload_to='thumbnail/%Y/%m/', null=True, blank=True, verbose_name=_('Thumbnail Image'))
    resume = models.TextField(blank=True, null=True, verbose_name=_('Resume'))
    content = HTMLField(blank=True, null=True, verbose_name=_('Content'))
    categories = models.ManyToManyField(Category, verbose_name=_('Categories'))
    slug = models.SlugField(max_length=100, unique=True, default="slug", editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))




    def __str__(self):
        return self.title

    def get_categories(self):
        categories = self.categories.all()
        return ', '.join([x.name for x in categories])

    get_categories.short_description = _('Categories')


    @property
    def header_image_url(self):
        if self.header_image and hasattr(self.header_image, 'url'):
            return self.header_image.url

    @property
    def thumbnail_image_url(self):
        if self.thumbnail_image and hasattr(self.thumbnail_image, 'url'):
            return self.thumbnail_image.url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def has_thumbnail_image(self):
        return True if self.thumbnail_image else False
    has_thumbnail_image.boolean = True
    has_thumbnail_image.short_description = _('Thumbnail')


    def has_header_image(self):
        return True if self.header_image else False
    has_header_image.boolean = True
    has_header_image.short_description = _('Image')


class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Headers'), {
            'fields': (('title', 'subtitle'),),
        }),
        (_('Images'), {
            'fields': (('header_image', 'thumbnail_image',),)
        }),
        (None, {
            'fields': ('resume', 'content', 'categories',)
        }),
        (_('Dates'), {
            'fields': (('created_at', 'updated_at', ),),
            'classes': ['collapse', ]
        })
    )
    autocomplete_fields = ('categories',)

    list_display = ('title', 'subtitle', 'has_header_image', 'has_thumbnail_image', 'get_categories', 'created_at')
    search_fields = ('title', 'subtitle', 'resume', 'content')
    list_filter = ('categories__name',)

    readonly_fields = ('created_at', 'updated_at')
