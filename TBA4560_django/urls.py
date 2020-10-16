from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from apps.staticpages import views

urlpatterns = [
    # Main navigation page
    url(r'^$', views.home, name='home'),

    # Apps
    url(r'^eddies/', include('apps.eddies.urls'), name='eddies'),

    # Admin
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)