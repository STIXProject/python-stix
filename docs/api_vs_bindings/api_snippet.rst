.. code-block:: python

	from datetime import datetime
	from stix.core import STIXPackage, STIXHeader
	from stix.common import InformationSource
	from cybox.common import Time

	# Create the STIX Package and STIX Header objects
	stix_package = STIXPackage()
	stix_header = STIXHeader()

	# Set the description
	stix_header.description = 'APIs vs. Bindings Wiki Example'

	# Set the produced time to now
	stix_header.information_source = InformationSource()
	stix_header.information_source.time = Time()
	stix_header.information_source.time.produced_time = datetime.now()

	# Build document
	stix_package.stix_header = stix_header

	# Print the document to stdout
	print(stix_package.to_xml())