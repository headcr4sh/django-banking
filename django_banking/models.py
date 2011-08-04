# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_banking.fields import FT20
from django_banking.fields import FT21
from django_banking.fields import FT25
from django_banking.fields import FT28C


class MT940(model.Model):

    """MT 940 Customer Statement Message

    Scope:
      This message is used to transmit detailed information about all
      entries booked to an account, serviced by a financial institution.

    Usage:
      In the bank-to-bank part of the payment chain, the MT 940 is normally
      sent by an account servicing institution (reporting institution) to a
      financial institution (forwarding institution) which has been authorised
      by the account owner to receive it. 
      In the bank-to-corporate environment, this ‘relay’ scenario is also
      supported by the MT 940: the forwarding institution forwards the MT 940
      to the corporate (the account owner, or the party authorised by the
      account owner to receive the information). 
      In a bank-to-corporate environment, however, the MT 940 is also to be
      used instead of the MT 950 directly between the account servicing
      financial institution and the corporate (the account owner, or the
      party authorised by the account owner to receive the information).""" 


    trn = FT20()

    class Meta:
        verbose_name = _('customer statement message')
        verbose_name_plurals = _('customer statement messages')
