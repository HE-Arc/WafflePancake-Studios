# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Gallery, Image

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from .forms import GalleryNewForm, GalleryEditForm


class GalleryListView(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = "galleries/gallery_list.html"


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery


class GalleryEditFormView(CreateView):
    model = Image
    fields = ['title', 'file']

    def gallery(self):
        return Gallery.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.gallery_id = int(self.kwargs['pk'])
        return super().form_valid(form)


#  Convert form methods to classes
@login_required
def gallery_new_form_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GalleryNewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            gallery = Gallery(
                title=request.POST.get('gallery_name'),
                author_id=request.user.id)
            gallery.save()
            # redirect to a new URL:
            return redirect('galleries:index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GalleryNewForm()
    return render(request, 'galleries/gallery_new_form.html', {'form': form})

'''
@login_required
def gallery_edit_form_view(request, pk):
    # if this is a POST request we need to process the form data

    form = GalleryEditForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GalleryEditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            files = request.FILES.getlist('images')
            for f in files:
                image = Image(title=request.POST.get('image_name'), gallery=pk, file=f)
                image.save()
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return redirect('galleries:detail', {'id': pk})
        else:
            messages.add_message(request, messages.ERROR, form.errors)

    return render(request, 'galleries/image_form.html', {'id': pk, 'form': form})

'''
