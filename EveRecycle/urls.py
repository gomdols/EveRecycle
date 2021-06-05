from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from post.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/', include('post.urls')),
]
