# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .models import Gallery, Image

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from .forms import GalleryNewForm, GalleryEditForm


class GalleryListView(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = "galleries/gallery_list.html"


def delete_gallery(request):
    id = request.POST.get('id')
    Gallery.objects.get(pk=id).delete()
    return HttpResponse(status=200)


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery

    def deleteImage(self):
        pass


class GalleryEditFormView(CreateView):
    model = Image
    fields = ['title', 'file']
    # form_class = GalleryEditForm

    def gallery(self):
        return Gallery.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.gallery_id = int(self.kwargs['pk'])
        return super().form_valid(form)


class GalleryNewFormView(CreateView):
    model = Gallery
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
