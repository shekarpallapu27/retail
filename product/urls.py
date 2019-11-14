from django.conf.urls import url,include
from django.contrib import admin
from .views import *

urlpatterns = [

    url(r'admin/', admin.site.urls),
    url(r'populate/$', executedata),
    url(r'productdetails/$', webscrapdeatails),
    url(r'update/$', updateproduct),
    url(r'info/$', Product.as_view()),
    url(r'amazon/$', AmazonProductDetails.as_view())



]
