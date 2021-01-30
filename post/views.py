from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Category
from django.shortcuts import render
from django.utils.translation import gettext as _

class HomeView(View):
    def get(self, request):
        return render(request=request, template_name='base.html')

class PostList(ListView):
    model = Post

    paginate_by = 2
    ordering = ['-created_at']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(post__isnull=False).order_by('name')
        context['latest'] = Post.objects.all().order_by('-created_at')[:2]
        context['subheader'] = _('Blog')
        return context

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'header_image', 'thumbnail_image', 'resume', 'content', 'categories']
    template_name_suffix = '_update_form'
    def get_success_url(self, **kwargs):
        return reverse_lazy("post_detail", args=(self.object.slug,))

class PostView(DetailView):
    model = Post

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


