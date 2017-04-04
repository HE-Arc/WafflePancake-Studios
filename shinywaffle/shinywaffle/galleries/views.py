# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, CreateView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse

from .models import Gallery, Image

from .forms import GalleryForm, ImageForm


class GalleryListView(LoginRequiredMixin, ListView):
    model = Gallery
    template_name = "galleries/gallery_list.html"


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery


class GalleryEditFormView(FormView):
    '''
    model = Image
    fields = ['title', 'file']
    '''
    form_class = ImageForm
    template_name = 'galleries/image_form.html'

    def get_success_url(self):
        return '/galleries/{0}/'.format(self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        name = request.POST.get('image_name')
        files = request.FILES.getlist('images')
        print(name)
        if form.is_valid():
            for f in files:
                i = Image(title=name, gallery=self.gallery(), file=f)
                i.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def gallery(self):
        return Gallery.objects.get(pk=self.kwargs['pk'])

'''
    def form_valid(self, form):
        form.instance.gallery_id = int(self.kwargs['pk'])
        return super().form_valid(form)'''


class GalleryNewFormView(FormView):
    '''
    model = Gallery
    fields = ['title']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        '''

    form_class = GalleryForm
    template_name = 'galleries/gallery_form.html'
    success_url = '/galleries/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        name = request.POST.get('gallery_name')
        print(name)
        if form.is_valid():
            g = Gallery(title=name, author=self.request.user)
            g.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# AJAX METHODS


def delete_gallery(request):
    id = request.POST.get('id')
    Gallery.objects.get(pk=id).delete()
    data = {'id': id, 'message': 'Gallery deleted correctly'}
    return JsonResponse(data, status=200)


def delete_image(request):
    id = request.POST.get('id')
    Image.objects.get(pk=id).delete()
    data = {'id': id, 'message': 'Image deleted correctly'}
    return JsonResponse(data, status=200)
