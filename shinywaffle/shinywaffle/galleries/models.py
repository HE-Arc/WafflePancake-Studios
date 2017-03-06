# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Gallery(models.Model):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    title = models.CharField(_('Title of Gallery'), blank=False, max_length=255)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:detail', kwargs={'username': self.title})
