# -*- coding: utf-8 -*-
from django.urls import include, path
from django.contrib import admin
import finweb

urlpatterns = [
    # Examples:
    # url(r'^$', 'fintech.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('finweb/',include('finweb.urls')),
]
