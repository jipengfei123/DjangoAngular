"""DjangoAngular URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from . import view
from . import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^helloWorld/', view.helloWorld),
    url(r'^helloJson1/', view.helloJson1),
    url(r'^helloJson2/', view.helloJson2),
    url(r'^helloModel/', view.helloModel),
    url(r'^helloTemplates/', view.helloTemplates),
    # ...... 其他配置
    url(r'^angular/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
