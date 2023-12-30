
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from Home import urls
import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(Home.urls)),
    path("predict/",include("predict.urls")),
    path("Teacher/",include("Teacher.urls"))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
