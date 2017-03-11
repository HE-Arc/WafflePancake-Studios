# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gallery

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


class GalleryListView(LoginRequiredMixin, ListView):
    model = Gallery
    # These next two lines tell the view to index lookups by username
    slug_field = 'title'
    slug_url_kwarg = 'title'


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery


@login_required
def GalleryNewFormView(request):
    return render(request, 'galleries/gallery_new_form.html')


@login_required
def GalleryEditFormView(request, id):
    return render(request, 'galleries/gallery_edit_form.html', {id: id})
