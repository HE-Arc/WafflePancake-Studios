# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gallery

from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from .forms import GalleryNewForm, GalleryEditForm


@login_required
def GalleryListView(request):
    galleries = Gallery.objects.all()
    return render(request, 'galleries/gallery_list.html', {'galleries_list': galleries})


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery


@login_required
def GalleryNewFormView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GalleryNewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'galleries/gallery_list.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GalleryNewForm()
    return render(request, 'galleries/gallery_new_form.html', {'form': form})


@login_required
def GalleryEditFormView(request, pk):
    return render(request, 'galleries/gallery_edit_form.html', {id: pk})
