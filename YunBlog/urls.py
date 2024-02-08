# url的path中，name
from django.contrib import admin
from django.urls import path, include
from article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/article/', ArticleListView.as_view(), name='article-list'),
    path('api/article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('api/tag/', TagListView.as_view(), name='tag-list'),
    path('api/tag/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]
