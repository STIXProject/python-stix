# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

__version__ = "1.1.1.5.dev0"


def supported_stix_version():
    return '.'.join(__version__.split('.')[:3])


from .base import Entity, EntityList, TypedList, BaseCoreComponent  # noqa

# Make sure common gets imported before anything else.
from . import common  # noqa
