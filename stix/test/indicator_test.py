'''
Created on Feb 20, 2013

@author: BWORRELL
'''

import stix.api.observable as stix_observable_api
import stix.api.indicator as stix_indicator_api


def get_email():
    email_dict = {
        'from': 'jsmith@yahoo.com',
        'to': 'janedoe@gmail.com',
        'isodate': 'Tue, 5 Feb 2013 10:56:02 -0500',
        'x-originating-ip': '255.255.255.255',
        'reply_to': 'foo@example.com',
        'subject': 'test'
    }
    
    return email_dict


def get_source():
    source_dict = {
        'person' : 'John McHacksalot',
        'organization' : 'Hackme Inc.'
    }



def main():
    my_indicators = []
    email_dict = get_email()
    source_dict = get_source()
    
    indicator = stix_indicator_api.Indicator(source=source_dict)
    indicator.add_observable(stix_observable_api.TYPE_EMAIL, email_dict)
    stix_package = stix_api.Package(indicators=my_indicators)
    
    # OUTPUT
    stix_package_obj = stix_package.to_obj()
    #or
    stix_package_xml = stix_package.to_xml() # BytesIO representation
    



if __name__ == '__main__':
    main()