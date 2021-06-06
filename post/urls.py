from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'archivements', views.ArchivementViewSet)
router.register(r'boards', views.BoardViewSet)
router.register(r'bulletins', views.BulletinViewSet)
router.register(r'recycle_tags', views.RecycleTagViewSet)
router.register(r'memos', views.MemoViewSet)
router.register(r'clear_archivements', views.ClearArchivementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]