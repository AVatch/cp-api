from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

import views

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^users$',
        views.UserList.as_view(),
        name='user-list'),

    url(r'^users/(?P<pk>[0-9]+)$',
        views.UserDetail.as_view(),
        name='user-detail'),
])