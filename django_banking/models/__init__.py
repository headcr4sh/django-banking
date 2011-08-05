# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractMT(models.Model):
    
    raw_data = models.TextField(blank=True, null=False,
            verbose_name=_('raw message data'))

    class Meta:
        abstract = True


class AbstractFT(models.Model):

    raw_data = models.TextField(blank=True, null=False,
            verbose_name=_('raw field data'))

    class Meta:
        abstract = True

