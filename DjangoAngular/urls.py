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
    url(r'^helloParam1/(.+)/$', view.helloParam1),
    # http://127.0.0.1:8000/helloParam1/pathparam/
    url(r'^helloParam2/(.+)/(.+)/$', view.helloParam2),
    # http://127.0.0.1:8000/helloParam2/pathparam1/pathparam2/
    url(r'^helloParam3/p1(\w+)p2(.+)/$', view.helloParam3),
    # http://127.0.0.1:8000/helloParam3/p1pathparam1p2pathparam2/
    url(r'^helloParam4/', view.helloParam4),
    # http://127.0.0.1:8000/helloParam4/?p1=param1&p2=param2
    url(r'^helloParam5$', view.helloParam5),
    # ...... 其他配置
    url(r'^angular/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
