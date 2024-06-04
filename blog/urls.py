from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/like/', views.add_like, name='add_like'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user/<str:username>/follow/', views.follow_unfollow_user, name='follow_unfollow_user'),
    path('user/<str:username>/', views.profile, name='profile'),
    path('post/<int:pk>/comment/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'),
    path('posts/following/', views.following_posts, name='following_posts'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('following/', views.following_list, name='following_list'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
