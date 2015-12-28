from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

import views

# API endpoints
urlpatterns = [
    url(r'^snippets$',
        views.SnippetList.as_view(),
        name='snippet-list'),

    url(r'^snippets/(?P<pk>[0-9]+)$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
]