# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import dateutil
from datetime import datetime

def parse_value(value):
    if not value:
        return None
    elif isinstance(value, datetime):
        return value
    return dateutil.parser.parse(value)

def serialize_value(value):
    if not value:
        return None
    return value.isoformat()
