import stix


class STIXHeader(stix.Entity):
    def __init__(self, package_intent=None, description=None, handling=None, information_source=None):
        self.package_intent = package_intent
        self.description = description
        self.handling = handling # not implemented
        self.information_source = information_source
        
    