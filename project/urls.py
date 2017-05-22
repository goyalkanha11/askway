from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^askway/', include('askway.urls')),
    url(r'^admin/', admin.site.urls),
]
