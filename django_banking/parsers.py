# -*- coding: utf-8 -*-

from django_banking.models import MT940

def parse_mt940(input):

    messages = []
    message = None

    for line in input:

        if line.startswith(':20:'):
            message = MT940()
            message.trn = line[4:]
            continue

        if line.startswith('-'):
            messages += message
            message = None
            continue

