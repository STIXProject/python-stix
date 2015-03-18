# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import datetime

# external
import dateutil
import dateutil.parser
import dateutil.tz


def parse_value(value):
    """Attempts to parse `value` into an instance of ``datetime.datetime``. If
    `value` is ``None``, this function will return ``None``.

    Args:
        value: A timestamp. This can be a string or datetime.datetime value.

    """
    if not value:
        return None
    elif isinstance(value, datetime.datetime):
        return value
    return dateutil.parser.parse(value)


def serialize_value(value):
    """Attempts to convert `value` into an ISO8601-compliant timestamp string.
    If `value` is ``None``, ``None`` will be returned.

    Args:
        value: A datetime.datetime value.

    Returns:
        An ISO8601 formatted timestamp string.

    """
    if not value:
        return None
    return value.isoformat()


def parse_date(value):
    """Attempts to parse `value` into an instance of ``datetime.date``. If
    `value` is ``None``, this function will return ``None``.

    Args:
        value: A timestamp. This can be a string, datetime.date, or
            datetime.datetime value.

    """
    if not value:
        return None
    elif isinstance(value, datetime.date):
        return value
    elif isinstance(value, datetime.datetime):
        return value.date()
    else:
        return dateutil.parser.parse(value).date()


def serialize_date(value):
    """Attempts to convert `value` into an ``xs:date`` string. If `value` is
    ``None``, ``None`` will be returned.

    Args:
        value: A date value. This can be a string, datetime.date, or
            datetime.datetime object.

    Returns:
        An ``xs:date`` formatted timestamp string.

    """
    if not value:
        return None
    elif isinstance(value, datetime.date):
        return value.isoformat()
    elif isinstance(value, datetime.datetime):
        return value.date().isoformat()
    else:
        return parse_date(value).isoformat()


def now():
    """Returns the current UTC datetime.datetime."""
    return datetime.datetime.now(tz=dateutil.tz.tzutc())
