from django.urls import path
from app_blog import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path(r'', views.HomePageView.as_view()),
 path('article/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)