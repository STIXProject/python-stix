
import io
from pprint import pprint

from stix.core import STIXPackage
from stix.indicator import Indicator
import stix.bindings.stix_core_1_0 as stix_core_binding

def main():
    fn = 'ex_01.xml'
    stix_package_obj = stix_core_binding.parse(fn) # create a binding object from xml
    stix_package = STIXPackage.from_obj(stix_package_obj) # create python-stix object from binding
    stix_dict = stix_package.to_dict() # parse to dictionary
    pprint(stix_dict)
    
    stix_package_two = STIXPackage.from_dict(stix_dict) # create python-stix object from dictionary
    xml = stix_package_two.to_xml() # generate xml from python-stix object
    print(xml)
    
if __name__ == '__main__':
    main()