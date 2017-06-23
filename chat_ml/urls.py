from django.conf.urls import url
from . import views

app_name = 'chatapp'

urlpatterns = [
url(r'^$', views.googleapi, name='home'),

        ]