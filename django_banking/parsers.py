# -*- coding: utf-8 -*-

from django_banking.models import MT940

class MT940Parser(object):

    def parse(self, input):

        messages = []
        message = None

        for line in input:

            if line.startswith(':20:'):
                message = MT940()
                message.trn = line[4:]
                continue

            if line.startswith('-'):
                messages.append(message)
                message = None
                continue

