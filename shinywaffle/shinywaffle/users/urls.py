# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views
from friendship.views import view_friends, friendship_add_friend

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
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<username>[\w-]+)/friendlist/$',
        view=views.user_search_friend,
        kwargs={'template_name' : 'users/user_friendlist.html'},
        name='friendlist'
    ),
    url(
        regex=r'^(?P<to_username>[\w-]+)/addfriend/$',
        view=friendship_add_friend,
        kwargs={'template_name' : 'users/user_friendadd.html'},
        name='addfriend'
    ),
]
