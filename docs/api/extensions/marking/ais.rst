:mod:`stix.extensions.marking.ais` Module
====================================================

.. automodule:: stix.extensions.marking.ais

Classes
-------

.. autoclass:: AISMarkingStructure
	:show-inheritance:
	:members:

Functions
---------

.. autofunction:: add_ais_marking


Examples
--------

Applying AIS Markings
---------------------

The STIX specification allows data markings to be applied to any combination of
attributes and elements that can be described by XPath. That being said, the
Automated Indicator Sharing (AIS) capability requires those markings controlled
structure to select all nodes and attributes ``//node() | //@*``. All required
fields to create a valid AIS Markings are provided through the ``add_ais_marking``
function.

.. code-block:: python

    # python-stix imports
    import stix
    from stix.core import STIXPackage
    from stix.extensions.marking.ais import (add_ais_marking,
                                             COMMUNICATIONS_SECTOR,
                                             INFORMATION_TECHNOLOGY_SECTOR)
    from stix.indicator import Indicator

    # Create new STIX Package
    stix_package = STIXPackage()

    # Create new Indicator
    indicator = Indicator(title='My Indicator Example',
                          description='Example using AIS')

    # Add indicator to our STIX Package
    stix_package.add_indicator(indicator)

    # Create AIS Marking with CIQ Identity and attach it to STIX Header.
    add_ais_marking(stix_package, False, 'EVERYONE', 'GREEN',
        country_name_code='US',
        country_name_code_type='ISO 3166-1 alpha-2',
        admin_area_name_code='US-VA',
        admin_area_name_code_type='ISO 3166-2',
        organisation_name='Example Corporation',
        industry_type=[INFORMATION_TECHNOLOGY_SECTOR, COMMUNICATIONS_SECTOR]
    )

    # Print the XML.
    print stix_package.to_xml()

    # Print the JSON.
    print stix_package.to_json()

This corresponds to the XML result:

.. code-block:: xml

    <stix:STIX_Package
        xmlns:AIS="http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2"
        xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
        xmlns:xpil="urn:oasis:names:tc:ciq:xpil:3"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xal="urn:oasis:names:tc:ciq:xal:3"
        xmlns:xnl="urn:oasis:names:tc:ciq:xnl:3"
        xmlns:stix="http://stix.mitre.org/stix-1"
        xmlns:indicator="http://stix.mitre.org/Indicator-2"
        xmlns:marking="http://data-marking.mitre.org/Marking-1"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:stixCommon="http://stix.mitre.org/common-1"
        xmlns:example="http://example.com"
        xmlns:stix-ciqidentity="http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1"
        xmlns:xlink="http://www.w3.org/1999/xlink"
         id="example:Package-73ac199c-9dd8-4d8d-a37e-8ac40fc65ccf" version="1.2">
        <stix:STIX_Header>
            <stix:Handling>
                <marking:Marking>
                    <marking:Controlled_Structure>//node() | //@*</marking:Controlled_Structure>
                    <marking:Marking_Structure xsi:type='AIS:AISMarkingStructure'>
                        <AIS:Not_Proprietary CISA_Proprietary="false">
                            <AIS:AISConsent consent="EVERYONE"/>
                            <AIS:TLPMarking color="GREEN"/>
                        </AIS:Not_Proprietary>
                    </marking:Marking_Structure>
                    <marking:Information_Source>
                        <stixCommon:Identity xsi:type="stix-ciqidentity:CIQIdentity3.0InstanceType">
                            <stix-ciqidentity:Specification xmlns:stix-ciqidentity="http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1">\
                                <xpil:PartyName xmlns:xpil="urn:oasis:names:tc:ciq:xpil:3">
                                    <xnl:OrganisationName xmlns:xnl="urn:oasis:names:tc:ciq:xnl:3">
                                        <xnl:NameElement>Example Corporation</xnl:NameElement>
                                    </xnl:OrganisationName>
                                </xpil:PartyName>
                                <xpil:Addresses xmlns:xpil="urn:oasis:names:tc:ciq:xpil:3">
                                    <xpil:Address>
                                        <xal:Country xmlns:xal="urn:oasis:names:tc:ciq:xal:3">
                                            <xal:NameElement xal:NameCode="US" xal:NameCodeType="ISO 3166-1 alpha-2"/>
                                        </xal:Country>
                                        <xal:AdministrativeArea xmlns:xal="urn:oasis:names:tc:ciq:xal:3">
                                            <xal:NameElement xal:NameCode="US-VA" xal:NameCodeType="ISO 3166-2"/>
                                        </xal:AdministrativeArea>
                                    </xpil:Address>
                                </xpil:Addresses>
                                <xpil:OrganisationInfo xmlns:xpil="urn:oasis:names:tc:ciq:xpil:3" xpil:IndustryType="Information Technology Sector|Communications Sector"/>
                            </stix-ciqidentity:Specification>
                        </stixCommon:Identity>
                    </marking:Information_Source>
                </marking:Marking>
            </stix:Handling>
        </stix:STIX_Header>
        <stix:Indicators>
            <stix:Indicator id="example:indicator-eab71e49-e982-4874-a057-e75e51a76009" timestamp="2017-09-21T13:28:47.467000+00:00" xsi:type='indicator:IndicatorType'>
                <indicator:Title>My Indicator Example</indicator:Title>
                <indicator:Description>Example using AIS</indicator:Description>
            </stix:Indicator>
        </stix:Indicators>
    </stix:STIX_Package>

The following corresponds to the JSON result:

.. code-block:: json

    {
        "stix_header": {
            "handling": [
                {
                    "controlled_structure": "//node() | //@*",
                    "information_source": {
                        "identity": {
                            "xsi:type": "stix-ciqidentity:CIQIdentity3.0InstanceType",
                            "specification": {
                                "organisation_info": {
                                    "industry_type": "Information Technology Sector|Communications Sector"
                                },
                                "party_name": {
                                    "organisation_names": [
                                        {
                                            "name_elements": [
                                                {
                                                    "value": "Example Corporation"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                "addresses": [
                                    {
                                        "country": {
                                            "name_elements": [
                                                {
                                                    "name_code_type": "ISO 3166-1 alpha-2",
                                                    "name_code": "US"
                                                }
                                            ]
                                        },
                                        "administrative_area": {
                                            "name_elements": [
                                                {
                                                    "name_code_type": "ISO 3166-2",
                                                    "name_code": "US-VA"
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    "marking_structures": [
                        {
                            "xsi:type": "AIS:AISMarkingStructure",
                            "not_proprietary": {
                                "tlp_marking": {
                                    "color": "GREEN"
                                },
                                "ais_consent": {
                                    "consent": "EVERYONE"
                                },
                                "cisa_proprietary": "false"
                            }
                        }
                    ]
                }
            ]
        },
        "version": "1.2",
        "indicators": [
            {
                "description": "Example using AIS",
                "title": "My Indicator Example",
                "timestamp": "2017-10-02T14:26:57.510000+00:00",
                "id": "example:indicator-81466b8d-4efb-460f-ba13-b072420b9540"
            }
        ],
        "id": "example:Package-a8c8135d-18d8-4384-903f-71285a02346e"
    }

Parsing AIS Markings
--------------------

Using the same example used for Applying AIS Markings. This would be how a
consumer of AIS would parse the data.

.. code-block:: python

    # python-stix imports
    import stix
    from stix.core import STIXPackage
    import stix.extensions.marking.ais  # Register the AIS markings

    # Parse STIX Package
    stix_package = STIXPackage.from_xml("stix_input.xml")
    # stix_package = STIXPackage.from_json("stix_input.json")

    # Print all indicators
    for indicator in stix_package.indicators:
        print(indicator)

    # Extract markings from STIX Header
    markings = stix_package.stix_header.handling

    # Print all markings contained in the STIX Header
    for marking in markings:
        print(marking)
        print(marking.marking_structures)
        print("----------MARKING CONTENT----------")
        ais_struct = marking.marking_structures[0]
        print("OBJ: %s" % ais_struct)
        print("NotProprietary OBJ: %s" % ais_struct.not_proprietary)
        print("CISA_Proprietary: %s" % ais_struct.not_proprietary.cisa_proprietary)
        print("Consent: %s" % ais_struct.not_proprietary.ais_consent.consent)
        print("TLP color: %s" % ais_struct.not_proprietary.tlp_marking.color)

        print("----------INFORMATION SOURCE----------")
        identity = marking.information_source.identity.specification
        print("OBJ: %s" % identity)
        print("Organization Name: %s" % identity.party_name.organisation_names[0].name_elements[0].value)
        print("Country: %s" % identity.addresses[0].country.name_elements[0].name_code)
        print("Country code type: %s" % identity.addresses[0].country.name_elements[0].name_code_type)
        print("Administrative area: %s" % identity.addresses[0].administrative_area.name_elements[0].name_code)
        print("Administrative area code type: %s" % identity.addresses[0].administrative_area.name_elements[0].name_code_type)
        print("Industry Type: %s" % identity.organisation_info.industry_type)


    >>> <stix.indicator.indicator.Indicator object at 0x...>
    >>> <stix.data_marking.MarkingSpecification object at 0x...>
    >>> [<stix.extensions.marking.ais.AISMarkingStructure object at 0x...>, ...]
    >>> ----------MARKING CONTENT----------
    >>> OBJ: <stix.extensions.marking.ais.AISMarkingStructure object at 0x...>
    >>> NotProprietary OBJ: <stix.extensions.marking.ais.NotProprietary object at 0x...>
    >>> CISA_Proprietary: False
    >>> Consent: EVERYONE
    >>> TLP color: GREEN
    >>> ----------INFORMATION SOURCE----------
    >>> OBJ: <stix.extensions.identity.ciq_identity_3_0.STIXCIQIdentity3_0 object at 0x...>
    >>> Organization Name: Example Corporation
    >>> Country: US
    >>> Country code type: ISO 3166-1 alpha-2
    >>> Administrative area: US-VA
    >>> Administrative area code type: ISO 3166-2
    >>> Industry Type: Information Technology Sector|Communications Sector

Constants
---------

The following constants can be used for the ``industry_type`` keyword argument to
``add_ais_marking``:

.. autodata:: CHEMICAL_SECTOR
.. autodata:: COMMERCIAL_FACILITIES_SECTOR
.. autodata:: COMMUNICATIONS_SECTOR
.. autodata:: CRITICAL_MANUFACTURING_SECTOR
.. autodata:: DAMS_SECTOR
.. autodata:: DEFENSE_INDUSTRIAL_BASE_SECTOR
.. autodata:: EMERGENCY_SERVICES_SECTOR
.. autodata:: ENERGY_SECTOR
.. autodata:: FINANCIAL_SERVICES_SECTOR
.. autodata:: FOOD_AND_AGRICULTURE_SECTOR
.. autodata:: GOVERNMENT_FACILITIES_SECTOR
.. autodata:: HEALTH_CARE_AND_PUBLIC_HEALTH_SECTOR
.. autodata:: INFORMATION_TECHNOLOGY_SECTOR
.. autodata:: NUCLEAR_REACTORS_MATERIALS_AND_WASTE_SECTOR
.. autodata:: OTHER
.. autodata:: TRANSPORTATION_SYSTEMS_SECTOR
.. autodata:: WATER_AND_WASTEWATER_SYSTEMS_SECTOR
