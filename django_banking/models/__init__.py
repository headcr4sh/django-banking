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




# ---- Abstract FieldTypes -----------------------------------------------------

class FT25(AbstractFT):

    bic = models.CharField(max_length=11)
    iban = models.CharField(max_length=23)

    cur = models.CharField(max_length=3)

    class Meta:
        verbose_name = _('account designation')
        verbose_name = _('account designations')


class FT28(AbstractFT):

    asn = models.CharField(max_length=5,
            verbose_name=_('account statement number'))
  
    pn = models.CharField(max_length=5,
            verbose_name=_('page number'))

    class Meta:
        verbose_name = _('account statement number')
        verbose_name = _('account statement numbers')
