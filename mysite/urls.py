"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers

from mysite.myapp import views as myapp_views

#from . import views

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'lines', myapp_views.LineViewSet)
router.register(r'words', myapp_views.WordViewSet)


urlpatterns = patterns('',
    # This is going to be our home view.
    # We'll uncomment it later
    url(r'^$', 'mysite.myapp.views.home', name='home'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^hello/', 'mysite.myapp.views.hello'),
    url(r'^loadwords/', 'mysite.myapp.views.loadwords'),
    url(r'^example/', 'mysite.myapp.views.example'),
    url(r'^example2/', 'mysite.myapp.views.example2'),
    url(r'^test/', 'mysite.static.js.test.index'),

    url(r'^newpagewords/', 'mysite.myapp.views.newpagewords'),
    url(r'^loadwords/', 'mysite.myapp.views.loadwords'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^register/$', myapp_views.UserFormView.as_view(), name='register'),

    url(r'^wordajax/$', myapp_views.wordajax.as_view(), name='ajaxword'),
    url(r'^wordselectionajax/$', myapp_views.WordSelectionAjax.as_view(), name='wordselectionajax')
)