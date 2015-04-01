# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

__version__ = "1.1.1.5-dev"


def supported_stix_version():
    lib_version = __version__
    return lib_version[:-2]


from .base import Entity, EntityList, TypedList, BaseCoreComponent  # noqa

# Make sure common gets imported before anything else.
from . import common  # noqa
