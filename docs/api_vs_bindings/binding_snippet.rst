.. code-block:: python

	import sys
	from datetime import datetime

	import stix.bindings.stix_core as stix_core_binding
	import stix.bindings.stix_common as stix_common_binding
	import cybox.bindings.cybox_common as cybox_common_binding

	# Create the STIX Package and STIX Header objects
	stix_package = stix_core_binding.STIXType()
	stix_header = stix_core_binding.STIXHeaderType()

	# Set the description
	stix_header_description = stix_common_binding.StructuredTextType()
	stix_header_description.set_valueOf_('APIs vs. Bindings Wiki Example')

	# Set the produced time to now
	stix_header_time = cybox_common_binding.TimeType()
	stix_header_time.set_Produced_Time(datetime.now())

	# Bind the time to the STIX Header's Information Source element
	stix_header_info_source = stix_common_binding.InformationSourceType()
	stix_header_info_source.set_Time(stix_header_time)

	# Build the document
	stix_header.set_Description(stix_header_description)
	stix_header.set_Information_Source(stix_header_info_source)
	stix_package.set_STIX_Header(stix_header)

	# Print the document to stdout
	stix_package.export(sys.stdout, 0, stix_core_binding.DEFAULT_XML_NS_MAP)