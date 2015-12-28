from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.authtoken import views as rest_views

import views

VERSION = 'v1'


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    url(r'^api/' + VERSION + '/$', views.api_root),
    url(r'^api/' + VERSION + '/', include('accounts.urls')),
    url(r'^api/' + VERSION + '/', include('clipboards.urls')),
    url(r'^api/' + VERSION + '/', include('snippets.urls')),


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', rest_views.obtain_auth_token)
]