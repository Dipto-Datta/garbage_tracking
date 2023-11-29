from rest_framework.routers import DefaultRouter
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *


router = DefaultRouter()

router.register(r'v1/recyling_center', reclying_center_view)
router.register(r'v1/gazrbage_type', garbage_type_view)


urlpatterns = [
    path('', include(router.urls)), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)