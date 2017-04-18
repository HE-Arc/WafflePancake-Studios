# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.views.generic import DetailView, CreateView, ListView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Gallery
=======

from .models import Gallery, Image
>>>>>>> origin/friend-users-network

from .forms import GalleryForm, ImageForm

from django.shortcuts import render, get_object_or_404, redirect

from .forms import GalleryNewForm, GalleryEditForm


User = get_user_model()

@login_required
def gallery_list_view(request):
    galleries = Gallery.objects.all()
    return render(request, 'galleries/gallery_list.html', {'galleries_list': galleries})


class GalleryDetailView(LoginRequiredMixin, DetailView):
    model = Gallery

@login_required
def gallery_userlist_view(request, username):
    users = User.objects.get(username=username)
    galleries = Gallery.objects.filter(author_id=users.id)
    return render(request, 'galleries/gallery_list.html', {'galleries_list': galleries})

class GalleryEditFormView(FormView):
    form_class = ImageForm
    template_name = 'galleries/image_form.html'

    def get_success_url(self):
        return '/galleries/{0}/'.format(self.kwargs['pk'])

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        name = request.POST.get('image_name')
        files = request.FILES.getlist('images')
        if form.is_valid():
            for f in files:
                i = Image(title=name, gallery=self.gallery(), file=f)
                i.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def gallery(self):
        return Gallery.objects.get(pk=self.kwargs['pk'])


class GalleryNewFormView(FormView):
    form_class = GalleryForm
    template_name = 'galleries/gallery_form.html'
    success_url = '/galleries/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        name = request.POST.get('gallery_name')
        if form.is_valid():
            g = Gallery(title=name, author=self.request.user)
            g.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
