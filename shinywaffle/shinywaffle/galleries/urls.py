# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^$', view=views.GalleryListView.as_view(),
        name='index'),
    url(regex=r'^delete/$', view=views.GalleryListView.deleteGallery),
    url(regex=r'^new/$', view=views.GalleryNewFormView.as_view(),
        name='new'),

    url(regex=r'^(?P<pk>\d)/$',
        view=views.GalleryDetailView.as_view(),
        name='detail'),
    url(regex=r'^(?P<pk>\d)/delete/$',
        view=views.GalleryDetailView.deleteImage),
    url(regex=r'^(?P<pk>\d)/image/new/$',
        view=views.GalleryEditFormView.as_view(),
        name='edit')
]
