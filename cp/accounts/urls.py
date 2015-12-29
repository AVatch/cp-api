from django.conf.urls import url, include

from rest_framework.authtoken import views as rest_views

import views

# API endpoints
urlpatterns = [
    url(r'^users$',
        views.UserList.as_view(),
        name='user-list'),

    url(r'^users/(?P<pk>[0-9]+)$',
        views.UserDetail.as_view(),
        name='user-detail'),
]