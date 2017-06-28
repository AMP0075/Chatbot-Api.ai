
from django.conf.urls import url,include
from django.contrib import admin
from chat_ml import urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('chat_ml.urls')),
]
