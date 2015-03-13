# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import datetime

# external
import dateutil
import dateutil.parser
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


def parse_date(value):
    if not value:
        return None
    elif isinstance(value, datetime.date):
        return value
    elif isinstance(value, datetime.datetime):
        return value.date()
    else:
        return dateutil.parser.parse(value).date()


def serialize_date(value):
    if not value:
        return None
    elif isinstance(value, datetime.date):
        return value.isoformat()
    elif isinstance(value, datetime.datetime):
        return value.date().isoformat()
    else:
        return parse_date(value).isoformat()



def now():
    return datetime.datetime.now(tz=dateutil.tz.tzutc())