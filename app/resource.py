#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from random import choice
from string import ascii_uppercase as uppercase, digits


def get_unique_str(amount):
    """
    Return a unique string
    
    :param amount: (int)
    :return string:
    """
    try:
        unique_string = (''.join(choice(uppercase + digits)
                                 for x in xrange(amount)))
    except NameError:
        unique_string = (''.join(choice(uppercase + digits)
                                 for x in range(amount)))
    return unique_string
