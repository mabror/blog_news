from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index.as_view(), name='main-page'),
    path('register/', views.register, name='register-page'),
    path('reg', views.register_post, name='reg-post'),
    path('login/', views.login_check, name='login'), 
    path('logout/', views.logout_check, name='logout'),
    path('post/', views.post_create, name='post-create'),
    path('post-edit/<int:id>/', views.post_edit, name='post-edit'),
    path('posts/<int:id>/', views.posts, name='posts-page'),
]



if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)