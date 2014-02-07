# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.bindings.incident as incident_binding


class Incident(stix.Entity):
    _binding = incident_binding
    _namespace = "http://stix.mitre.org/Incident-1"
    
    def __init__(self, id_=None, title=None, description=None, time=None):
        self.id_ = id_ or stix.utils.create_id()
        self.description = description
        self.title = title
        self.time = time
        
        
        
        