# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import datetime

# external
import dateutil
import dateutil.tz


def parse_value(value):
    if not value:
        return None
    elif isinstance(value, datetime.datetime):
        return value
    return dateutil.parser.parse(value)


def serialize_value(value):
    if not value:
        return None
    return value.isoformat()


def now():
    return datetime.datetime.now(tz=dateutil.tz.tzutc())