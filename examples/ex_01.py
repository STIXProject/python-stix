
import io
from pprint import pprint

from stix.core import STIXPackage
from stix.indicator import Indicator
import stix.bindings.stix_core_1_0 as stix_core_binding

def main():
    fn = 'email_indicator_instance.xml'
    stix_package_obj = stix_core_binding.parse(fn) # create a binding object
    stix_package = STIXPackage.from_obj(stix_package_obj)
    stix_dict = stix_package.to_dict()
    pprint(stix_dict)
    #other way
    stix_package_two = STIXPackage.from_dict(stix_dict)
    xml = stix_package_two.to_xml()
    print xml
    
if __name__ == '__main__':
    main()