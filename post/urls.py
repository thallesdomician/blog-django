from django.urls import path
from .views import PostList, PostView, PostUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<slug:slug>/', PostView.as_view(), name='post_detail'),
    path('<slug:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('<slug:slug>/delete/', PostDelete.as_view(), name='post_delete'),
]
