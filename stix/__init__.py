# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# Make sure base gets imported before common.
from .base import (  # noqa
    Entity, EntityList, TypedCollection, TypedList, TypedSequence,
    BaseCoreComponent
)

from . import common  # noqa

from .version import __version__  # noqa

def supported_stix_version():
    return '.'.join(__version__.split('.')[:3])

