# url的path中，name
from django.contrib import admin
from django.urls import path, include
from article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('tag/', TagList.as_view()),
    path('tag/<int:pk>/', TagDetail.as_view()),
]
