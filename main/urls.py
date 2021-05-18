from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Index.as_view(), name='main-page'),
    path('register/', views.register, name='register-page'),
    path('reg', views.register_post, name='reg-post'),
    path('login/', views.login_check, name='login'), 
    path('logout/', views.logout_check, name='logout'),
    # path('post/', views.post_create, name='post-create'),
    path('post/', views.PostCreate.as_view(), name='post-create'),
    path('post-edit/<int:pk>/', views.PostEdit.as_view(), name='post-edit'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts-page'),
    path('comment/<int:id>/', views.comment, name='comment'),
    path('like/<int:id>/', views.add_like, name='like'),
    path('delete/<int:id>/', views.DeletePost.as_view(), name='delete'),




]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)