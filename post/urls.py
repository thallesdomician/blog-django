from django.urls import path
from .views import PostList, PostView, PostUpdate, PostDelete, PostCreate
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('new/', login_required(PostCreate.as_view()), name='post_create'),
    path('<slug:slug>/', PostView.as_view(), name='post_detail'),
    path('<slug:slug>/update/', login_required(PostUpdate.as_view()), name='post_update'),
    path('<slug:slug>/delete/', login_required(PostDelete.as_view()), name='post_delete'),
]
