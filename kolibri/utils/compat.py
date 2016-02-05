# -*- coding: utf-8 -*-
"""
Compatibility helpers
"""
from __future__ import print_function, unicode_literals, absolute_import

__all__ = ['input']

# In Python 2 there is raw_input() that takes a string from stdin and input()
# that takes a string from stdin and evaluates it. That last function is not
# very useful and has been removed in Python 3, while raw_input() has been
# renamed to input().
try:
    input = raw_input  # @ReservedAssignment
except NameError:
    pass
