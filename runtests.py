#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
 
from django.core.management import execute_manager
from django.core.management import setup_environ

def main():

    # Import test settings
    from django_banking import test_settings as settings 
    setup_environ(settings)

    # Use Django's Execute manager to run the tests
    sys.argv = [sys.argv[0],'test', 'django_banking']
    execute_manager(settings)

if __name__ == '__main__':
    main()
