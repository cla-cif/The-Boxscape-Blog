from django.core.exceptions import ValidationError
import re


def validate_url(value):
    reg = re.compile('(?:([^:/?#]+):)?(?://([^/?#]*))?([^?#]*\.(?:jpg|gif|png|webp|jpeg))(?:\?([^#]*))?(?:#(.*))?') # noqa
    if not reg.match(value):
        raise ValidationError('Unsupported file extension.')
