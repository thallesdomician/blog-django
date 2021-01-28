from django.db import models
from colorfield.fields import ColorField
from django.utils.translation import gettext as _
from django.template.defaultfilters import slugify, default


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


class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255)
    header_image = models.ImageField(upload_to='block-image/header', null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='block-image/thumbnail', null=True, blank=True)
    resume = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    slug = models.SlugField(max_length=100, unique=True, default="slug")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)



