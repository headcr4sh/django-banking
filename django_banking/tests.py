# -*- coding: utf-8 -*-

from django.utils import unittest

from django_banking import fields
from django_banking import models
from django_banking import parsers

mt940_test_data = '' \
':20:STARTUMS\r\n' \
':25:50050050/12345\r\n' \
':28C:0\r\n' \
':60F:C110216EUR3574,81\r\n' \
':61:110216C45,22NMSCNONREF\r\n' \
':86:051?00UEBERWEISUNG?10931?20RENR 2011 01 4444 01?3030060601\r\n' \
'?314587243?32MUSTERMANN MAX\r\n' \
':62F:C110216EUR3620,03\r\n' \
'-\r\n'
 


class MT940ParserTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def testParser(self):

	parser = parsers.MT940Parser()
        messages = parser.parse(mt940_test_data.split('\r\n'))
        
