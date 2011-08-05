# -*- coding: utf-8 -*-

from django_banking.models.mt940 import MT940

class MT940Parser(object):

    def parse(self, input):

        messages = []
        message = None

        for line in input:

            if line.startswith(':20:'):
                message = MT940()
                message.trn = line[4:]
                continue

            if line.startswith(':21'):
                message.ref = line[4:]
                continue

            if line.startswith(':25:'):
                message.acc = line[4:]
                continue

            if line.startswith(':28C:'):
                message.seq = line[5:]
                continue

            if line.startswith(':60F:'):
                message.bal_open = line[5:]
                continue

# TODO :61: and :86:

            if line.startswith('62F:'):
                message.bal_close = line[5:]
                continue

            if line.startswith(':64:'):
                message.bal_close_avail = line[4:]
                continue

            if line.startswith('-'):
                if message:
                    messages.append(message)
                    message = None
                continue

