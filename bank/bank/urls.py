from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('common.urls')),
    url(r'^', include('statements.urls')),
    url(r'^', include('cibil.urls')),
    url(r'^', include('notification.urls')),
]

urlpatterns += (url(r'^admin/django-ses/', include('django_ses.urls')),)
