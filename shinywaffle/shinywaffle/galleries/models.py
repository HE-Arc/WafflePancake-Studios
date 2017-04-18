# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


@python_2_unicode_compatible
class Gallery(models.Model):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    title = models.CharField(
        _('Title of Gallery'), blank=False, max_length=255)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('galleries:index')  # , kwargs={'pk': self.title})


@python_2_unicode_compatible
class Image(models.Model):
    title = models.CharField(_('Title of Image'), blank=False, max_length=255)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    file = models.ImageField(
        upload_to='pictures/', default='pictures/None/no-img.jpg')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('galleries:detail', kwargs={'pk': self.gallery.id})
