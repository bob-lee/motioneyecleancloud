import base64
import datetime
import functools
import hashlib
import logging
import os
import re
import socket
import sys
import time
import urllib
import urllib2
import urlparse

import settings


def urlopen(*args, **kwargs):
    if sys.version_info >= (2, 7, 9) and not settings.VALIDATE_CERTS:
        # ssl certs are not verified by default
        # in versions prior to 2.7.9

        import ssl

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        kwargs.setdefault('context', ctx)

    return urllib2.urlopen(*args, **kwargs)
