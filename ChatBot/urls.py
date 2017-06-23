
from django.conf.urls import url,include
from django.contrib import admin
from chat_ml import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('chat_ml.urls')),
]
