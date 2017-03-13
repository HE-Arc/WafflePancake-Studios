# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gallery

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


@login_required
def GalleryListView(request):
    galleries = Gallery.objects.all()
    return render(request, 'galleries/gallery_list.html', {'galleries_list': galleries})


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery


@login_required
def GalleryNewFormView(request):
    return render(request, 'galleries/gallery_new_form.html')


@login_required
def GalleryEditFormView(request, id):
    return render(request, 'galleries/gallery_edit_form.html', {id: id})
