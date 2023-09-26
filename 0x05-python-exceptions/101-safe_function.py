#!/usr/bin/python3


from __future__ import print_function
import sys


def safe_function(func, *args):
    try:
        rest = func(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return rest
