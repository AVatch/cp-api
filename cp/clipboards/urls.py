from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rest_views

import views

# API endpoints
urlpatterns = [
    url(r'^clipboards$',
        views.ClipboardList.as_view(),
        name='clipboard-list'),

    url(r'^clipboards/(?P<pk>[0-9]+)$',
        views.ClipboardDetail.as_view(),
        name='clipboard-detail'),

    url(r'^clipboards/(?P<pk>[0-9]+)/snippets$',
        views.ClipboardSnippetList.as_view(),
        name='clipboard-snippets-list'),
]