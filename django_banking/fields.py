# -*- coding: utf-8 -*-

from django.core.validator import RegexValidator
from django.db.models import CharField


class FT20(models.CharField):
    def __init__(self, **kwargs):
        super(CharField, self).__init__(max_length=16, null=False blank=True,
                validators=[RegexValidator(r'^(.{0,16})$')],
                verbose_name='message reference number')




class FT21(models.CharField):

    def __init__(self, **kwargs):
        super(CharField, self).__init__(max_length=16, null=True, blank=True,
                validators=[RegexValidator(r'^(.{0,16})$')],
                verbose_name='related reference number')



class FT25(models.CharField):

    # TODO We need a 2nd validator for BIC/IBAN or Kto/BLZ inpput validation

    def __init__(self, **kwargs):
        super(CharField, self).__init__(max_length=35, null=False, blank=True,
                validators=[RegexValidator(r'^(.{0,35})$')],
                verbose_name='account designation')



class FT28C(models.CharField):

    def __init__(self, **kwargs):
        super(CharField, self).__init__(max_length=35, null=False, blank=True,
                validators=[RegexValidator(r'(\d{5})/(\d{3})')],
                verbose_name='')

