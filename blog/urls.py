from django.urls import path
from .views import (PostListView, PostView, PostListPopular,
                    PostComment, PostLike, CommentLike,
                    PostCreate, PostUpdate, Report,
                    PostReadLater, PostDelete)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreate.as_view(), name='post_new'),
    path('<slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('<slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('most-popular/', PostListPopular.as_view(), name='post_popular'),
    path('<slug>/', PostView.as_view(), name='post_detail'),
    path('<slug>/comments/', PostComment.as_view(), name='post_comment'),
    path('<slug>/likes/', PostLike.as_view(), name='post_like'),
    path('<slug>/add-to-list/', PostReadLater.as_view(), name='post_read_list'),
    path('comments/<id>/like', CommentLike.as_view(), name='comment_like'),
    path('comments/<id>/report', Report.as_view(), name='comment_report')
]
