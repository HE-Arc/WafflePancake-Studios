# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views
from friendship.views import view_friends

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.user_detail,
        name='detail'
    ),
    url(
        regex=r'^(?P<to_username>[\w.@+-]+)/addfriend/$',
        view=views.user_addfriend,
        name='addfriend'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/friends/$',
        view=views.user_friends,
        name='friendlist'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
]
