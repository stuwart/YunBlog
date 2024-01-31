# url的path中，name
from django.contrib import admin
from django.urls import path, include
from article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/article/list/', ArticleListView.as_view(), name='article-list'),
    path('api/article/detail/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('api/tag/list/', TagListView.as_view(), name='tag-list'),
    path('api/tag/detail/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
]
