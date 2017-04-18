# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # url(
    #     regex=r'^$',
    #     view=views.GalleryListView.as_view(),
    #     name='list'
    # ),
    url(regex=r'^$', view=views.gallery_list_view,
        name='index'),
    url(regex=r'^(?P<username>[\w.@+-]+)/$', view=views.gallery_userlist_view,
        name='userlist'),
    url(regex=r'^new/$', view=views.gallery_new_form_view,
        name='new'),
    # url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),
    # url(
    #     regex=r'^~redirect/$',
    #     view=views.UserRedirectView.as_view(),
    #     name='redirect'
    # ),
    url(regex=r'^display/(?P<pk>\d)/$',
        view=views.GalleryDetailView.as_view(),
        name='detail'),
    url(regex=r'^edit/(?P<pk>\d)/$',
        view=views.gallery_edit_form_view,
        name='edit')
    # url(
    #     regex=r'^~update/$',
    #     view=views.UserUpdateView.as_view(),
    #     name='update'
    # ),
]
