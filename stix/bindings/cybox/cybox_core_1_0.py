#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Thu Nov 01 09:53:09 2012 by generateDS.py version 2.7c.
#

import sys
import getopt
import re as re_

import cybox_common_types_1_0

#Objects path - set to point to the CybOX Objects Bindings folder
objects_path = ''
#Dictionary for storing Defined Objects, their main types, namespaces, and schemalocations
defined_objects = {'AccountObjectType' : {'binding_name' : 'account_object_1_2', 'namespace_prefix' : 'AccountObj', 'namespace' : 'http://cybox.mitre.org/objects#AccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Account/Account_Object_1.2.xsd'},
                   'AddressObjectType' : {'binding_name' : 'address_object_1_2', 'namespace_prefix' : 'AddressObj', 'namespace' : 'http://cybox.mitre.org/objects#AddressObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Address/Address_Object_1.2.xsd'},
                   'APIObjectType' : {'binding_name' : 'api_object_1_1', 'namespace_prefix' : 'APIObj', 'namespace' : 'http://cybox.mitre.org/objects#APIObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/API/API_Object_1.1.xsd'},
                   'ArtifactType' : {'binding_name' : 'artifact_object_1_0', 'namespace_prefix' : 'ArtifactObj', 'namespace' : 'http://cybox.mitre.org/objects#ArtifactObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Artifact/Artifact_Object_1.0.xsd'},
                   'CodeObjectType' : {'binding_name' : 'code_object_1_1', 'namespace_prefix' : 'CodeObj', 'namespace' : 'http://cybox.mitre.org/objects#CodeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Code/Code_Object_1.1.xsd'},
                   'DeviceObjectType' : {'binding_name' : 'device_object_1_1', 'namespace_prefix' : 'DeviceObj', 'namespace' : 'http://cybox.mitre.org/objects#DeviceObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Device/Device_Object_1.1.xsd'},
                   'DiskObjectType' : {'binding_name' : 'disk_object_1_3', 'namespace_prefix' : 'DiskObj', 'namespace' : 'http://cybox.mitre.org/objects#DiskObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Disk/Disk_Object_1.3.xsd', 'dependencies' : 'DiskPartitionObjectType'},
                   'DiskPartitionObjectType' : {'binding_name' : 'disk_partition_object_1_3', 'namespace_prefix' : 'DiskPartitionObj', 'namespace' : 'http://cybox.mitre.org/objects#DiskPartitionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Disk_Partition/Disk_Partition_Object_1.3.xsd'},
                   'DNSCacheEntryType' : {'binding_name' : 'dns_cache_object_1_3', 'namespace_prefix' : 'DNSCacheObj', 'namespace' : 'http://cybox.mitre.org/objects#DNSCacheObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/DNS_Cache/DNS_Cache_Object_1.3.xsd', 'dependencies' : 'DNSRecordObjectType,AddressObjectType,URIObjectType'},
                   'DNSQueryObjectType' : {'binding_name' : 'dns_query_object_1_0', 'namespace_prefix' : 'DNSQueryObj', 'namespace' : 'http://cybox.mitre.org/objects#DNSQueryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/DNS_Query/DNS_Query_Object_1.0.xsd', 'dependencies' : 'DNSRecordObjectType,URIObjectType,AddressObjectType'},
                   'DNSRecordObjectType' : {'binding_name' : 'dns_record_object_1_1', 'namespace_prefix' : 'DNSRecordObj', 'namespace' : 'http://cybox.mitre.org/objects#DNSRecordObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/DNS_Record/DNS_Record_Object_1.1.xsd', 'dependencies' : 'URIObjectType,AddressObjectType'},
                   'EmailMessageObjectType' : {'binding_name' : 'email_message_object_1_2', 'namespace_prefix' : 'EmailMessageObj', 'namespace' : 'http://cybox.mitre.org/objects#EmailMessageObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Email_Message/Email_Message_Object_1.2.xsd', 'dependencies' : 'FileObjectType,AddressObjectType,URIObjectType'},
                   'FileObjectType' : {'binding_name' : 'file_object_1_3', 'namespace_prefix' : 'FileObj', 'namespace' : 'http://cybox.mitre.org/objects#FileObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/File/File_Object_1.3.xsd'},
                   'GUIDialogboxObjectType' : {'binding_name' : 'gui_dialogbox_object_1_2', 'namespace_prefix' : 'GUIDialogboxObj', 'namespace' : 'http://cybox.mitre.org/objects#GUIDialogboxObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/GUI_Dialogbox/GUI_Dialogbox_Object_1.2.xsd', 'dependencies' : 'GUIObjectType'},
                   'GUIObjectType' : {'binding_name' : 'gui_object_1_2', 'namespace_prefix' : 'GUIObj', 'namespace' : 'http://cybox.mitre.org/objects#GUIObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/GUI/GUI_Object_1.2.xsd'},
                   'GUIWindowObjectType' : {'binding_name' : 'gui_window_object_1_2', 'namespace_prefix' : 'GUIWindowOb', 'namespace' : 'http://cybox.mitre.org/objects#GUIWindowObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/GUI_Window/GUI_Window_Object_1.2.xsd', 'dependencies' : 'GUIObjectType'},
                   'HTTPSessionObjectType' : {'binding_name' : 'http_session_object_1_0', 'namespace_prefix' : 'HTTPSessionObj', 'namespace' : 'http://cybox.mitre.org/objects#HTTPSessionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/HTTP_Session/HTTP_Session_Object_1.0.xsd', 'dependencies' : 'AddressObjectType,PortObjectType,URIObjectType'},
                   'LibraryObjectType' : {'binding_name' : 'library_object_1_3', 'namespace_prefix' : 'LibraryObj', 'namespace' : 'http://cybox.mitre.org/objects#LibraryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Library/Library_Object_1.3.xsd'},
                   'LinuxPackageObjectType' : {'binding_name' : 'linux_package_object_1_3', 'namespace_prefix' : 'LinuxPackageObj', 'namespace' : 'http://cybox.mitre.org/objects#LinuxPackageObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Linux_Package/Linux_Package_Object_1.3.xsd'},
                   'MemoryObjectType' : {'binding_name' : 'memory_object_1_2', 'namespace_prefix' : 'MemoryObj', 'namespace' : 'http://cybox.mitre.org/objects#MemoryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Memory/Memory_Object_1.2.xsd'},
                   'MutexObjectType' : {'binding_name' : 'mutex_object_1_3', 'namespace_prefix' : 'MutexObj', 'namespace' : 'http://cybox.mitre.org/objects#MutexObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Mutex/Mutex_Object_1.3.xsd'},
                   'NetworkConnectionType' : {'binding_name' : 'network_connection_object_1_0', 'namespace_prefix' : 'NetworkConnectionObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkConnectionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Connection/Network_Connection_Object_1.0.xsd', 'dependencies' : 'AddressObjectType,PortObjectType,HTTPSessionObjectType,DNSQueryObjectType,DNSRecordObjectType,URIObjectType'},
                   'NetworkFlowObjectType' : {'binding_name' : 'network_flow_object_1_1', 'namespace_prefix' : 'NetFlowObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkFlowObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Flow/Network_Flow_Object_1.1.xsd', 'dependencies' : 'NetworkPacketType,AddressObjectType,PortObjectType'},
                   'NetworkPacketType' : {'binding_name' : 'network_packet_object_1_1', 'namespace_prefix' : 'PacketObj', 'namespace' : 'http://cybox.mitre.org/objects#PacketObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Packet/Network_Packet_Object_1.1.xsd', 'dependencies' : 'AddressObjectType,PortObjectType'},
                   'NetworkRouteEntryObjectType' : {'binding_name' : 'network_route_entry_object_1_1', 'namespace_prefix' : 'NetworkRouteEntryObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkRouteEntryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Route_Entry/Network_Route_Entry_Object_1.1.xsd', 'dependencies' : 'AddressObjectType'},
                   'NetRouteObjectType' : {'binding_name' : 'network_route_object_1_2', 'namespace_prefix' : 'NetworkRouteObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkRouteObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Route/Network_Route_Object_1.2.xsd', 'dependencies' : 'NetworkRouteEntryObjectType,AddressObjectType'},
                   'NetworkSubnetObjectType' : {'binding_name' : 'network_subnet_object_1_1', 'namespace_prefix' : 'NetworkSubnetObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkSubnetObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Subnet/Network_Subnet_Object_1.1.xsd', 'dependencies' : 'NetworkRouteEntryObjectType,AddressObjectType'},
                   'PipeObjectType' : {'binding_name' : 'pipe_object_1_3', 'namespace_prefix' : 'PipeObj', 'namespace' : 'http://cybox.mitre.org/objects#PipeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Pipe/Pipe_Object_1.3.xsd'},
                   'PortObjectType' : {'binding_name' : 'port_object_1_3', 'namespace_prefix' : 'PortObj', 'namespace' : 'http://cybox.mitre.org/objects#PortObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Port/Port_Object_1.3.xsd'},
                   'ProcessObjectType' : {'binding_name' : 'process_object_1_3', 'namespace_prefix' : 'ProcessObj', 'namespace' : 'http://cybox.mitre.org/objects#ProcessObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Process/Process_Object_1.3.xsd', 'dependencies' : 'AddressObjectType,PortObjectType'},
                   'SemaphoreObjectType' : {'binding_name' : 'semaphore_object_1_3', 'namespace_prefix' : 'SemaphoreObj', 'namespace' : 'http://cybox.mitre.org/objects#SemaphoreObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Semaphore/Semaphore_Object_1.3.xsd'},
                   'SocketObjectType' : {'binding_name' : 'socket_object_1_4', 'namespace_prefix' : 'SocketObj', 'namespace' : 'http://cybox.mitre.org/objects#SocketObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Socket/Socket_Object_1.4.xsd', 'dependencies' : 'AddressObjectType,PortObjectType'},
                   'SystemObjectType' : {'binding_name' : 'system_object_1_3', 'namespace_prefix' : 'SystemObj', 'namespace' : 'http://cybox.mitre.org/objects#SystemObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/System/System_Object_1.3.xsd', 'dependencies' : 'AddressObjectType'},
                   'UnixFileObjectType' : {'binding_name' : 'unix_file_object_1_3', 'namespace_prefix' : 'UnixFileObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixFileObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_File/Unix_File_Object_1.3.xsd', 'dependencies' : 'FileObjectType'},
                   'UnixNetworkRouteEntryObjectType' : {'binding_name' : 'unix_network_route_entry_object_1_1', 'namespace_prefix' : 'UnixNetworkRouteEntryObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_Network_Route_Entry/Unix_Network_Route_Entry_Object_1.1.xsd', 'dependencies' : 'NetworkRouteEntryObjectType,AddressObjectType'},
                   'UnixPipeObjectType' : {'binding_name' : 'unix_pipe_object_1_2', 'namespace_prefix' : 'UnixPipeObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixPipeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_Pipe/Unix_Pipe_Object_1.2.xsd', 'dependencies' : 'PipeObjectType'},
                   'UnixProcessObjectType' : {'binding_name' : 'unix_process_object_1_3', 'namespace_prefix' : 'UnixProcessObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixProcessObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_Process/Unix_Process_Object_1.3.xsd', 'dependencies' : 'ProcessObjectType,AddressObjectType,PortObjectType'},
                   'UnixUserAccountObjectType' : {'binding_name' : 'unix_user_account_object_1_2', 'namespace_prefix' : 'UnixUserAccountObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixUserAccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_User_Account/Unix_User_Account_Object_1.2.xsd', 'dependencies' : 'UserAccountObjectType,AccountObjectType'},
                   'UnixVolumeObjectType' : {'binding_name' : 'unix_volume_object_1_2', 'namespace_prefix' : 'UnixVolumeObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixVolumeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_Volume/Unix_Volume_Object_1.2.xsd', 'dependencies' : 'VolumeObjectType'},
                   'URIObjectType' : {'binding_name' : 'uri_object_1_2', 'namespace_prefix' : 'URIObj', 'namespace' : 'http://cybox.mitre.org/objects#URIObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/URI/URI_Object_1.2.xsd'},
                   'UserAccountObjectType' : {'binding_name' : 'user_account_object_1_2', 'namespace_prefix' : 'UserAccountObj', 'namespace' : 'http://cybox.mitre.org/objects#UserAccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/User_Account/User_Account_Object_1.2.xsd', 'dependencies' : 'AccountObjectType'},
                   'VolumeObjectType' : {'binding_name' : 'volume_object_1_3', 'namespace_prefix' : 'VolumeObj', 'namespace' : 'http://cybox.mitre.org/objects#VolumeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Volume/Volume_Object_1.3.xsd'},
                   'WhoisObjectType' : {'binding_name' : 'whois_object_1_0', 'namespace_prefix' : 'WhoisObj', 'namespace' : 'http://cybox.mitre.org/objects#WhoisObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Whois/Whois_Object_1.0.xsd', 'dependencies' : 'URIObjectType,AddressObjectType'},
                   'WinComputerAccountObjectType' : {'binding_name' : 'win_computer_account_object_1_3', 'namespace_prefix' : 'WinComputerAccountObj', 'namespace' : 'http://cybox.mitre.org/objects#WinComputerAccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Computer_Account/Win_Computer_Account_Object_1.3.xsd', 'dependencies' : 'AccountObjectType,PortObjectType'},
                   'WinCriticalSectionObjectType' : {'binding_name' : 'win_critical_section_object_1_2', 'namespace_prefix' : 'WinCriticalSectionObj', 'namespace' : 'http://cybox.mitre.org/objects#WinCriticalSectionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Critical_Section/Win_Critical_Section_Object_1.2.xsd'},
                   'WindowsDriverObjectType' : {'binding_name' : 'win_driver_object_1_2', 'namespace_prefix' : 'WinDriverObj', 'namespace' : 'http://cybox.mitre.org/objects#WinDriverObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Driver/Win_Driver_Object_1.2.xsd'},
                   'WindowsEventLogObjectType' : {'binding_name' : 'win_event_log_object_1_2', 'namespace_prefix' : 'WinEventLogObj', 'namespace' : 'http://cybox.mitre.org/objects#WinEventLogObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Event_Log/Win_Event_Log_Object_1.2.xsd'},
                   'WindowsEventObjectType' : {'binding_name' : 'win_event_object_1_3', 'namespace_prefix' : 'WinEventObj', 'namespace' : 'http://cybox.mitre.org/objects#WinEventObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Event/Win_Event_Object_1.3.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'WindowsExecutableFileObjectType' : {'binding_name' : 'win_executable_file_object_1_3', 'namespace_prefix' : 'WinExecutableFileObj', 'namespace' : 'http://cybox.mitre.org/objects#WinExecutableFileObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Executable_File/Win_Executable_File_Object_1.3.xsd', 'dependencies' : 'WindowsFileObjectType,FileObjectType,WinComputerAccountObjectType,AccountObjectType,PortObjectType'},
                   'WindowsFileObjectType' : {'binding_name' : 'win_file_object_1_3', 'namespace_prefix' : 'WinFileObj', 'namespace' : 'http://cybox.mitre.org/objects#WinFileObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_File/Win_File_Object_1.3.xsd', 'dependencies' : 'FileObjectType,WinComputerAccountObjectType,AccountObjectType,PortObjectType'},
                   'WindowsHandleObjectType' : {'binding_name' : 'win_handle_object_1_3', 'namespace_prefix' : 'WinHandleObj', 'namespace' : 'http://cybox.mitre.org/objects#WinHandleObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Handle/Win_Handle_Object_1.3.xsd'},
                   'WindowsKernelHookObjectType' : {'binding_name' : 'win_kernel_hook_object_1_3', 'namespace_prefix' : 'WinKernelHookObj', 'namespace' : 'http://cybox.mitre.org/objects#WinKernelHookObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel_Hook/Win_Kernel_Hook_Object_1.3.xsd'},
                   'WindowsKernelObjectType' : {'binding_name' : 'win_kernel_object_1_2', 'namespace_prefix' : 'WinKernelObj', 'namespace' : 'http://cybox.mitre.org/objects#WinKernelObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel/Win_Kernel_Object_1.2.xsd'},
                   'WindowsMailslotObjectType' : {'binding_name' : 'win_mailslot_object_1_2', 'namespace_prefix' : 'WinMailslotObj', 'namespace' : 'http://cybox.mitre.org/objects#WinMailslotObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Mailslot/Win_Mailslot_Object_1.2.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'WindowsMemoryPageRegionObjectType' : {'binding_name' : 'win_memory_page_region_object_1_0', 'namespace_prefix' : 'WinMemoryPageRegionObj', 'namespace' : 'http://cybox.mitre.org/objects#WinMemoryPageRegionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Memory_Page_Region/Win_Memory_Page_Region_Object_1.0.xsd', 'dependencies' : 'MemoryObjectType'},
                   'WindowsMutexObjectType' : {'binding_name' : 'win_mutex_object_1_2', 'namespace_prefix' : 'WinMutexObj', 'namespace' : 'http://cybox.mitre.org/objects#WinMutexObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Mutex/Win_Mutex_Object_1.2.xsd', 'dependencies' : 'WindowsHandleObjectType,MutexObjectType'},
                   'WindowsNetworkRouteEntryObjectType' : {'binding_name' : 'win_network_route_entry_object_1_3', 'namespace_prefix' : 'WinNetworkRouteEntryObj', 'namespace' : 'http://cybox.mitre.org/objects#WinNetworkRouteEntryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Route_Entry/Win_Network_Route_Entry_Object_1.3.xsd', 'dependencies' : 'NetworkRouteEntryObjectType,AddressObjectType'},
                   'WindowsNetworkShareObjectType' : {'binding_name' : 'win_network_share_object_1_3', 'namespace_prefix' : 'WinNetworkShareObj', 'namespace' : 'http://cybox.mitre.org/objects#WinNetworkShareObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Share/Win_Network_Share_Object_1.3.xsd'},
                   'WindowsPipeObjectType' : {'binding_name' : 'win_pipe_object_1_2', 'namespace_prefix' : 'WinPipeObj', 'namespace' : 'http://cybox.mitre.org/objects#WinPipeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Pipe/Win_Pipe_Object_1.2.xsd', 'dependencies' : 'PipeObjectType'},
                   'WindowsPrefetchObjectType' : {'binding_name' : 'win_prefetch_object_1_2', 'namespace_prefix' : 'WinPrefetchObj', 'namespace' : 'http://cybox.mitre.org/objects#WinPrefetchObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Prefetch/Win_Prefetch_Object_1.2.xsd', 'dependencies' : 'WindowsVolumeObjectType,VolumeObjectType,DeviceObjectType'},
                   'WindowsProcessObjectType' : {'binding_name' : 'win_process_object_1_3', 'namespace_prefix' : 'WinProcessObj', 'namespace' : 'http://cybox.mitre.org/objects#WinProcessObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Process/Win_Process_Object_1.3.xsd', 'dependencies' : 'ProcessObjectType,WindowsHandleObjectType,MemoryObjectType,AddressObjectType,PortObjectType'},
                   'WindowsRegistryKeyObjectType' : {'binding_name' : 'win_registry_key_object_1_3', 'namespace_prefix' : 'WinRegistryKeyObj', 'namespace' : 'http://cybox.mitre.org/objects#WinRegistryKeyObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Registry_Key/Win_Registry_Key_Object_1.3.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'WindowsSemaphoreObjectType' : {'binding_name' : 'win_semaphore_object_1_2', 'namespace_prefix' : 'WinSemaphoreObj', 'namespace' : 'http://cybox.mitre.org/objects#WinSemaphoreObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Semaphore/Win_Semaphore_Object_1.2.xsd', 'dependencies' : 'WindowsHandleObjectType,SemaphoreObjectType'},
                   'WindowsServiceObjectType' : {'binding_name' : 'win_service_object_1_3', 'namespace_prefix' : 'WinServiceObj', 'namespace' : 'http://cybox.mitre.org/objects#WinServiceObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Service/Win_Service_Object_1.3.xsd', 'dependencies' : 'WindowsProcessObjectType,WindowsHandleObjectType,MemoryObjectType,AddressObjectType,PortObjectType'},
                   'WindowsSystemObjectType' : {'binding_name' : 'win_system_object_1_2', 'namespace_prefix' : 'WinSystemObj', 'namespace' : 'http://cybox.mitre.org/objects#WinSystemObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_System/Win_System_Object_1.2.xsd', 'dependencies' : 'WindowsHandleObjectType,SystemObjectType,AddressObjectType'},
                   'WindowsSystemRestoreObjectType' : {'binding_name' : 'win_system_restore_object_1_2', 'namespace_prefix' : 'WinSystemRestoreObj', 'namespace' : 'http://cybox.mitre.org/objects#WinSystemRestoreObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_System_Restore/Win_System_Restore_Object_1.2.xsd'},
                   'WindowsTaskObjectType' : {'binding_name' : 'win_task_object_1_3', 'namespace_prefix' : 'WinTaskObj', 'namespace' : 'http://cybox.mitre.org/objects#WinTaskObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Task/Win_Task_Object_1.3.xsd', 'dependencies' : 'EmailMessageObjectType,FileObjectType,AddressObjectType,URIObjectType'},
                   'WindowsThreadObjectType' : {'binding_name' : 'win_thread_object_1_3', 'namespace_prefix' : 'WinThreadObj', 'namespace' : 'http://cybox.mitre.org/objects#WinThreadObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Thread/Win_Thread_Object_1.3.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'WindowsUserAccountObjectType' : {'binding_name' : 'win_user_account_object_1_3', 'namespace_prefix' : 'WinUserAccountObj', 'namespace' : 'http://cybox.mitre.org/objects#WinUserAccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_User_Account/Win_User_Account_Object_1.3.xsd', 'dependencies' : 'UserAccountObjectType,AccountObjectType'},
                   'WindowsVolumeObjectType' : {'binding_name' : 'win_volume_object_1_3', 'namespace_prefix' : 'WinVolumeObj', 'namespace' : 'http://cybox.mitre.org/objects#WinVolumeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Volume/Win_Volume_Object_1.3.xsd', 'dependencies' : 'VolumeObjectType'},
                   'WindowsWaitableTimerObjectType' : {'binding_name' : 'win_waitable_timer_object_1_3', 'namespace_prefix' : 'WinWaitableTimerObj', 'namespace' : 'http://cybox.mitre.org/objects#WinWaitableTimerObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Waitable_Timer/Win_Waitable_Timer_Object_1.3.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'X509CertificateObjectType' : {'binding_name' : 'x509_certificate_object_1_2', 'namespace_prefix' : 'X509CertificateObj', 'namespace' : 'http://cybox.mitre.org/objects#X509CertificateObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/X509_Certificate/X509_Certificate_Object_1.2.xsd'} }

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    if Verbose_import_:
        print 'Error: LXML version 2.3+ required for parsing files'

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class ObservablesType(GeneratedsSuper):
    """The ObservablesType is a complex type representing a collection of
    cyber observables.The major_version attribute specifies the
    major version of the CybOX language utlized for this set of
    Observables.The minor_version attribute specifies the minor
    version of the CybOX language utlized for this set of
    Observables."""
    subclass = None
    superclass = None
    def __init__(self, cybox_minor_version=None, cybox_major_version=None, Observable_Package_Source=None, Observable=None, Pools=None, extensiontype_=None):
        self.cybox_minor_version = _cast(None, cybox_minor_version)
        self.cybox_major_version = _cast(None, cybox_major_version)
        self.Observable_Package_Source = Observable_Package_Source
        if Observable is None:
            self.Observable = []
        else:
            self.Observable = Observable
        self.Pools = Pools
        self.extensiontype_ = extensiontype_
        #A list of the types of objects in the Observables
        self.__object_types = []
        self.__object_type_dependencies = []
    def factory(*args_, **kwargs_):
        if ObservablesType.subclass:
            return ObservablesType.subclass(*args_, **kwargs_)
        else:
            return ObservablesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Observable_Package_Source(self): return self.Observable_Package_Source
    def set_Observable_Package_Source(self, Observable_Package_Source): self.Observable_Package_Source = Observable_Package_Source
    def get_Observable(self): return self.Observable
    def set_Observable(self, Observable): self.Observable = Observable
    def add_Observable(self, value): self.Observable.append(value)
    def insert_Observable(self, index, value): self.Observable[index] = value
    def get_Pools(self): return self.Pools
    def set_Pools(self, Pools): self.Pools = Pools
    def get_cybox_minor_version(self): return self.cybox_minor_version
    def set_cybox_minor_version(self, cybox_minor_version): self.cybox_minor_version = cybox_minor_version
    def get_cybox_major_version(self): return self.cybox_major_version
    def set_cybox_major_version(self, cybox_major_version): self.cybox_major_version = cybox_major_version
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    #Functions for grabbing the namespaces of all objects in the current Observables instance
    def __get_object_namespaces(self):
        for observable in self.get_Observable():
            self.__process_observable_namespace(observable)
    def __process_event_namespace(self, event):
        if event.get_Actions() is not None:
            for action in event.get_Actions().get_Action():
                for associated_object in action.get_Associated_Objects().get_Associated_Object():
                    self.__get_namespace_from_object(associated_object)
        if event.get_Event() is not None:
            for embedded_event in event.get_Event():
                self.__process_event_namespace(embedded_event)
    def __process_observable_namespace(self, observable):
        if observable.get_Stateful_Measure() is not None:
            object = observable.get_Stateful_Measure().get_Object()
            self.__get_namespace_from_object(object)
        elif observable.get_Event() is not None:
            self.__process_event_namespace(observable.get_Event())
        elif observable.get_Observable_Composition() is not None:
            for embedded_observable in observable.get_Observable_Composition().get_Observable():
                self.__process_observable_namespace(embedded_observable)
    def __get_namespace_from_object(self, object):
        if object.get_Defined_Object() is not None:
            defined_object = object.get_Defined_Object()
            if defined_object.get_anyAttributes_() is not None:
                any_attributes = defined_object.get_anyAttributes_()
                self.__get_defined_object_namespace(any_attributes)
        if object.get_Discovery_Method() is not None:
            discovery_method = object.get_Discovery_Method()
            if discovery_method.get_System() is not None:
                self.__add_object_namespace('SystemObjectType')
            if discovery_method.get_Tools() is not None:
                for tool in discovery_method.get_Tools().get_Tool():
                    if tool.get_Execution_Environment() is not None:
                        execution_environment = tool.get_Execution_Environment()
                        if execution_environment.get_System() is not None:
                            self.__add_object_namespace('SystemObjectType')
                        if execution_environment.get_User_Account_Info() is not None:
                            self.__add_object_namespace('UserAccountObjectType')
            if discovery_method.get_Instance() is not None:
                self.__add_object_namespace('ProcessObjectType')
    def __get_defined_object_namespace(self, any_attributes):
        for key, value in any_attributes.items():
            if (key == '{http://www.w3.org/2001/XMLSchema-instance}type' or key == 'xsi:type') and value.split(':')[1] in defined_objects.keys():
                self.__add_object_namespace(value.split(':')[1])
    def __add_object_namespace(self, object_type):
        if object_type not in self.__object_types:
            #Add the object type
            self.__object_types.append(object_type)
            #Add any dependencies
            if defined_objects.get(object_type).get('dependencies') is not None:
                dependencies = defined_objects.get(object_type).get('dependencies').split(',')
                for dependency in dependencies:
                    if dependency not in self.__object_types:
                        self.__object_type_dependencies.append(dependency)
    #Build the namespace/schemalocation declaration string
    def __build_namespaces_schemalocations(self):
        output_string = '\n '
        schemalocs = []
        #Add the XSI and CybOX Core/Common namespaces and schemalocation
        output_string += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \n '
        output_string += 'xmlns:cybox="http://cybox.mitre.org/cybox_v1" \n '
        output_string += 'xmlns:Common="http://cybox.mitre.org/Common_v1" \n '
        schemalocs.append('http://cybox.mitre.org/cybox_v1 http://cybox.mitre.org/XMLSchema/cybox_core_v1.0.xsd')
        for object_type in self.__object_types:
            namespace_prefix = defined_objects.get(object_type).get('namespace_prefix')
            namespace = defined_objects.get(object_type).get('namespace')
            output_string += ('xmlns:' + namespace_prefix + '=' + '"' + namespace + '"' + ' \n ')
        for object_type_dependency in self.__object_type_dependencies:
            if object_type_dependency not in self.__object_types:
                namespace_prefix = defined_objects.get(object_type_dependency).get('namespace_prefix')
                namespace = defined_objects.get(object_type_dependency).get('namespace')
                output_string += ('xmlns:' + namespace_prefix + '=' + '"' + namespace + '"' + ' \n ')
        output_string += 'xsi:schemaLocation="'
        for object_type in self.__object_types:
            namespace = defined_objects.get(object_type).get('namespace')
            schemalocation = defined_objects.get(object_type).get('schemalocation')
            schemalocs.append(' ' + namespace + ' ' + schemalocation)
        for schemalocation_string in schemalocs:
            if schemalocs.index(schemalocation_string) == (len(schemalocs) - 1):
                output_string += (schemalocation_string + '"')
            else:
                output_string += (schemalocation_string + '\n')
        return output_string
    def export(self, outfile, level, namespace_='cybox:', name_='Observables', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        #Build and set the namespace declarations so that we generate valid CybOX XML
        if namespacedef_ == None or namespacedef_ == '':
            #First, find all of the objects used and get their namespaces
            self.__get_object_namespaces()
            #Create the namespace string and set the namespacedef to it
            namespacedef_ = self.__build_namespaces_schemalocations()
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObservablesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='Observables'):
        if self.cybox_minor_version is not None and 'cybox_minor_version' not in already_processed:
            already_processed.append('cybox_minor_version')
            outfile.write(' cybox_minor_version=%s' % (self.gds_format_string(quote_attrib(self.cybox_minor_version).encode(ExternalEncoding), input_name='cybox_minor_version'), ))
        if self.cybox_major_version is not None and 'cybox_major_version' not in already_processed:
            already_processed.append('cybox_major_version')
            outfile.write(' cybox_major_version=%s' % (self.gds_format_string(quote_attrib(self.cybox_major_version).encode(ExternalEncoding), input_name='cybox_major_version'), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.append('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='Observables', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Observable_Package_Source is not None:
            self.Observable_Package_Source.export(outfile, level, 'cybox:', name_='Observable_Package_Source', pretty_print=pretty_print)
        for Observable_ in self.Observable:
            Observable_.export(outfile, level, 'cybox:', name_='Observable', pretty_print=pretty_print)
        if self.Pools is not None:
            self.Pools.export(outfile, level, 'cybox:', name_='Pools', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Observable_Package_Source is not None or
            self.Observable or
            self.Pools is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='Observables'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.cybox_minor_version is not None and 'cybox_minor_version' not in already_processed:
            already_processed.append('cybox_minor_version')
            showIndent(outfile, level)
            outfile.write('cybox_minor_version = "%s",\n' % (self.cybox_minor_version,))
        if self.cybox_major_version is not None and 'cybox_major_version' not in already_processed:
            already_processed.append('cybox_major_version')
            showIndent(outfile, level)
            outfile.write('cybox_major_version = "%s",\n' % (self.cybox_major_version,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Observable_Package_Source is not None:
            showIndent(outfile, level)
            outfile.write('Observable_Package_Source=model_.cybox_common_types_1_0.MeasureSourceType(\n')
            self.Observable_Package_Source.exportLiteral(outfile, level, name_='Observable_Package_Source')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Observable=[\n')
        level += 1
        for Observable_ in self.Observable:
            showIndent(outfile, level)
            outfile.write('model_.Observable(\n')
            Observable_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Pools is not None:
            showIndent(outfile, level)
            outfile.write('Pools=model_.PoolsType(\n')
            self.Pools.exportLiteral(outfile, level, name_='Pools')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('cybox_minor_version', node)
        if value is not None and 'cybox_minor_version' not in already_processed:
            already_processed.append('cybox_minor_version')
            self.cybox_minor_version = value
        value = find_attr_value_('cybox_major_version', node)
        if value is not None and 'cybox_major_version' not in already_processed:
            already_processed.append('cybox_major_version')
            self.cybox_major_version = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.append('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Observable_Package_Source':
            obj_ = cybox_common_types_1_0.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Observable_Package_Source(obj_)
        elif nodeName_ == 'Observable':
            obj_ = ObservableType.factory()
            obj_.build(child_)
            self.Observable.append(obj_)
        elif nodeName_ == 'Pools':
            obj_ = PoolsType.factory()
            obj_.build(child_)
            self.set_Pools(obj_)
# end class ObservablesType

class ObservableType(GeneratedsSuper):
    """The ObservableType is a complex type representing a description of a
    single cyber observable.The id attribute specifies a unique id
    for this Observable.The idref attribute specifies a unique id
    reference to an Observable defined elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Title=None, Description=None, Keywords=None, Observable_Source=None, Stateful_Measure=None, Event=None, Observable_Composition=None, Noisiness=None, Ease_of_Obfuscation=None, Obfuscation_Techniques=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Title = Title
        self.Description = Description
        if Keywords is None:
            self.Keywords = []
        else:
            self.Keywords = Keywords
        self.Observable_Source = Observable_Source
        self.Stateful_Measure = Stateful_Measure
        self.Event = Event
        self.Observable_Composition = Observable_Composition
        self.Noisiness = Noisiness
        self.Ease_of_Obfuscation = Ease_of_Obfuscation
        self.Obfuscation_Techniques = Obfuscation_Techniques
    def factory(*args_, **kwargs_):
        if ObservableType.subclass:
            return ObservableType.subclass(*args_, **kwargs_)
        else:
            return ObservableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Keywords(self): return self.Keywords
    def set_Keywords(self, Keywords): self.Keywords = Keywords
    def add_Keywords(self, value): self.Keywords.append(value)
    def insert_Keywords(self, index, value): self.Keywords[index] = value
    def get_Observable_Source(self): return self.Observable_Source
    def set_Observable_Source(self, Observable_Source): self.Observable_Source = Observable_Source
    def get_Stateful_Measure(self): return self.Stateful_Measure
    def set_Stateful_Measure(self, Stateful_Measure): self.Stateful_Measure = Stateful_Measure
    def get_Event(self): return self.Event
    def set_Event(self, Event): self.Event = Event
    def get_Observable_Composition(self): return self.Observable_Composition
    def set_Observable_Composition(self, Observable_Composition): self.Observable_Composition = Observable_Composition
    def get_Noisiness(self): return self.Noisiness
    def set_Noisiness(self, Noisiness): self.Noisiness = Noisiness
    def validate_NoisinessEnum(self, value):
        # Validate type NoisinessEnum, a restriction on xs:string.
        pass
    def get_Ease_of_Obfuscation(self): return self.Ease_of_Obfuscation
    def set_Ease_of_Obfuscation(self, Ease_of_Obfuscation): self.Ease_of_Obfuscation = Ease_of_Obfuscation
    def validate_EaseOfObfuscationEnum(self, value):
        # Validate type EaseOfObfuscationEnum, a restriction on xs:string.
        pass
    def get_Obfuscation_Techniques(self): return self.Obfuscation_Techniques
    def set_Obfuscation_Techniques(self, Obfuscation_Techniques): self.Obfuscation_Techniques = Obfuscation_Techniques
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def export(self, outfile, level, namespace_='cybox:', name_='ObservableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObservableType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObservableType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.append('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObservableType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sTitle>%s</%sTitle>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Title).encode(ExternalEncoding), input_name='Title'), 'cybox:', eol_))
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        for Keywords_ in self.Keywords:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sKeywords>%s</%sKeywords>%s' % ('cybox:', self.gds_format_string(quote_xml(Keywords_).encode(ExternalEncoding), input_name='Keywords'), 'cybox:', eol_))
        if self.Observable_Source is not None:
            self.Observable_Source.export(outfile, level, 'cybox:', name_='Observable_Source', pretty_print=pretty_print)
        if self.Stateful_Measure is not None:
            self.Stateful_Measure.export(outfile, level, 'cybox:', name_='Stateful_Measure', pretty_print=pretty_print)
        if self.Event is not None:
            self.Event.export(outfile, level, 'cybox:', name_='Event', pretty_print=pretty_print)
        if self.Observable_Composition is not None:
            self.Observable_Composition.export(outfile, level, 'cybox:', name_='Observable_Composition', pretty_print=pretty_print)
        if self.Noisiness is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sNoisiness>%s</%sNoisiness>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Noisiness).encode(ExternalEncoding), input_name='Noisiness'), 'cybox:', eol_))
        if self.Ease_of_Obfuscation is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sEase_of_Obfuscation>%s</%sEase_of_Obfuscation>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Ease_of_Obfuscation).encode(ExternalEncoding), input_name='Ease_of_Obfuscation'), 'cybox:', eol_))
        if self.Obfuscation_Techniques is not None:
            self.Obfuscation_Techniques.export(outfile, level, 'cybox:', name_='Obfuscation_Techniques', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Description is not None or
            self.Keywords or
            self.Observable_Source is not None or
            self.Stateful_Measure is not None or
            self.Event is not None or
            self.Observable_Composition is not None or
            self.Noisiness is not None or
            self.Ease_of_Obfuscation is not None or
            self.Obfuscation_Techniques is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ObservableType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.append('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Title is not None:
            showIndent(outfile, level)
            outfile.write('Title=%s,\n' % quote_python(self.Title).encode(ExternalEncoding))
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description=model_.cybox_common_types_1_0.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Keywords=[\n')
        level += 1
        for Keywords_ in self.Keywords:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(Keywords_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Observable_Source is not None:
            showIndent(outfile, level)
            outfile.write('Observable_Source=model_.cybox_common_types_1_0.MeasureSourceType(\n')
            self.Observable_Source.exportLiteral(outfile, level, name_='Observable_Source')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Stateful_Measure is not None:
            showIndent(outfile, level)
            outfile.write('Stateful_Measure=model_.StatefulMeasureType(\n')
            self.Stateful_Measure.exportLiteral(outfile, level, name_='Stateful_Measure')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Event is not None:
            showIndent(outfile, level)
            outfile.write('Event=model_.Event(\n')
            self.Event.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Observable_Composition is not None:
            showIndent(outfile, level)
            outfile.write('Observable_Composition=model_.ObservableCompositionType(\n')
            self.Observable_Composition.exportLiteral(outfile, level, name_='Observable_Composition')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Noisiness is not None:
            showIndent(outfile, level)
            outfile.write('Noisiness=%s,\n' % quote_python(self.Noisiness).encode(ExternalEncoding))
        if self.Ease_of_Obfuscation is not None:
            showIndent(outfile, level)
            outfile.write('Ease_of_Obfuscation=%s,\n' % quote_python(self.Ease_of_Obfuscation).encode(ExternalEncoding))
        if self.Obfuscation_Techniques is not None:
            showIndent(outfile, level)
            outfile.write('Obfuscation_Techniques=model_.ObfuscationTechniquesType(\n')
            self.Obfuscation_Techniques.exportLiteral(outfile, level, name_='Obfuscation_Techniques')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.append('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Description':
            obj_ = cybox_common_types_1_0.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Keywords':
            Keywords_ = child_.text
            Keywords_ = self.gds_validate_string(Keywords_, node, 'Keywords')
            self.Keywords.append(Keywords_)
        elif nodeName_ == 'Observable_Source':
            obj_ = cybox_common_types_1_0.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Observable_Source(obj_)
        elif nodeName_ == 'Stateful_Measure':
            obj_ = StatefulMeasureType.factory()
            obj_.build(child_)
            self.set_Stateful_Measure(obj_)
        elif nodeName_ == 'Event':
            obj_ = EventType.factory()
            obj_.build(child_)
            self.set_Event(obj_)
        elif nodeName_ == 'Observable_Composition':
            obj_ = ObservableCompositionType.factory()
            obj_.build(child_)
            self.set_Observable_Composition(obj_)
        elif nodeName_ == 'Noisiness':
            obj_ = child_.text 
            obj_ = self.gds_validate_string(obj_, node, 'Noisiness') 
            self.set_Noisiness(obj_)
        elif nodeName_ == 'Ease_of_Obfuscation':
            obj_ = child_.text 
            obj_ = self.gds_validate_string(obj_, node, 'Ease_of_Obfuscation') 
            self.set_Ease_of_Obfuscation(obj_)
        elif nodeName_ == 'Obfuscation_Techniques':
            obj_ = ObfuscationTechniquesType.factory()
            obj_.build(child_)
            self.set_Obfuscation_Techniques(obj_)
# end class ObservableType

class StatefulMeasureType(GeneratedsSuper):
    """The StatefulMeasureType is a complex type representing a cyber
    observable property that is statically stateful in nature (e.g.
    a registry key holding a certain value, a specific mutex
    existing or a file having a specific MD5 hash). The name
    attribute is optional and enables the assignment of a relevant
    name to a specific Stateful Measure.The has_changed attribute is
    optional and conveys a targeted observation pattern of whether
    the associated stateful measure specified has changed. This
    attribute would be leveraged within a pattern observable
    triggering on whether the value of a stateful measure comprised
    of an objet specification has changed."""
    subclass = None
    superclass = None
    def __init__(self, has_changed=None, name=None, Description=None, Object=None):
        self.has_changed = _cast(bool, has_changed)
        self.name = _cast(None, name)
        self.Description = Description
        self.Object = Object
    def factory(*args_, **kwargs_):
        if StatefulMeasureType.subclass:
            return StatefulMeasureType.subclass(*args_, **kwargs_)
        else:
            return StatefulMeasureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Object(self): return self.Object
    def set_Object(self, Object): self.Object = Object
    def get_has_changed(self): return self.has_changed
    def set_has_changed(self, has_changed): self.has_changed = has_changed
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def export(self, outfile, level, namespace_='cybox:', name_='StatefulMeasureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='StatefulMeasureType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='StatefulMeasureType'):
        if self.has_changed is not None and 'has_changed' not in already_processed:
            already_processed.append('has_changed')
            outfile.write(' has_changed="%s"' % self.gds_format_boolean(self.gds_str_lower(str(self.has_changed)), input_name='has_changed'))
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            outfile.write(' name=%s' % (self.gds_format_string(quote_attrib(self.name).encode(ExternalEncoding), input_name='name'), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='StatefulMeasureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Object is not None:
            self.Object.export(outfile, level, 'cybox:', name_='Object', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Object is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='StatefulMeasureType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.has_changed is not None and 'has_changed' not in already_processed:
            already_processed.append('has_changed')
            showIndent(outfile, level)
            outfile.write('has_changed = %s,\n' % (self.has_changed,))
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            showIndent(outfile, level)
            outfile.write('name = "%s",\n' % (self.name,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description=model_.cybox_common_types_1_0.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Object is not None:
            showIndent(outfile, level)
            outfile.write('Object=model_.Object(\n')
            self.Object.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('has_changed', node)
        if value is not None and 'has_changed' not in already_processed:
            already_processed.append('has_changed')
            if value in ('true', '1'):
                self.has_changed = True
            elif value in ('false', '0'):
                self.has_changed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.append('name')
            self.name = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common_types_1_0.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Object':
            obj_ = ObjectType.factory()
            obj_.build(child_)
            self.set_Object(obj_)
# end class StatefulMeasureType

class EventType(GeneratedsSuper):
    """The EventType is a complex type representing a cyber observable
    event that is dynamic in nature with specific action(s) taken
    against specific cyber relevant objects (e.g. a file is deleted,
    a registry key is created or an HTTP Get Request is
    received).The id attribute specifies a unique id for this
    Event.The idref attribute specifies a unique id reference to an
    Event defined elsewhere.The type attribute specifies what kind
    of Event this is."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, type_=None, id=None, Description=None, Producer_Observer=None, Actions=None, Frequency=None, Event=None):
        self.idref = _cast(None, idref)
        self.type_ = _cast(None, type_)
        self.id = _cast(None, id)
        self.Description = Description
        self.Producer_Observer = Producer_Observer
        self.Actions = Actions
        self.Frequency = Frequency
        self.Event = Event
    def factory(*args_, **kwargs_):
        if EventType.subclass:
            return EventType.subclass(*args_, **kwargs_)
        else:
            return EventType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Producer_Observer(self): return self.Producer_Observer
    def set_Producer_Observer(self, Producer_Observer): self.Producer_Observer = Producer_Observer
    def get_Actions(self): return self.Actions
    def set_Actions(self, Actions): self.Actions = Actions
    def get_Frequency(self): return self.Frequency
    def set_Frequency(self, Frequency): self.Frequency = Frequency
    def get_Event(self): return self.Event
    def set_Event(self, Event): self.Event = Event
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def export(self, outfile, level, namespace_='cybox:', name_='EventType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EventType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='EventType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.append('type_')
            outfile.write(' type=%s' % (quote_attrib(self.type_), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.append('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='EventType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Producer_Observer is not None:
            self.Producer_Observer.export(outfile, level, 'cybox:', name_='Producer-Observer', pretty_print=pretty_print)
        if self.Actions is not None:
            self.Actions.export(outfile, level, 'cybox:', name_='Actions', pretty_print=pretty_print)
        if self.Frequency is not None:
            self.Frequency.export(outfile, level, 'cybox:', name_='Frequency', pretty_print=pretty_print)
        if self.Event is not None:
            self.Event.export(outfile, level, 'cybox:', name_='Event', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Producer_Observer is not None or
            self.Actions is not None or
            self.Frequency is not None or
            self.Event is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='EventType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.append('type_')
            showIndent(outfile, level)
            outfile.write('type_ = %s,\n' % (self.type_,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.append('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description=model_.cybox_common_types_1_0.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Producer_Observer is not None:
            showIndent(outfile, level)
            outfile.write('Producer_Observer=model_.cybox_common_types_1_0.MeasureSourceType(\n')
            self.Producer_Observer.exportLiteral(outfile, level, name_='Producer_Observer')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Actions is not None:
            showIndent(outfile, level)
            outfile.write('Actions=model_.ActionsType(\n')
            self.Actions.exportLiteral(outfile, level, name_='Actions')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Frequency is not None:
            showIndent(outfile, level)
            outfile.write('Frequency=model_.FrequencyType(\n')
            self.Frequency.exportLiteral(outfile, level, name_='Frequency')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Event is not None:
            showIndent(outfile, level)
            outfile.write('Event=model_.EventType(\n')
            self.Event.exportLiteral(outfile, level, name_='Event')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            self.idref = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.append('type')
            self.type_ = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.append('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common_types_1_0.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Producer-Observer':
            obj_ = cybox_common_types_1_0.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Producer_Observer(obj_)
        elif nodeName_ == 'Actions':
            obj_ = ActionsType.factory()
            obj_.build(child_)
            self.set_Actions(obj_)
        elif nodeName_ == 'Frequency':
            obj_ = FrequencyType.factory()
            obj_.build(child_)
            self.set_Frequency(obj_)
        elif nodeName_ == 'Event':
            obj_ = EventType.factory()
            obj_.build(child_)
            self.set_Event(obj_)
# end class EventType

class FrequencyType(GeneratedsSuper):
    """The FrequencyType is a complex type representing the specification
    of a frequency for a given action or event..This attribute
    specifies the rate for this defined frequency.This attribute
    specifies the units for this defined frequency.This attribute
    specifies the time scale for this defined frequency.This
    attribute is optional and conveys a targeted observation pattern
    of the nature of any trend in the frequency of the associated
    event or action. This attribute would be leveraged within an
    event or action pattern observable triggering on the matching of
    a specified trend in the frequency of an event or action."""
    subclass = None
    superclass = None
    def __init__(self, units=None, trend=None, rate=None, scale=None):
        self.units = _cast(None, units)
        self.trend = _cast(None, trend)
        self.rate = _cast(float, rate)
        self.scale = _cast(None, scale)
        pass
    def factory(*args_, **kwargs_):
        if FrequencyType.subclass:
            return FrequencyType.subclass(*args_, **kwargs_)
        else:
            return FrequencyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_units(self): return self.units
    def set_units(self, units): self.units = units
    def get_trend(self): return self.trend
    def set_trend(self, trend): self.trend = trend
    def get_rate(self): return self.rate
    def set_rate(self, rate): self.rate = rate
    def get_scale(self): return self.scale
    def set_scale(self, scale): self.scale = scale
    def export(self, outfile, level, namespace_='cybox:', name_='FrequencyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='FrequencyType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='FrequencyType'):
        if self.units is not None and 'units' not in already_processed:
            already_processed.append('units')
            outfile.write(' units=%s' % (self.gds_format_string(quote_attrib(self.units).encode(ExternalEncoding), input_name='units'), ))
        if self.trend is not None and 'trend' not in already_processed:
            already_processed.append('trend')
            outfile.write(' trend=%s' % (quote_attrib(self.trend), ))
        if self.rate is not None and 'rate' not in already_processed:
            already_processed.append('rate')
            outfile.write(' rate="%s"' % self.gds_format_float(self.rate, input_name='rate'))
        if self.scale is not None and 'scale' not in already_processed:
            already_processed.append('scale')
            outfile.write(' scale=%s' % (self.gds_format_string(quote_attrib(self.scale).encode(ExternalEncoding), input_name='scale'), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='FrequencyType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='FrequencyType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.units is not None and 'units' not in already_processed:
            already_processed.append('units')
            showIndent(outfile, level)
            outfile.write('units = "%s",\n' % (self.units,))
        if self.trend is not None and 'trend' not in already_processed:
            already_processed.append('trend')
            showIndent(outfile, level)
            outfile.write('trend = %s,\n' % (self.trend,))
        if self.rate is not None and 'rate' not in already_processed:
            already_processed.append('rate')
            showIndent(outfile, level)
            outfile.write('rate = %f,\n' % (self.rate,))
        if self.scale is not None and 'scale' not in already_processed:
            already_processed.append('scale')
            showIndent(outfile, level)
            outfile.write('scale = "%s",\n' % (self.scale,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('units', node)
        if value is not None and 'units' not in already_processed:
            already_processed.append('units')
            self.units = value
        value = find_attr_value_('trend', node)
        if value is not None and 'trend' not in already_processed:
            already_processed.append('trend')
            self.trend = value
        value = find_attr_value_('rate', node)
        if value is not None and 'rate' not in already_processed:
            already_processed.append('rate')
            try:
                self.rate = float(value)
            except ValueError, exp:
                raise ValueError('Bad float/double attribute (rate): %s' % exp)
        value = find_attr_value_('scale', node)
        if value is not None and 'scale' not in already_processed:
            already_processed.append('scale')
            self.scale = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class FrequencyType

class ActionsType(GeneratedsSuper):
    """The ActionsType is a complex type representing a set of cyber
    observable actions."""
    subclass = None
    superclass = None
    def __init__(self, Action=None):
        if Action is None:
            self.Action = []
        else:
            self.Action = Action
    def factory(*args_, **kwargs_):
        if ActionsType.subclass:
            return ActionsType.subclass(*args_, **kwargs_)
        else:
            return ActionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action(self): return self.Action
    def set_Action(self, Action): self.Action = Action
    def add_Action(self, value): self.Action.append(value)
    def insert_Action(self, index, value): self.Action[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='ActionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_ in self.Action:
            Action_.export(outfile, level, 'cybox:', name_='Action', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Action
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action=[\n')
        level += 1
        for Action_ in self.Action:
            showIndent(outfile, level)
            outfile.write('model_.Action(\n')
            Action_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action':
            obj_ = ActionType.factory()
            obj_.build(child_)
            self.Action.append(obj_)
# end class ActionsType

class ActionType(GeneratedsSuper):
    """The ActionType is a complex type representing a single cyber
    observable action.The id attribute specifies a unique id for
    this Action.The idref attribute specifies a unique id reference
    to an Action defined elsewhere.The type attribute specifies the
    basic type of action performed.The name attribute is optional
    and utilizes a standardized defined name to
    identify/characterize the specific action performed. Wherever
    possible, standardized defined action names should be
    utilized.The undefined_name attribute is optional and utilizes a
    non-standardized undefined name to identify/characterize the
    specific action performed.The ordinal_position attribute is
    intended to reference the ordinal position of the action with
    within a series of actions.The action_status attribute enables
    description of the status of the action being described.The
    context attribute is optional and enables simple
    characterization of the broad operational context in which the
    Action is relevantThe network_protocol attribute is optional and
    (where the Context is Network) enables the description of the
    relevant network protocol involved in the Action.The timestamp
    attribute represents the local or relative time at which the
    action occurred or was observed. The "any" attribute enables the
    capture of custom attributes describing this Action."""
    subclass = None
    superclass = None
    def __init__(self, undefined_name=None, name=None, timestamp=None, action_status=None, ordinal_position=None, context=None, idref=None, type_=None, id=None, network_protocol=None, Description=None, Action_Aliases=None, Action_Arguments=None, Discovery_Method=None, Associated_Objects=None, Relationships=None, Frequency=None):
        self.undefined_name = _cast(None, undefined_name)
        self.name = _cast(None, name)
        self.timestamp = _cast(None, timestamp)
        self.action_status = _cast(None, action_status)
        self.ordinal_position = _cast(int, ordinal_position)
        self.context = _cast(None, context)
        self.idref = _cast(None, idref)
        self.type_ = _cast(None, type_)
        self.id = _cast(None, id)
        self.network_protocol = _cast(None, network_protocol)
        self.Description = Description
        self.Action_Aliases = Action_Aliases
        self.Action_Arguments = Action_Arguments
        self.Discovery_Method = Discovery_Method
        self.Associated_Objects = Associated_Objects
        self.Relationships = Relationships
        self.Frequency = Frequency
        self.anyAttributes_ = {}
    def factory(*args_, **kwargs_):
        if ActionType.subclass:
            return ActionType.subclass(*args_, **kwargs_)
        else:
            return ActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Action_Aliases(self): return self.Action_Aliases
    def set_Action_Aliases(self, Action_Aliases): self.Action_Aliases = Action_Aliases
    def get_Action_Arguments(self): return self.Action_Arguments
    def set_Action_Arguments(self, Action_Arguments): self.Action_Arguments = Action_Arguments
    def get_Discovery_Method(self): return self.Discovery_Method
    def set_Discovery_Method(self, Discovery_Method): self.Discovery_Method = Discovery_Method
    def get_Associated_Objects(self): return self.Associated_Objects
    def set_Associated_Objects(self, Associated_Objects): self.Associated_Objects = Associated_Objects
    def get_Relationships(self): return self.Relationships
    def set_Relationships(self, Relationships): self.Relationships = Relationships
    def get_Frequency(self): return self.Frequency
    def set_Frequency(self, Frequency): self.Frequency = Frequency
    def get_undefined_name(self): return self.undefined_name
    def set_undefined_name(self, undefined_name): self.undefined_name = undefined_name
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def get_action_status(self): return self.action_status
    def set_action_status(self, action_status): self.action_status = action_status
    def get_ordinal_position(self): return self.ordinal_position
    def set_ordinal_position(self, ordinal_position): self.ordinal_position = ordinal_position
    def get_context(self): return self.context
    def set_context(self, context): self.context = context
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_network_protocol(self): return self.network_protocol
    def set_network_protocol(self, network_protocol): self.network_protocol = network_protocol
    def get_anyAttributes_(self): return self.anyAttributes_
    def set_anyAttributes_(self, anyAttributes_): self.anyAttributes_ = anyAttributes_
    def export(self, outfile, level, namespace_='cybox:', name_='ActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionType'):
        unique_counter = 0
        for name, value in self.anyAttributes_.items():
            xsinamespaceprefix = 'xsi'
            xsinamespace1 = 'http://www.w3.org/2001/XMLSchema-instance'
            xsinamespace2 = '{%s}' % (xsinamespace1, )
            if name.startswith(xsinamespace2):
                name1 = name[len(xsinamespace2):]
                name2 = '%s:%s' % (xsinamespaceprefix, name1, )
                if name2 not in already_processed:
                    already_processed.append(name2)
                    outfile.write(' %s=%s' % (name2, quote_attrib(value), ))
            else:
                mo = re_.match(Namespace_extract_pat_, name)
                if mo is not None:
                    namespace, name = mo.group(1, 2)
                    if name not in already_processed:
                        already_processed.append(name)
                        if namespace == 'http://www.w3.org/XML/1998/namespace':
                            outfile.write(' %s=%s' % (name, quote_attrib(value), ))
                        else:
                            unique_counter += 1
                            outfile.write(' xmlns:yyy%d="%s"' % (unique_counter, namespace, ))
                            outfile.write(' yyy%d:%s=%s' % (unique_counter, name, quote_attrib(value), ))
                else:
                    if name not in already_processed:
                        already_processed.append(name)
                        outfile.write(' %s=%s' % (name, quote_attrib(value), ))
        if self.undefined_name is not None and 'undefined_name' not in already_processed:
            already_processed.append('undefined_name')
            outfile.write(' undefined_name=%s' % (self.gds_format_string(quote_attrib(self.undefined_name).encode(ExternalEncoding), input_name='undefined_name'), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            outfile.write(' name=%s' % (quote_attrib(self.name), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.append('timestamp')
            outfile.write(' timestamp=%s' % (self.gds_format_string(quote_attrib(self.timestamp).encode(ExternalEncoding), input_name='timestamp'), ))
        if self.action_status is not None and 'action_status' not in already_processed:
            already_processed.append('action_status')
            outfile.write(' action_status=%s' % (quote_attrib(self.action_status), ))
        if self.ordinal_position is not None and 'ordinal_position' not in already_processed:
            already_processed.append('ordinal_position')
            outfile.write(' ordinal_position="%s"' % self.gds_format_integer(self.ordinal_position, input_name='ordinal_position'))
        if self.context is not None and 'context' not in already_processed:
            already_processed.append('context')
            outfile.write(' context=%s' % (quote_attrib(self.context), ))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.append('type_')
            outfile.write(' type=%s' % (quote_attrib(self.type_), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.append('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
        if self.network_protocol is not None and 'network_protocol' not in already_processed:
            already_processed.append('network_protocol')
            outfile.write(' network_protocol=%s' % (quote_attrib(self.network_protocol), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Action_Aliases is not None:
            self.Action_Aliases.export(outfile, level, 'cybox:', name_='Action_Aliases', pretty_print=pretty_print)
        if self.Action_Arguments is not None:
            self.Action_Arguments.export(outfile, level, 'cybox:', name_='Action_Arguments', pretty_print=pretty_print)
        if self.Discovery_Method is not None:
            self.Discovery_Method.export(outfile, level, 'cybox:', name_='Discovery_Method', pretty_print=pretty_print)
        if self.Associated_Objects is not None:
            self.Associated_Objects.export(outfile, level, 'cybox:', name_='Associated_Objects', pretty_print=pretty_print)
        if self.Relationships is not None:
            self.Relationships.export(outfile, level, 'cybox:', name_='Relationships', pretty_print=pretty_print)
        if self.Frequency is not None:
            self.Frequency.export(outfile, level, 'cybox:', name_='Frequency', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Action_Aliases is not None or
            self.Action_Arguments is not None or
            self.Discovery_Method is not None or
            self.Associated_Objects is not None or
            self.Relationships is not None or
            self.Frequency is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.undefined_name is not None and 'undefined_name' not in already_processed:
            already_processed.append('undefined_name')
            showIndent(outfile, level)
            outfile.write('undefined_name = "%s",\n' % (self.undefined_name,))
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            showIndent(outfile, level)
            outfile.write('name = %s,\n' % (self.name,))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.append('timestamp')
            showIndent(outfile, level)
            outfile.write('timestamp = "%s",\n' % (self.timestamp,))
        if self.action_status is not None and 'action_status' not in already_processed:
            already_processed.append('action_status')
            showIndent(outfile, level)
            outfile.write('action_status = %s,\n' % (self.action_status,))
        if self.ordinal_position is not None and 'ordinal_position' not in already_processed:
            already_processed.append('ordinal_position')
            showIndent(outfile, level)
            outfile.write('ordinal_position = %d,\n' % (self.ordinal_position,))
        if self.context is not None and 'context' not in already_processed:
            already_processed.append('context')
            showIndent(outfile, level)
            outfile.write('context = %s,\n' % (self.context,))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.append('type_')
            showIndent(outfile, level)
            outfile.write('type_ = %s,\n' % (self.type_,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.append('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
        if self.network_protocol is not None and 'network_protocol' not in already_processed:
            already_processed.append('network_protocol')
            showIndent(outfile, level)
            outfile.write('network_protocol = %s,\n' % (self.network_protocol,))
        for name, value in self.anyAttributes_.items():
            showIndent(outfile, level)
            outfile.write('%s = "%s",\n' % (name, value,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description=model_.cybox_common_types_1_0.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Action_Aliases is not None:
            showIndent(outfile, level)
            outfile.write('Action_Aliases=model_.ActionAliasesType(\n')
            self.Action_Aliases.exportLiteral(outfile, level, name_='Action_Aliases')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Action_Arguments is not None:
            showIndent(outfile, level)
            outfile.write('Action_Arguments=model_.ActionArgumentsType(\n')
            self.Action_Arguments.exportLiteral(outfile, level, name_='Action_Arguments')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Discovery_Method is not None:
            showIndent(outfile, level)
            outfile.write('Discovery_Method=model_.cybox_common_types_1_0.MeasureSourceType(\n')
            self.Discovery_Method.exportLiteral(outfile, level, name_='Discovery_Method')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Associated_Objects is not None:
            showIndent(outfile, level)
            outfile.write('Associated_Objects=model_.AssociatedObjectsType(\n')
            self.Associated_Objects.exportLiteral(outfile, level, name_='Associated_Objects')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Relationships is not None:
            showIndent(outfile, level)
            outfile.write('Relationships=model_.RelationshipsType(\n')
            self.Relationships.exportLiteral(outfile, level, name_='Relationships')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Frequency is not None:
            showIndent(outfile, level)
            outfile.write('Frequency=model_.FrequencyType(\n')
            self.Frequency.exportLiteral(outfile, level, name_='Frequency')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('undefined_name', node)
        if value is not None and 'undefined_name' not in already_processed:
            already_processed.append('undefined_name')
            self.undefined_name = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.append('name')
            self.name = value
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.append('timestamp')
            self.timestamp = value
        value = find_attr_value_('action_status', node)
        if value is not None and 'action_status' not in already_processed:
            already_processed.append('action_status')
            self.action_status = value
        value = find_attr_value_('ordinal_position', node)
        if value is not None and 'ordinal_position' not in already_processed:
            already_processed.append('ordinal_position')
            try:
                self.ordinal_position = int(value)
            except ValueError, exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.ordinal_position <= 0:
                raise_parse_error(node, 'Invalid PositiveInteger')
        value = find_attr_value_('context', node)
        if value is not None and 'context' not in already_processed:
            already_processed.append('context')
            self.context = value
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            self.idref = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.append('type')
            self.type_ = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.append('id')
            self.id = value
        value = find_attr_value_('network_protocol', node)
        if value is not None and 'network_protocol' not in already_processed:
            already_processed.append('network_protocol')
            self.network_protocol = value
        self.anyAttributes_ = {}
        for name, value in attrs.items():
            if name not in already_processed:
                self.anyAttributes_[name] = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common_types_1_0.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Action_Aliases':
            obj_ = ActionAliasesType.factory()
            obj_.build(child_)
            self.set_Action_Aliases(obj_)
        elif nodeName_ == 'Action_Arguments':
            obj_ = ActionArgumentsType.factory()
            obj_.build(child_)
            self.set_Action_Arguments(obj_)
        elif nodeName_ == 'Discovery_Method':
            obj_ = cybox_common_types_1_0.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Discovery_Method(obj_)
        elif nodeName_ == 'Associated_Objects':
            obj_ = AssociatedObjectsType.factory()
            obj_.build(child_)
            self.set_Associated_Objects(obj_)
        elif nodeName_ == 'Relationships':
            obj_ = RelationshipsType.factory()
            obj_.build(child_)
            self.set_Relationships(obj_)
        elif nodeName_ == 'Frequency':
            obj_ = FrequencyType.factory()
            obj_.build(child_)
            self.set_Frequency(obj_)
# end class ActionType

class ActionAliasesType(GeneratedsSuper):
    """The ActionAliasesType enables identification of other potentially
    used names for this Action."""
    subclass = None
    superclass = None
    def __init__(self, Action_Alias=None):
        if Action_Alias is None:
            self.Action_Alias = []
        else:
            self.Action_Alias = Action_Alias
    def factory(*args_, **kwargs_):
        if ActionAliasesType.subclass:
            return ActionAliasesType.subclass(*args_, **kwargs_)
        else:
            return ActionAliasesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action_Alias(self): return self.Action_Alias
    def set_Action_Alias(self, Action_Alias): self.Action_Alias = Action_Alias
    def add_Action_Alias(self, value): self.Action_Alias.append(value)
    def insert_Action_Alias(self, index, value): self.Action_Alias[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='ActionAliasesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionAliasesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionAliasesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionAliasesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_Alias_ in self.Action_Alias:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAction_Alias>%s</%sAction_Alias>%s' % ('cybox:', self.gds_format_string(quote_xml(Action_Alias_).encode(ExternalEncoding), input_name='Action_Alias'), 'cybox:', eol_))
    def hasContent_(self):
        if (
            self.Action_Alias
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionAliasesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action_Alias=[\n')
        level += 1
        for Action_Alias_ in self.Action_Alias:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(Action_Alias_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action_Alias':
            Action_Alias_ = child_.text
            Action_Alias_ = self.gds_validate_string(Action_Alias_, node, 'Action_Alias')
            self.Action_Alias.append(Action_Alias_)
# end class ActionAliasesType

class ActionArgumentsType(GeneratedsSuper):
    """The ActionArgumentsType enables the specification of relevant
    arguments/parameters for this Action."""
    subclass = None
    superclass = None
    def __init__(self, Action_Argument=None):
        if Action_Argument is None:
            self.Action_Argument = []
        else:
            self.Action_Argument = Action_Argument
    def factory(*args_, **kwargs_):
        if ActionArgumentsType.subclass:
            return ActionArgumentsType.subclass(*args_, **kwargs_)
        else:
            return ActionArgumentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action_Argument(self): return self.Action_Argument
    def set_Action_Argument(self, Action_Argument): self.Action_Argument = Action_Argument
    def add_Action_Argument(self, value): self.Action_Argument.append(value)
    def insert_Action_Argument(self, index, value): self.Action_Argument[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='ActionArgumentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionArgumentsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionArgumentsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionArgumentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_Argument_ in self.Action_Argument:
            Action_Argument_.export(outfile, level, 'cybox:', name_='Action_Argument', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Action_Argument
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionArgumentsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action_Argument=[\n')
        level += 1
        for Action_Argument_ in self.Action_Argument:
            showIndent(outfile, level)
            outfile.write('model_.ActionArgumentType(\n')
            Action_Argument_.exportLiteral(outfile, level, name_='ActionArgumentType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action_Argument':
            obj_ = ActionArgumentType.factory()
            obj_.build(child_)
            self.Action_Argument.append(obj_)
# end class ActionArgumentsType

class ActionArgumentType(GeneratedsSuper):
    """The ActionArgumentType enables the specification of a single
    relevant argument/parameter for this Action.The
    defined_argument_name field is optional and utilizes a
    standardized defined name to identify/characterize the specific
    action argument utilized. Wherever possible, standardized
    defined argument names should be utilized.The
    undefined_argument_name field is optional and utilizes a non-
    standardized undefined name to identify/characterize the
    specific action argument utilized.The argument_value field
    specifies the value for this action argument/parameter."""
    subclass = None
    superclass = None
    def __init__(self, undefined_argument_name=None, argument_value=None, defined_argument_name=None):
        self.undefined_argument_name = _cast(None, undefined_argument_name)
        self.argument_value = _cast(None, argument_value)
        self.defined_argument_name = _cast(None, defined_argument_name)
        pass
    def factory(*args_, **kwargs_):
        if ActionArgumentType.subclass:
            return ActionArgumentType.subclass(*args_, **kwargs_)
        else:
            return ActionArgumentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_undefined_argument_name(self): return self.undefined_argument_name
    def set_undefined_argument_name(self, undefined_argument_name): self.undefined_argument_name = undefined_argument_name
    def get_argument_value(self): return self.argument_value
    def set_argument_value(self, argument_value): self.argument_value = argument_value
    def get_defined_argument_name(self): return self.defined_argument_name
    def set_defined_argument_name(self, defined_argument_name): self.defined_argument_name = defined_argument_name
    def export(self, outfile, level, namespace_='cybox:', name_='ActionArgumentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.hasContent_():
            showIndent(outfile, level, pretty_print)
            outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
            already_processed = []
            self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionArgumentType')
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionArgumentType'):
        if self.undefined_argument_name is not None and 'undefined_argument_name' not in already_processed:
            already_processed.append('undefined_argument_name')
            outfile.write(' undefined_argument_name=%s' % (self.gds_format_string(quote_attrib(self.undefined_argument_name).encode(ExternalEncoding), input_name='undefined_argument_name'), ))
        if self.argument_value is not None and 'argument_value' not in already_processed:
            already_processed.append('argument_value')
            outfile.write(' argument_value=%s' % (self.gds_format_string(quote_attrib(self.argument_value).encode(ExternalEncoding), input_name='argument_value'), ))
        if self.defined_argument_name is not None and 'defined_argument_name' not in already_processed:
            already_processed.append('defined_argument_name')
            outfile.write(' defined_argument_name=%s' % (quote_attrib(self.defined_argument_name), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionArgumentType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (
            self.defined_argument_name is not None or
            self.undefined_argument_name is not None or
            self.argument_value is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionArgumentType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.undefined_argument_name is not None and 'undefined_argument_name' not in already_processed:
            already_processed.append('undefined_argument_name')
            showIndent(outfile, level)
            outfile.write('undefined_argument_name = "%s",\n' % (self.undefined_argument_name,))
        if self.argument_value is not None and 'argument_value' not in already_processed:
            already_processed.append('argument_value')
            showIndent(outfile, level)
            outfile.write('argument_value = "%s",\n' % (self.argument_value,))
        if self.defined_argument_name is not None and 'defined_argument_name' not in already_processed:
            already_processed.append('defined_argument_name')
            showIndent(outfile, level)
            outfile.write('defined_argument_name = %s,\n' % (self.defined_argument_name,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('undefined_argument_name', node)
        if value is not None and 'undefined_argument_name' not in already_processed:
            already_processed.append('undefined_argument_name')
            self.undefined_argument_name = value
        value = find_attr_value_('argument_value', node)
        if value is not None and 'argument_value' not in already_processed:
            already_processed.append('argument_value')
            self.argument_value = value
        value = find_attr_value_('defined_argument_name', node)
        if value is not None and 'defined_argument_name' not in already_processed:
            already_processed.append('defined_argument_name')
            self.defined_argument_name = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ActionArgumentType

class AssociatedObjectsType(GeneratedsSuper):
    """The AssociatedObjectsType enables the description/specification of
    cyber Objects relevant to an Action."""
    subclass = None
    superclass = None
    def __init__(self, Associated_Object=None):
        if Associated_Object is None:
            self.Associated_Object = []
        else:
            self.Associated_Object = Associated_Object
    def factory(*args_, **kwargs_):
        if AssociatedObjectsType.subclass:
            return AssociatedObjectsType.subclass(*args_, **kwargs_)
        else:
            return AssociatedObjectsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Associated_Object(self): return self.Associated_Object
    def set_Associated_Object(self, Associated_Object): self.Associated_Object = Associated_Object
    def add_Associated_Object(self, value): self.Associated_Object.append(value)
    def insert_Associated_Object(self, index, value): self.Associated_Object[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='AssociatedObjectsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AssociatedObjectsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='AssociatedObjectsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='AssociatedObjectsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Associated_Object_ in self.Associated_Object:
            Associated_Object_.export(outfile, level, 'cybox:', name_='Associated_Object', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Associated_Object
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AssociatedObjectsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Associated_Object=[\n')
        level += 1
        for Associated_Object_ in self.Associated_Object:
            showIndent(outfile, level)
            outfile.write('model_.AssociatedObjectType(\n')
            Associated_Object_.exportLiteral(outfile, level, name_='AssociatedObjectType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Associated_Object':
            obj_ = AssociatedObjectType.factory()
            obj_.build(child_)
            self.Associated_Object.append(obj_)
# end class AssociatedObjectsType

class ActionPertinentObjectAttributesType(GeneratedsSuper):
    """The ActionPertinentObjectAttributesType identifies which of the
    Attributes of this Object are specifically pertinent to this
    Action."""
    subclass = None
    superclass = None
    def __init__(self, Attribute=None):
        if Attribute is None:
            self.Attribute = []
        else:
            self.Attribute = Attribute
    def factory(*args_, **kwargs_):
        if ActionPertinentObjectAttributesType.subclass:
            return ActionPertinentObjectAttributesType.subclass(*args_, **kwargs_)
        else:
            return ActionPertinentObjectAttributesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attribute(self): return self.Attribute
    def set_Attribute(self, Attribute): self.Attribute = Attribute
    def add_Attribute(self, value): self.Attribute.append(value)
    def insert_Attribute(self, index, value): self.Attribute[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='ActionPertinentObjectAttributesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionPertinentObjectAttributesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionPertinentObjectAttributesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionPertinentObjectAttributesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Attribute_ in self.Attribute:
            Attribute_.export(outfile, level, 'cybox:', name_='Attribute', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Attribute
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionPertinentObjectAttributesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Attribute=[\n')
        level += 1
        for Attribute_ in self.Attribute:
            showIndent(outfile, level)
            outfile.write('model_.ActionPertinentObjectAttributeType(\n')
            Attribute_.exportLiteral(outfile, level, name_='ActionPertinentObjectAttributeType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attribute':
            obj_ = ActionPertinentObjectAttributeType.factory()
            obj_.build(child_)
            self.Attribute.append(obj_)
# end class ActionPertinentObjectAttributesType

class ActionPertinentObjectAttributeType(GeneratedsSuper):
    """The ActionPertinentObjectAttributeType identifies one of the
    Attributes of an Object that specifically pertinent to an
    Action.The name attribute specifies the field name for the
    pertinent Object Attribute.The xpath attribute specifies the
    XPath expression identifying the pertinent attribute within the
    Defined_Object schema for this object type."""
    subclass = None
    superclass = None
    def __init__(self, xpath=None, name=None):
        self.xpath = _cast(None, xpath)
        self.name = _cast(None, name)
        pass
    def factory(*args_, **kwargs_):
        if ActionPertinentObjectAttributeType.subclass:
            return ActionPertinentObjectAttributeType.subclass(*args_, **kwargs_)
        else:
            return ActionPertinentObjectAttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_xpath(self): return self.xpath
    def set_xpath(self, xpath): self.xpath = xpath
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def export(self, outfile, level, namespace_='cybox:', name_='ActionPertinentObjectAttributeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionPertinentObjectAttributeType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionPertinentObjectAttributeType'):
        if self.xpath is not None and 'xpath' not in already_processed:
            already_processed.append('xpath')
            outfile.write(' xpath=%s' % (self.gds_format_string(quote_attrib(self.xpath).encode(ExternalEncoding), input_name='xpath'), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            outfile.write(' name=%s' % (self.gds_format_string(quote_attrib(self.name).encode(ExternalEncoding), input_name='name'), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionPertinentObjectAttributeType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionPertinentObjectAttributeType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.xpath is not None and 'xpath' not in already_processed:
            already_processed.append('xpath')
            showIndent(outfile, level)
            outfile.write('xpath = "%s",\n' % (self.xpath,))
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            showIndent(outfile, level)
            outfile.write('name = "%s",\n' % (self.name,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xpath', node)
        if value is not None and 'xpath' not in already_processed:
            already_processed.append('xpath')
            self.xpath = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.append('name')
            self.name = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ActionPertinentObjectAttributeType

class RelationshipsType(GeneratedsSuper):
    """The RelationshipsType enables description of other cyber observable
    actions that are related to this Action."""
    subclass = None
    superclass = None
    def __init__(self, Relationship=None):
        if Relationship is None:
            self.Relationship = []
        else:
            self.Relationship = Relationship
    def factory(*args_, **kwargs_):
        if RelationshipsType.subclass:
            return RelationshipsType.subclass(*args_, **kwargs_)
        else:
            return RelationshipsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Relationship(self): return self.Relationship
    def set_Relationship(self, Relationship): self.Relationship = Relationship
    def add_Relationship(self, value): self.Relationship.append(value)
    def insert_Relationship(self, index, value): self.Relationship[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='RelationshipsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RelationshipsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='RelationshipsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='RelationshipsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Relationship_ in self.Relationship:
            Relationship_.export(outfile, level, 'cybox:', name_='Relationship', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Relationship
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='RelationshipsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Relationship=[\n')
        level += 1
        for Relationship_ in self.Relationship:
            showIndent(outfile, level)
            outfile.write('model_.ActionRelationshipType(\n')
            Relationship_.exportLiteral(outfile, level, name_='ActionRelationshipType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Relationship':
            obj_ = ActionRelationshipType.factory()
            obj_.build(child_)
            self.Relationship.append(obj_)
# end class RelationshipsType

class ActionRelationshipType(GeneratedsSuper):
    """The ActionRelationshipType is a complex type characterizing a
    relationship between a specified cyber observable action and
    another cyber observable action.The type attribute describes the
    nature of the relationship between this Action and the related
    Action."""
    subclass = None
    superclass = None
    def __init__(self, type_=None, Action_Reference=None):
        self.type_ = _cast(None, type_)
        if Action_Reference is None:
            self.Action_Reference = []
        else:
            self.Action_Reference = Action_Reference
    def factory(*args_, **kwargs_):
        if ActionRelationshipType.subclass:
            return ActionRelationshipType.subclass(*args_, **kwargs_)
        else:
            return ActionRelationshipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action_Reference(self): return self.Action_Reference
    def set_Action_Reference(self, Action_Reference): self.Action_Reference = Action_Reference
    def add_Action_Reference(self, value): self.Action_Reference.append(value)
    def insert_Action_Reference(self, index, value): self.Action_Reference[index] = value
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def export(self, outfile, level, namespace_='cybox:', name_='ActionRelationshipType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionRelationshipType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionRelationshipType'):
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.append('type_')
            outfile.write(' type=%s' % (quote_attrib(self.type_), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionRelationshipType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_Reference_ in self.Action_Reference:
            Action_Reference_.export(outfile, level, 'cybox:', name_='Action_Reference', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Action_Reference
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionRelationshipType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.append('type_')
            showIndent(outfile, level)
            outfile.write('type_ = %s,\n' % (self.type_,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action_Reference=[\n')
        level += 1
        for Action_Reference_ in self.Action_Reference:
            showIndent(outfile, level)
            outfile.write('model_.ActionReferenceType(\n')
            Action_Reference_.exportLiteral(outfile, level, name_='ActionReferenceType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.append('type')
            self.type_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action_Reference':
            obj_ = ActionReferenceType.factory()
            obj_.build(child_)
            self.Action_Reference.append(obj_)
# end class ActionRelationshipType

class ActionReferenceType(GeneratedsSuper):
    """ActionReferenceType is intended to serve as a method for linking to
    actions.The action_id attribute refers to the id of the action
    being referenced."""
    subclass = None
    superclass = None
    def __init__(self, action_id=None):
        self.action_id = _cast(None, action_id)
        pass
    def factory(*args_, **kwargs_):
        if ActionReferenceType.subclass:
            return ActionReferenceType.subclass(*args_, **kwargs_)
        else:
            return ActionReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_action_id(self): return self.action_id
    def set_action_id(self, action_id): self.action_id = action_id
    def export(self, outfile, level, namespace_='cybox:', name_='ActionReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionReferenceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionReferenceType'):
        if self.action_id is not None and 'action_id' not in already_processed:
            already_processed.append('action_id')
            outfile.write(' action_id=%s' % (quote_attrib(self.action_id), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionReferenceType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionReferenceType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.action_id is not None and 'action_id' not in already_processed:
            already_processed.append('action_id')
            showIndent(outfile, level)
            outfile.write('action_id = %s,\n' % (self.action_id,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('action_id', node)
        if value is not None and 'action_id' not in already_processed:
            already_processed.append('action_id')
            self.action_id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ActionReferenceType

class ObjectType(GeneratedsSuper):
    """The ObjectType is a complex type representing the characteristics of
    a specific cyber-relevant object (e.g. a file, a registry key or
    a process). The id attribute specifies a unique id for this
    Object.The idref attribute specifies a unique id reference to an
    Object defined elsewhere.The type attribute specifies what kind
    of object this is.The object_state attribute enables description
    of the current state of the object.The "any" attribute enables
    the capture of custom attributes describing this Object."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, type_=None, id=None, object_state=None, Description=None, Defined_Object=None, Domain_specific_Object_Attributes=None, Custom_Attributes=None, Related_Objects=None, Defined_Effect=None, Discovery_Method=None, extensiontype_=None):
        self.idref = _cast(None, idref)
        self.type_ = _cast(None, type_)
        self.id = _cast(None, id)
        self.object_state = _cast(None, object_state)
        self.Description = Description
        self.Defined_Object = Defined_Object
        self.Domain_specific_Object_Attributes = Domain_specific_Object_Attributes
        self.Custom_Attributes = Custom_Attributes
        self.Related_Objects = Related_Objects
        self.Defined_Effect = Defined_Effect
        self.Discovery_Method = Discovery_Method
        self.anyAttributes_ = {}
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if ObjectType.subclass:
            return ObjectType.subclass(*args_, **kwargs_)
        else:
            return ObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Defined_Object(self): return self.Defined_Object
    def set_Defined_Object(self, Defined_Object): self.Defined_Object = Defined_Object
    def get_Domain_specific_Object_Attributes(self): return self.Domain_specific_Object_Attributes
    def set_Domain_specific_Object_Attributes(self, Domain_specific_Object_Attributes): self.Domain_specific_Object_Attributes = Domain_specific_Object_Attributes
    def get_Custom_Attributes(self): return self.Custom_Attributes
    def set_Custom_Attributes(self, Custom_Attributes): self.Custom_Attributes = Custom_Attributes
    def get_Related_Objects(self): return self.Related_Objects
    def set_Related_Objects(self, Related_Objects): self.Related_Objects = Related_Objects
    def get_Defined_Effect(self): return self.Defined_Effect
    def set_Defined_Effect(self, Defined_Effect): self.Defined_Effect = Defined_Effect
    def get_Discovery_Method(self): return self.Discovery_Method
    def set_Discovery_Method(self, Discovery_Method): self.Discovery_Method = Discovery_Method
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_type(self): return self.type_
    def set_type(self, type_): self.type_ = type_
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_object_state(self): return self.object_state
    def set_object_state(self, object_state): self.object_state = object_state
    def get_anyAttributes_(self): return self.anyAttributes_
    def set_anyAttributes_(self, anyAttributes_): self.anyAttributes_ = anyAttributes_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def export(self, outfile, level, namespace_='cybox:', name_='ObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObjectType'):
        unique_counter = 0
        for name, value in self.anyAttributes_.items():
            xsinamespaceprefix = 'xsi'
            xsinamespace1 = 'http://www.w3.org/2001/XMLSchema-instance'
            xsinamespace2 = '{%s}' % (xsinamespace1, )
            if name.startswith(xsinamespace2):
                name1 = name[len(xsinamespace2):]
                name2 = '%s:%s' % (xsinamespaceprefix, name1, )
                if name2 not in already_processed:
                    already_processed.append(name2)
                    outfile.write(' %s=%s' % (name2, quote_attrib(value), ))
            else:
                mo = re_.match(Namespace_extract_pat_, name)
                if mo is not None:
                    namespace, name = mo.group(1, 2)
                    if name not in already_processed:
                        already_processed.append(name)
                        if namespace == 'http://www.w3.org/XML/1998/namespace':
                            outfile.write(' %s=%s' % (name, quote_attrib(value), ))
                        else:
                            unique_counter += 1
                            outfile.write(' xmlns:yyy%d="%s"' % (unique_counter, namespace, ))
                            outfile.write(' yyy%d:%s=%s' % (unique_counter, name, quote_attrib(value), ))
                else:
                    if name not in already_processed:
                        already_processed.append(name)
                        outfile.write(' %s=%s' % (name, quote_attrib(value), ))
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.append('type_')
            outfile.write(' type=%s' % (quote_attrib(self.type_), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.append('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
        if self.object_state is not None and 'object_state' not in already_processed:
            already_processed.append('object_state')
            outfile.write(' object_state=%s' % (quote_attrib(self.object_state), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.append('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObjectType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Defined_Object is not None:
            self.Defined_Object.export(outfile, level, 'cybox:', name_='Defined_Object', pretty_print=pretty_print)
        if self.Domain_specific_Object_Attributes is not None:
            self.Domain_specific_Object_Attributes.export(outfile, level, 'cybox:', name_='Domain_specific_Object_Attributes', pretty_print=pretty_print)
        if self.Custom_Attributes is not None:
            self.Custom_Attributes.export(outfile, level, 'cybox:', name_='Custom_Attributes', pretty_print=pretty_print)
        if self.Related_Objects is not None:
            self.Related_Objects.export(outfile, level, 'cybox:', name_='Related_Objects', pretty_print=pretty_print)
        if self.Defined_Effect is not None:
            self.Defined_Effect.export(outfile, level, 'cybox:', name_='Defined_Effect', pretty_print=pretty_print)
        if self.Discovery_Method is not None:
            self.Discovery_Method.export(outfile, level, 'cybox:', name_='Discovery_Method', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Defined_Object is not None or
            self.Domain_specific_Object_Attributes is not None or
            self.Custom_Attributes is not None or
            self.Related_Objects is not None or
            self.Defined_Effect is not None or
            self.Discovery_Method is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.type_ is not None and 'type_' not in already_processed:
            already_processed.append('type_')
            showIndent(outfile, level)
            outfile.write('type_ = %s,\n' % (self.type_,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.append('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
        if self.object_state is not None and 'object_state' not in already_processed:
            already_processed.append('object_state')
            showIndent(outfile, level)
            outfile.write('object_state = %s,\n' % (self.object_state,))
        for name, value in self.anyAttributes_.items():
            showIndent(outfile, level)
            outfile.write('%s = "%s",\n' % (name, value,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description=model_.cybox_common_types_1_0.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.cybox_common_types_1_0.DefinedObjectType is not None:
            showIndent(outfile, level)
            outfile.write('cybox_common_types_1_0.DefinedObjectType=model_.cybox_common_types_1_0.DefinedObjectType(\n')
            self.cybox_common_types_1_0.DefinedObjectType.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.DomainSpecificObjectAttributesType is not None:
            showIndent(outfile, level)
            outfile.write('DomainSpecificObjectAttributesType=model_.DomainSpecificObjectAttributesType(\n')
            self.DomainSpecificObjectAttributesType.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Custom_Attributes is not None:
            showIndent(outfile, level)
            outfile.write('Custom_Attributes=model_.CustomAttributesType(\n')
            self.Custom_Attributes.exportLiteral(outfile, level, name_='Custom_Attributes')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Related_Objects is not None:
            showIndent(outfile, level)
            outfile.write('Related_Objects=model_.RelatedObjectsType(\n')
            self.Related_Objects.exportLiteral(outfile, level, name_='Related_Objects')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.DefinedEffectType is not None:
            showIndent(outfile, level)
            outfile.write('DefinedEffectType=model_.DefinedEffectType(\n')
            self.DefinedEffectType.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Discovery_Method is not None:
            showIndent(outfile, level)
            outfile.write('Discovery_Method=model_.cybox_common_types_1_0.MeasureSourceType(\n')
            self.Discovery_Method.exportLiteral(outfile, level, name_='Discovery_Method')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.append('idref')
            self.idref = value
        value = find_attr_value_('type', node)
        if value is not None and 'type' not in already_processed:
            already_processed.append('type')
            self.type_ = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.append('id')
            self.id = value
        value = find_attr_value_('object_state', node)
        if value is not None and 'object_state' not in already_processed:
            already_processed.append('object_state')
            self.object_state = value
        self.anyAttributes_ = {}
        for name, value in attrs.items():
            if name not in already_processed:
                self.anyAttributes_[name] = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.append('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common_types_1_0.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Defined_Object':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = getattr(__import__(objects_path + defined_objects.get(type_name_).get('binding_name'), globals(), fromlist=[type_name_]),type_name_)
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Defined_Object> element')
            self.set_Defined_Object(obj_)
        elif nodeName_ == 'Domain-specific_Object_Attributes':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                if type_name_ == 'AVClassificationsType':
                    exec("from maec_bundle_3_0 import AVClassificationsType") in globals()
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Domain_specific_Object_Attributes> element')
            self.set_Domain_specific_Object_Attributes(obj_)
        elif nodeName_ == 'Custom_Attributes':
            obj_ = CustomAttributesType.factory()
            obj_.build(child_)
            self.set_Custom_Attributes(obj_)
        elif nodeName_ == 'Related_Objects':
            obj_ = RelatedObjectsType.factory()
            obj_.build(child_)
            self.set_Related_Objects(obj_)
        elif nodeName_ == 'Defined_Effect':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Defined_Effect> element')
            self.set_Defined_Effect(obj_)
        elif nodeName_ == 'Discovery_Method':
            obj_ = cybox_common_types_1_0.MeasureSourceType.factory()
            obj_.build(child_)
            self.set_Discovery_Method(obj_)
# end class ObjectType

class DomainSpecificObjectAttributesType(GeneratedsSuper):
    """The DomainSpecificObjectAttributesType is an Abstract type
    placeholder within the CybOX schema enabling the inclusion of
    domain-specific metadata for an object through the use of a
    custom type defined as an extension of this base Abstract type.
    This enables domains utilizing CybOX such as malware analysis or
    forensics to incorporate non-generalized object metadata from
    their domains into CybOX objects."""
    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if DomainSpecificObjectAttributesType.subclass:
            return DomainSpecificObjectAttributesType.subclass(*args_, **kwargs_)
        else:
            return DomainSpecificObjectAttributesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def export(self, outfile, level, namespace_='cybox:', name_='DomainSpecificObjectAttributesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DomainSpecificObjectAttributesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DomainSpecificObjectAttributesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DomainSpecificObjectAttributesType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DomainSpecificObjectAttributesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DomainSpecificObjectAttributesType

class CustomAttributesType(GeneratedsSuper):
    """The CustomAttributesType enables the specification of a set of
    custom Object Attributes that may not be defined in existing
    Defined_Object schemas."""
    subclass = None
    superclass = None
    def __init__(self, Attribute=None):
        if Attribute is None:
            self.Attribute = []
        else:
            self.Attribute = Attribute
    def factory(*args_, **kwargs_):
        if CustomAttributesType.subclass:
            return CustomAttributesType.subclass(*args_, **kwargs_)
        else:
            return CustomAttributesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attribute(self): return self.Attribute
    def set_Attribute(self, Attribute): self.Attribute = Attribute
    def add_Attribute(self, value): self.Attribute.append(value)
    def insert_Attribute(self, index, value): self.Attribute[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='CustomAttributesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CustomAttributesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='CustomAttributesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='CustomAttributesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Attribute_ in self.Attribute:
            Attribute_.export(outfile, level, 'cybox:', name_='Attribute', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Attribute
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='CustomAttributesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Attribute=[\n')
        level += 1
        for Attribute_ in self.Attribute:
            showIndent(outfile, level)
            outfile.write('model_.Attribute(\n')
            Attribute_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attribute':
            obj_ = ActionPertinentObjectAttributeType.factory()
            obj_.build(child_)
            self.Attribute.append(obj_)
# end class CustomAttributesType

class RelatedObjectsType(GeneratedsSuper):
    """The RelatedObjectsType enables the identification and/or
    specification of Objects with relevant relationships with this
    Object."""
    subclass = None
    superclass = None
    def __init__(self, Related_Object=None):
        if Related_Object is None:
            self.Related_Object = []
        else:
            self.Related_Object = Related_Object
    def factory(*args_, **kwargs_):
        if RelatedObjectsType.subclass:
            return RelatedObjectsType.subclass(*args_, **kwargs_)
        else:
            return RelatedObjectsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Object(self): return self.Related_Object
    def set_Related_Object(self, Related_Object): self.Related_Object = Related_Object
    def add_Related_Object(self, value): self.Related_Object.append(value)
    def insert_Related_Object(self, index, value): self.Related_Object[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='RelatedObjectsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RelatedObjectsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='RelatedObjectsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='RelatedObjectsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Object_ in self.Related_Object:
            Related_Object_.export(outfile, level, 'cybox:', name_='Related_Object', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Related_Object
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='RelatedObjectsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Related_Object=[\n')
        level += 1
        for Related_Object_ in self.Related_Object:
            showIndent(outfile, level)
            outfile.write('model_.RelatedObjectType(\n')
            Related_Object_.exportLiteral(outfile, level, name_='RelatedObjectType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Object':
            obj_ = RelatedObjectType.factory()
            obj_.build(child_)
            self.Related_Object.append(obj_)
# end class RelatedObjectsType

class RelatedObjectType(ObjectType):
    """The RelatedObjectType enables the identification and/or
    specification of an Object with a relevant relationship with
    this Object.The Relationship attribute specifies the nature of
    the relationship between this Object and the Related_Object."""
    subclass = None
    superclass = ObjectType
    def __init__(self, idref=None, type_=None, id=None, object_state=None, Description=None, Defined_Object=None, Domain_specific_Object_Attributes=None, Custom_Attributes=None, Related_Objects=None, Defined_Effect=None, Discovery_Method=None, relationship=None):
        super(RelatedObjectType, self).__init__(idref, type_, id, object_state, Description, Defined_Object, Domain_specific_Object_Attributes, Custom_Attributes, Related_Objects, Defined_Effect, Discovery_Method, )
        self.relationship = _cast(None, relationship)
        pass
    def factory(*args_, **kwargs_):
        if RelatedObjectType.subclass:
            return RelatedObjectType.subclass(*args_, **kwargs_)
        else:
            return RelatedObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_relationship(self): return self.relationship
    def set_relationship(self, relationship): self.relationship = relationship
    def export(self, outfile, level, namespace_='cybox:', name_='RelatedObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='RelatedObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='RelatedObjectType'):
        super(RelatedObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='RelatedObjectType')
        if self.relationship is not None and 'relationship' not in already_processed:
            already_processed.append('relationship')
            outfile.write(' relationship=%s' % (quote_attrib(self.relationship), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='RelatedObjectType', fromsubclass_=False, pretty_print=True):
        super(RelatedObjectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
    def hasContent_(self):
        if (
            super(RelatedObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='RelatedObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.relationship is not None and 'relationship' not in already_processed:
            already_processed.append('relationship')
            showIndent(outfile, level)
            outfile.write('relationship = %s,\n' % (self.relationship,))
        super(RelatedObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(RelatedObjectType, self).exportLiteralChildren(outfile, level, name_)
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('relationship', node)
        if value is not None and 'relationship' not in already_processed:
            already_processed.append('relationship')
            self.relationship = value
        super(RelatedObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(RelatedObjectType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class RelatedObjectType

class DefinedEffectType(GeneratedsSuper):
    """The DefinedEffectType is an abstract placeholder for various
    predefined Object Effect types (e.g. DataReadEffect,
    ValuesEnumeratedEffect or StateChangeEffect) that can be
    instantiated in its place through extension of the
    DefinedEffectType. This mechanism enables the specification of a
    broad range of types of potential complex action effects on
    Objects. The set of Defined_Effect types (extending the
    DefinedEffectType) are maintained as part of the core CybOX
    schema.The effect_type attribute specifies the nature of the
    Defined Effect instantiated in the place of the Defined_Effect
    element."""
    subclass = None
    superclass = None
    def __init__(self, effect_type=None, extensiontype_=None):
        self.effect_type = _cast(None, effect_type)
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if DefinedEffectType.subclass:
            return DefinedEffectType.subclass(*args_, **kwargs_)
        else:
            return DefinedEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_effect_type(self): return self.effect_type
    def set_effect_type(self, effect_type): self.effect_type = effect_type
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def export(self, outfile, level, namespace_='cybox:', name_='DefinedEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DefinedEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DefinedEffectType'):
        if self.effect_type is not None and 'effect_type' not in already_processed:
            already_processed.append('effect_type')
            outfile.write(' effect_type=%s' % (quote_attrib(self.effect_type), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.append('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DefinedEffectType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DefinedEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.effect_type is not None and 'effect_type' not in already_processed:
            already_processed.append('effect_type')
            showIndent(outfile, level)
            outfile.write('effect_type = %s,\n' % (self.effect_type,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('effect_type', node)
        if value is not None and 'effect_type' not in already_processed:
            already_processed.append('effect_type')
            self.effect_type = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.append('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DefinedEffectType

class StateChangeEffectType(DefinedEffectType):
    """The StateChangeEffectType is intended as a generic way of
    characterizing the effects of actions upon objects where the
    some state of the object is changed."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Old_State=None, New_State=None):
        super(StateChangeEffectType, self).__init__(effect_type, )
        self.Old_State = Old_State
        self.New_State = New_State
    def factory(*args_, **kwargs_):
        if StateChangeEffectType.subclass:
            return StateChangeEffectType.subclass(*args_, **kwargs_)
        else:
            return StateChangeEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Old_State(self): return self.Old_State
    def set_Old_State(self, Old_State): self.Old_State = Old_State
    def get_New_State(self): return self.New_State
    def set_New_State(self, New_State): self.New_State = New_State
    def export(self, outfile, level, namespace_='cybox:', name_='StateChangeEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='StateChangeEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='StateChangeEffectType'):
        super(StateChangeEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='StateChangeEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='StateChangeEffectType', fromsubclass_=False, pretty_print=True):
        super(StateChangeEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Old_State is not None:
            self.Old_State.export(outfile, level, 'cybox:', name_='Old_State', pretty_print=pretty_print)
        if self.New_State is not None:
            self.New_State.export(outfile, level, 'cybox:', name_='New_State', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Old_State is not None or
            self.New_State is not None or
            super(StateChangeEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='StateChangeEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(StateChangeEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(StateChangeEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Old_State is not None:
            showIndent(outfile, level)
            outfile.write('Old_State=model_.StateType(\n')
            self.Old_State.exportLiteral(outfile, level, name_='Old_State')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.New_State is not None:
            showIndent(outfile, level)
            outfile.write('New_State=model_.StateType(\n')
            self.New_State.exportLiteral(outfile, level, name_='New_State')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(StateChangeEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Old_State':
            obj_ = StateType.factory()
            obj_.build(child_)
            self.set_Old_State(obj_)
        elif nodeName_ == 'New_State':
            obj_ = StateType.factory()
            obj_.build(child_)
            self.set_New_State(obj_)
        super(StateChangeEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class StateChangeEffectType

class StateType(GeneratedsSuper):
    """The StateType characterizes the state of an Object."""
    subclass = None
    superclass = None
    def __init__(self, Object=None, Defined_Object=None, Object_IDRef=None):
        self.Object = Object
        self.Defined_Object = Defined_Object
        self.Object_IDRef = Object_IDRef
    def factory(*args_, **kwargs_):
        if StateType.subclass:
            return StateType.subclass(*args_, **kwargs_)
        else:
            return StateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Object(self): return self.Object
    def set_Object(self, Object): self.Object = Object
    def get_Defined_Object(self): return self.Defined_Object
    def set_Defined_Object(self, Defined_Object): self.Defined_Object = Defined_Object
    def get_Object_IDRef(self): return self.Object_IDRef
    def set_Object_IDRef(self, Object_IDRef): self.Object_IDRef = Object_IDRef
    def export(self, outfile, level, namespace_='cybox:', name_='StateType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='StateType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='StateType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='StateType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Object is not None:
            self.Object.export(outfile, level, 'cybox:', name_='Object', pretty_print=pretty_print)
        if self.Defined_Object is not None:
            self.Defined_Object.export(outfile, level, 'cybox:', name_='Defined_Object', pretty_print=pretty_print)
        if self.Object_IDRef is not None:
            self.Object_IDRef.export(outfile, level, 'cybox:', name_='Object_IDRef', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Object is not None or
            self.Defined_Object is not None or
            self.Object_IDRef is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='StateType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Object is not None:
            showIndent(outfile, level)
            outfile.write('Object=model_.ObjectType(\n')
            self.Object.exportLiteral(outfile, level, name_='Object')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.cybox_common_types_1_0.DefinedObjectType is not None:
            showIndent(outfile, level)
            outfile.write('cybox_common_types_1_0.DefinedObjectType=model_.cybox_common_types_1_0.DefinedObjectType(\n')
            self.cybox_common_types_1_0.DefinedObjectType.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Object_IDRef is not None:
            showIndent(outfile, level)
            outfile.write('Object_IDRef=model_.xs_QName(\n')
            self.Object_IDRef.exportLiteral(outfile, level, name_='Object_IDRef')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Object':
            obj_ = ObjectType.factory()
            obj_.build(child_)
            self.set_Object(obj_)
        elif nodeName_ == 'Defined_Object':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Defined_Object> element')
            self.set_Defined_Object(obj_)
        elif nodeName_ == 'Object_IDRef':
            obj_ = xs_QName.factory()
            obj_.build(child_)
            self.set_Object_IDRef(obj_)
# end class StateType

class DataReadEffectType(DefinedEffectType):
    """The DataReadEffectType type is intended to characterize the effects
    of actions upon objects where some data is read, such as from a
    file or a pipe."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Data=None):
        super(DataReadEffectType, self).__init__(effect_type, )
        self.Data = Data
    def factory(*args_, **kwargs_):
        if DataReadEffectType.subclass:
            return DataReadEffectType.subclass(*args_, **kwargs_)
        else:
            return DataReadEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def export(self, outfile, level, namespace_='cybox:', name_='DataReadEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DataReadEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DataReadEffectType'):
        super(DataReadEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DataReadEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DataReadEffectType', fromsubclass_=False, pretty_print=True):
        super(DataReadEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data is not None:
            self.Data.export(outfile, level, 'cybox:', name_='Data', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Data is not None or
            super(DataReadEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DataReadEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DataReadEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DataReadEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Data is not None:
            showIndent(outfile, level)
            outfile.write('Data=model_.cybox_common_types_1_0.DataSegmentType(\n')
            self.Data.exportLiteral(outfile, level, name_='Data')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DataReadEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data':
            obj_ = cybox_common_types_1_0.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        super(DataReadEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class DataReadEffectType

class DataWrittenEffectType(DefinedEffectType):
    """The DataWrittenEffectType type is intended to characterize the
    effects of actions upon objects where some data is written, such
    as to a file or a pipe."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Data=None):
        super(DataWrittenEffectType, self).__init__(effect_type, )
        self.Data = Data
    def factory(*args_, **kwargs_):
        if DataWrittenEffectType.subclass:
            return DataWrittenEffectType.subclass(*args_, **kwargs_)
        else:
            return DataWrittenEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def export(self, outfile, level, namespace_='cybox:', name_='DataWrittenEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DataWrittenEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DataWrittenEffectType'):
        super(DataWrittenEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DataWrittenEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DataWrittenEffectType', fromsubclass_=False, pretty_print=True):
        super(DataWrittenEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data is not None:
            self.Data.export(outfile, level, 'cybox:', name_='Data', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Data is not None or
            super(DataWrittenEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DataWrittenEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DataWrittenEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DataWrittenEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Data is not None:
            showIndent(outfile, level)
            outfile.write('Data=model_.cybox_common_types_1_0.DataSegmentType(\n')
            self.Data.exportLiteral(outfile, level, name_='Data')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DataWrittenEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data':
            obj_ = cybox_common_types_1_0.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        super(DataWrittenEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class DataWrittenEffectType

class DataSentEffectType(DefinedEffectType):
    """The DataSentEffectType type is intended to characterize the effects
    of actions upon objects where some data is sent, such as a byte
    sequence on a socket."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Data=None):
        super(DataSentEffectType, self).__init__(effect_type, )
        self.Data = Data
    def factory(*args_, **kwargs_):
        if DataSentEffectType.subclass:
            return DataSentEffectType.subclass(*args_, **kwargs_)
        else:
            return DataSentEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def export(self, outfile, level, namespace_='cybox:', name_='DataSentEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DataSentEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DataSentEffectType'):
        super(DataSentEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DataSentEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DataSentEffectType', fromsubclass_=False, pretty_print=True):
        super(DataSentEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data is not None:
            self.Data.export(outfile, level, 'cybox:', name_='Data', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Data is not None or
            super(DataSentEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DataSentEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DataSentEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DataSentEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Data is not None:
            showIndent(outfile, level)
            outfile.write('Data=model_.cybox_common_types_1_0.DataSegmentType(\n')
            self.Data.exportLiteral(outfile, level, name_='Data')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DataSentEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data':
            obj_ = cybox_common_types_1_0.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        super(DataSentEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class DataSentEffectType

class DataReceivedEffectType(DefinedEffectType):
    """The DataReceivedEffectType type is intended to characterize the
    effects of actions upon objects where some data is received,
    such as a byte sequence on a socket."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Data=None):
        super(DataReceivedEffectType, self).__init__(effect_type, )
        self.Data = Data
    def factory(*args_, **kwargs_):
        if DataReceivedEffectType.subclass:
            return DataReceivedEffectType.subclass(*args_, **kwargs_)
        else:
            return DataReceivedEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def export(self, outfile, level, namespace_='cybox:', name_='DataReceivedEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DataReceivedEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='DataReceivedEffectType'):
        super(DataReceivedEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DataReceivedEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='DataReceivedEffectType', fromsubclass_=False, pretty_print=True):
        super(DataReceivedEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Data is not None:
            self.Data.export(outfile, level, 'cybox:', name_='Data', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Data is not None or
            super(DataReceivedEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DataReceivedEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DataReceivedEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DataReceivedEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Data is not None:
            showIndent(outfile, level)
            outfile.write('Data=model_.cybox_common_types_1_0.DataSegmentType(\n')
            self.Data.exportLiteral(outfile, level, name_='Data')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DataReceivedEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Data':
            obj_ = cybox_common_types_1_0.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        super(DataReceivedEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class DataReceivedEffectType

class PropertyReadEffectType(DefinedEffectType):
    """The PropertyReadEffectType type is intended to characterize the
    effects of actions upon objects where some specific property is
    read from an object, such as the current running state of a
    process."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Name=None, Value=None):
        super(PropertyReadEffectType, self).__init__(effect_type, )
        self.Name = Name
        self.Value = Value
    def factory(*args_, **kwargs_):
        if PropertyReadEffectType.subclass:
            return PropertyReadEffectType.subclass(*args_, **kwargs_)
        else:
            return PropertyReadEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def export(self, outfile, level, namespace_='cybox:', name_='PropertyReadEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PropertyReadEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PropertyReadEffectType'):
        super(PropertyReadEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='PropertyReadEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PropertyReadEffectType', fromsubclass_=False, pretty_print=True):
        super(PropertyReadEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sName>%s</%sName>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Name).encode(ExternalEncoding), input_name='Name'), 'cybox:', eol_))
        if self.Value is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Value).encode(ExternalEncoding), input_name='Value'), 'cybox:', eol_))
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Value is not None or
            super(PropertyReadEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PropertyReadEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(PropertyReadEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(PropertyReadEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Name is not None:
            showIndent(outfile, level)
            outfile.write('Name=%s,\n' % quote_python(self.Name).encode(ExternalEncoding))
        if self.Value is not None:
            showIndent(outfile, level)
            outfile.write('Value=%s,\n' % quote_python(self.Value).encode(ExternalEncoding))
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(PropertyReadEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            Name_ = child_.text
            Name_ = self.gds_validate_string(Name_, node, 'Name')
            self.Name = Name_
        elif nodeName_ == 'Value':
            Value_ = child_.text
            Value_ = self.gds_validate_string(Value_, node, 'Value')
            self.Value = Value_
        super(PropertyReadEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class PropertyReadEffectType

class PropertiesEnumeratedEffectType(DefinedEffectType):
    """The PropertiesEnumeratedEffectType type is intended to characterize
    the effects of actions upon objects where some properties of the
    object are enumerated, such as the startup parameters for a
    process."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Properties=None):
        super(PropertiesEnumeratedEffectType, self).__init__(effect_type, )
        self.Properties = Properties
    def factory(*args_, **kwargs_):
        if PropertiesEnumeratedEffectType.subclass:
            return PropertiesEnumeratedEffectType.subclass(*args_, **kwargs_)
        else:
            return PropertiesEnumeratedEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Properties(self): return self.Properties
    def set_Properties(self, Properties): self.Properties = Properties
    def export(self, outfile, level, namespace_='cybox:', name_='PropertiesEnumeratedEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PropertiesEnumeratedEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PropertiesEnumeratedEffectType'):
        super(PropertiesEnumeratedEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='PropertiesEnumeratedEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PropertiesEnumeratedEffectType', fromsubclass_=False, pretty_print=True):
        super(PropertiesEnumeratedEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Properties is not None:
            self.Properties.export(outfile, level, 'cybox:', name_='Properties', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Properties is not None or
            super(PropertiesEnumeratedEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PropertiesEnumeratedEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(PropertiesEnumeratedEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(PropertiesEnumeratedEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Properties is not None:
            showIndent(outfile, level)
            outfile.write('Properties=model_.PropertiesType(\n')
            self.Properties.exportLiteral(outfile, level, name_='Properties')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(PropertiesEnumeratedEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Properties':
            obj_ = PropertiesType.factory()
            obj_.build(child_)
            self.set_Properties(obj_)
        super(PropertiesEnumeratedEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class PropertiesEnumeratedEffectType

class PropertiesType(GeneratedsSuper):
    """The PropertiesType specifies the properties that were enumerated as
    a result of the action on the object."""
    subclass = None
    superclass = None
    def __init__(self, Property=None):
        if Property is None:
            self.Property = []
        else:
            self.Property = Property
    def factory(*args_, **kwargs_):
        if PropertiesType.subclass:
            return PropertiesType.subclass(*args_, **kwargs_)
        else:
            return PropertiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Property(self): return self.Property
    def set_Property(self, Property): self.Property = Property
    def add_Property(self, value): self.Property.append(value)
    def insert_Property(self, index, value): self.Property[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='PropertiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PropertiesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PropertiesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PropertiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Property_ in self.Property:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sProperty>%s</%sProperty>%s' % ('cybox:', self.gds_format_string(quote_xml(Property_).encode(ExternalEncoding), input_name='Property'), 'cybox:', eol_))
    def hasContent_(self):
        if (
            self.Property
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PropertiesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Property=[\n')
        level += 1
        for Property_ in self.Property:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(Property_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Property':
            Property_ = child_.text
            Property_ = self.gds_validate_string(Property_, node, 'Property')
            self.Property.append(Property_)
# end class PropertiesType

class ValuesEnumeratedEffectType(DefinedEffectType):
    """The ValuesEnumeratedEffectType type is intended to characterize the
    effects of actions upon objects where some values of the object
    are enumerated, such as the values of a registry key."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Values=None):
        super(ValuesEnumeratedEffectType, self).__init__(effect_type, )
        self.Values = Values
    def factory(*args_, **kwargs_):
        if ValuesEnumeratedEffectType.subclass:
            return ValuesEnumeratedEffectType.subclass(*args_, **kwargs_)
        else:
            return ValuesEnumeratedEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Values(self): return self.Values
    def set_Values(self, Values): self.Values = Values
    def export(self, outfile, level, namespace_='cybox:', name_='ValuesEnumeratedEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValuesEnumeratedEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ValuesEnumeratedEffectType'):
        super(ValuesEnumeratedEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='ValuesEnumeratedEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ValuesEnumeratedEffectType', fromsubclass_=False, pretty_print=True):
        super(ValuesEnumeratedEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Values is not None:
            self.Values.export(outfile, level, 'cybox:', name_='Values', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Values is not None or
            super(ValuesEnumeratedEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ValuesEnumeratedEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(ValuesEnumeratedEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(ValuesEnumeratedEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Values is not None:
            showIndent(outfile, level)
            outfile.write('Values=model_.ValuesType(\n')
            self.Values.exportLiteral(outfile, level, name_='Values')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ValuesEnumeratedEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Values':
            obj_ = ValuesType.factory()
            obj_.build(child_)
            self.set_Values(obj_)
        super(ValuesEnumeratedEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class ValuesEnumeratedEffectType

class ValuesType(GeneratedsSuper):
    """The ValuesType specifies the values that were enumerated as a result
    of the action on the object."""
    subclass = None
    superclass = None
    def __init__(self, Value=None):
        if Value is None:
            self.Value = []
        else:
            self.Value = Value
    def factory(*args_, **kwargs_):
        if ValuesType.subclass:
            return ValuesType.subclass(*args_, **kwargs_)
        else:
            return ValuesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def add_Value(self, value): self.Value.append(value)
    def insert_Value(self, index, value): self.Value[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='ValuesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ValuesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ValuesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ValuesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Value_ in self.Value:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sValue>%s</%sValue>%s' % ('cybox:', self.gds_format_string(quote_xml(Value_).encode(ExternalEncoding), input_name='Value'), 'cybox:', eol_))
    def hasContent_(self):
        if (
            self.Value
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ValuesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Value=[\n')
        level += 1
        for Value_ in self.Value:
            showIndent(outfile, level)
            outfile.write('%s,\n' % quote_python(Value_).encode(ExternalEncoding))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Value':
            Value_ = child_.text
            Value_ = self.gds_validate_string(Value_, node, 'Value')
            self.Value.append(Value_)
# end class ValuesType

class SendControlCodeEffectType(DefinedEffectType):
    """The SendControlCodeEffectType is intended to characterize the
    effects of actions upon objects where some control code, or
    other control-oriented communication signal, is sent to the
    object. For example, an action may send a control code to change
    the running state of a process."""
    subclass = None
    superclass = DefinedEffectType
    def __init__(self, effect_type=None, Control_Code=None):
        super(SendControlCodeEffectType, self).__init__(effect_type, )
        self.Control_Code = Control_Code
    def factory(*args_, **kwargs_):
        if SendControlCodeEffectType.subclass:
            return SendControlCodeEffectType.subclass(*args_, **kwargs_)
        else:
            return SendControlCodeEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Control_Code(self): return self.Control_Code
    def set_Control_Code(self, Control_Code): self.Control_Code = Control_Code
    def export(self, outfile, level, namespace_='cybox:', name_='SendControlCodeEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='SendControlCodeEffectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='SendControlCodeEffectType'):
        super(SendControlCodeEffectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='SendControlCodeEffectType')
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='SendControlCodeEffectType', fromsubclass_=False, pretty_print=True):
        super(SendControlCodeEffectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Control_Code is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sControl_Code>%s</%sControl_Code>%s' % ('cybox:', self.gds_format_string(quote_xml(self.Control_Code).encode(ExternalEncoding), input_name='Control_Code'), 'cybox:', eol_))
    def hasContent_(self):
        if (
            self.Control_Code is not None or
            super(SendControlCodeEffectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='SendControlCodeEffectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(SendControlCodeEffectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(SendControlCodeEffectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Control_Code is not None:
            showIndent(outfile, level)
            outfile.write('Control_Code=%s,\n' % quote_python(self.Control_Code).encode(ExternalEncoding))
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(SendControlCodeEffectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Control_Code':
            Control_Code_ = child_.text
            Control_Code_ = self.gds_validate_string(Control_Code_, node, 'Control_Code')
            self.Control_Code = Control_Code_
        super(SendControlCodeEffectType, self).buildChildren(child_, node, nodeName_, True)
# end class SendControlCodeEffectType

class ObservableCompositionType(GeneratedsSuper):
    """The ObservablesCompositionType enables the specification of higher-
    order composite observables composed of logical combinations of
    other observables.The operator attribute enables the
    specification of complex compositional cyber observables by
    providing logical operators for defining interrelationships
    between constituent cyber observables defined utilizing the
    recursive Observable element."""
    subclass = None
    superclass = None
    def __init__(self, operator=None, Observable=None):
        self.operator = _cast(None, operator)
        if Observable is None:
            self.Observable = []
        else:
            self.Observable = Observable
    def factory(*args_, **kwargs_):
        if ObservableCompositionType.subclass:
            return ObservableCompositionType.subclass(*args_, **kwargs_)
        else:
            return ObservableCompositionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Observable(self): return self.Observable
    def set_Observable(self, Observable): self.Observable = Observable
    def add_Observable(self, value): self.Observable.append(value)
    def insert_Observable(self, index, value): self.Observable[index] = value
    def get_operator(self): return self.operator
    def set_operator(self, operator): self.operator = operator
    def export(self, outfile, level, namespace_='cybox:', name_='ObservableCompositionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObservableCompositionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObservableCompositionType'):
        if self.operator is not None and 'operator' not in already_processed:
            already_processed.append('operator')
            outfile.write(' operator=%s' % (quote_attrib(self.operator), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObservableCompositionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Observable_ in self.Observable:
            Observable_.export(outfile, level, 'cybox:', name_='Observable', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Observable
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ObservableCompositionType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.operator is not None and 'operator' not in already_processed:
            already_processed.append('operator')
            showIndent(outfile, level)
            outfile.write('operator = %s,\n' % (self.operator,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Observable=[\n')
        level += 1
        for Observable_ in self.Observable:
            showIndent(outfile, level)
            outfile.write('model_.ObservableType(\n')
            Observable_.exportLiteral(outfile, level, name_='ObservableType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('operator', node)
        if value is not None and 'operator' not in already_processed:
            already_processed.append('operator')
            self.operator = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Observable':
            obj_ = ObservableType.factory()
            obj_.build(child_)
            self.Observable.append(obj_)
# end class ObservableCompositionType

class PoolsType(GeneratedsSuper):
    """The PoolsType enables the description of Events, Actions, Objects
    and Attributes in a space-efficient pooled manner with the
    actual Observable structures defined in the CybOX schema
    containing references to the pooled elements. This reduces
    redundancy caused when identical observable elements occur
    multiple times within a set of defined Observables."""
    subclass = None
    superclass = None
    def __init__(self, Event_Pool=None, Action_Pool=None, Object_Pool=None, Attribute_Pool=None):
        self.Event_Pool = Event_Pool
        self.Action_Pool = Action_Pool
        self.Object_Pool = Object_Pool
        self.Attribute_Pool = Attribute_Pool
    def factory(*args_, **kwargs_):
        if PoolsType.subclass:
            return PoolsType.subclass(*args_, **kwargs_)
        else:
            return PoolsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Event_Pool(self): return self.Event_Pool
    def set_Event_Pool(self, Event_Pool): self.Event_Pool = Event_Pool
    def get_Action_Pool(self): return self.Action_Pool
    def set_Action_Pool(self, Action_Pool): self.Action_Pool = Action_Pool
    def get_Object_Pool(self): return self.Object_Pool
    def set_Object_Pool(self, Object_Pool): self.Object_Pool = Object_Pool
    def get_Attribute_Pool(self): return self.Attribute_Pool
    def set_Attribute_Pool(self, Attribute_Pool): self.Attribute_Pool = Attribute_Pool
    def export(self, outfile, level, namespace_='cybox:', name_='PoolsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PoolsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='PoolsType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='PoolsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Event_Pool is not None:
            self.Event_Pool.export(outfile, level, 'cybox:', name_='Event_Pool', pretty_print=pretty_print)
        if self.Action_Pool is not None:
            self.Action_Pool.export(outfile, level, 'cybox:', name_='Action_Pool', pretty_print=pretty_print)
        if self.Object_Pool is not None:
            self.Object_Pool.export(outfile, level, 'cybox:', name_='Object_Pool', pretty_print=pretty_print)
        if self.Attribute_Pool is not None:
            self.Attribute_Pool.export(outfile, level, 'cybox:', name_='Attribute_Pool', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Event_Pool is not None or
            self.Action_Pool is not None or
            self.Object_Pool is not None or
            self.Attribute_Pool is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PoolsType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Event_Pool is not None:
            showIndent(outfile, level)
            outfile.write('Event_Pool=model_.EventPoolType(\n')
            self.Event_Pool.exportLiteral(outfile, level, name_='Event_Pool')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Action_Pool is not None:
            showIndent(outfile, level)
            outfile.write('Action_Pool=model_.ActionPoolType(\n')
            self.Action_Pool.exportLiteral(outfile, level, name_='Action_Pool')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Object_Pool is not None:
            showIndent(outfile, level)
            outfile.write('Object_Pool=model_.ObjectPoolType(\n')
            self.Object_Pool.exportLiteral(outfile, level, name_='Object_Pool')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Attribute_Pool is not None:
            showIndent(outfile, level)
            outfile.write('Attribute_Pool=model_.AttributePoolType(\n')
            self.Attribute_Pool.exportLiteral(outfile, level, name_='Attribute_Pool')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Event_Pool':
            obj_ = EventPoolType.factory()
            obj_.build(child_)
            self.set_Event_Pool(obj_)
        elif nodeName_ == 'Action_Pool':
            obj_ = ActionPoolType.factory()
            obj_.build(child_)
            self.set_Action_Pool(obj_)
        elif nodeName_ == 'Object_Pool':
            obj_ = ObjectPoolType.factory()
            obj_.build(child_)
            self.set_Object_Pool(obj_)
        elif nodeName_ == 'Attribute_Pool':
            obj_ = AttributePoolType.factory()
            obj_.build(child_)
            self.set_Attribute_Pool(obj_)
# end class PoolsType

class EventPoolType(GeneratedsSuper):
    """The EventPoolType enables the description of CybOX Events in a
    space-efficient pooled manner with the actual Observable
    structures defined in the CybOX schema containing references to
    the pooled Event elements. This reduces redundancy caused when
    identical Events occur multiple times within a set of defined
    Observables."""
    subclass = None
    superclass = None
    def __init__(self, Event=None):
        if Event is None:
            self.Event = []
        else:
            self.Event = Event
    def factory(*args_, **kwargs_):
        if EventPoolType.subclass:
            return EventPoolType.subclass(*args_, **kwargs_)
        else:
            return EventPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Event(self): return self.Event
    def set_Event(self, Event): self.Event = Event
    def add_Event(self, value): self.Event.append(value)
    def insert_Event(self, index, value): self.Event[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='EventPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='EventPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='EventPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='EventPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Event_ in self.Event:
            Event_.export(outfile, level, 'cybox:', name_='Event', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Event
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='EventPoolType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Event=[\n')
        level += 1
        for Event_ in self.Event:
            showIndent(outfile, level)
            outfile.write('model_.EventType(\n')
            Event_.exportLiteral(outfile, level, name_='EventType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Event':
            obj_ = EventType.factory()
            obj_.build(child_)
            self.Event.append(obj_)
# end class EventPoolType

class ActionPoolType(GeneratedsSuper):
    """The ActionPoolType enables the description of CybOX Actions in a
    space-efficient pooled manner with the actual Observable
    structures defined in the CybOX schema containing references to
    the pooled Action elements. This reduces redundancy caused when
    identical Actions occur multiple times within a set of defined
    Observables."""
    subclass = None
    superclass = None
    def __init__(self, Action=None):
        if Action is None:
            self.Action = []
        else:
            self.Action = Action
    def factory(*args_, **kwargs_):
        if ActionPoolType.subclass:
            return ActionPoolType.subclass(*args_, **kwargs_)
        else:
            return ActionPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action(self): return self.Action
    def set_Action(self, Action): self.Action = Action
    def add_Action(self, value): self.Action.append(value)
    def insert_Action(self, index, value): self.Action[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='ActionPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ActionPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ActionPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ActionPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_ in self.Action:
            Action_.export(outfile, level, 'cybox:', name_='Action', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Action
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ActionPoolType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Action=[\n')
        level += 1
        for Action_ in self.Action:
            showIndent(outfile, level)
            outfile.write('model_.ActionType(\n')
            Action_.exportLiteral(outfile, level, name_='ActionType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action':
            obj_ = ActionType.factory()
            obj_.build(child_)
            self.Action.append(obj_)
# end class ActionPoolType

class ObjectPoolType(GeneratedsSuper):
    """The ObjectPoolType enables the description of CybOX Objects in a
    space-efficient pooled manner with the actual Observable
    structures defined in the CybOX schema containing references to
    the pooled Object elements. This reduces redundancy caused when
    identical Objects occur multiple times within a set of defined
    Observables."""
    subclass = None
    superclass = None
    def __init__(self, Object=None):
        if Object is None:
            self.Object = []
        else:
            self.Object = Object
    def factory(*args_, **kwargs_):
        if ObjectPoolType.subclass:
            return ObjectPoolType.subclass(*args_, **kwargs_)
        else:
            return ObjectPoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Object(self): return self.Object
    def set_Object(self, Object): self.Object = Object
    def add_Object(self, value): self.Object.append(value)
    def insert_Object(self, index, value): self.Object[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='ObjectPoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObjectPoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObjectPoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObjectPoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Object_ in self.Object:
            Object_.export(outfile, level, 'cybox:', name_='Object', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Object
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ObjectPoolType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Object=[\n')
        level += 1
        for Object_ in self.Object:
            showIndent(outfile, level)
            outfile.write('model_.ObjectType(\n')
            Object_.exportLiteral(outfile, level, name_='ObjectType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Object':
            obj_ = ObjectType.factory()
            obj_.build(child_)
            self.Object.append(obj_)
# end class ObjectPoolType

class AttributePoolType(GeneratedsSuper):
    """The AttributePoolType enables the description of CybOX Attributes in
    a space-efficient pooled manner with the actual Observable
    structures defined in the CybOX schema containing references to
    the pooled Attributes elements. This reduces redundancy caused
    when identical Attributes occur multiple times within a set of
    defined Observables."""
    subclass = None
    superclass = None
    def __init__(self, Attribute=None):
        if Attribute is None:
            self.Attribute = []
        else:
            self.Attribute = Attribute
    def factory(*args_, **kwargs_):
        if AttributePoolType.subclass:
            return AttributePoolType.subclass(*args_, **kwargs_)
        else:
            return AttributePoolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attribute(self): return self.Attribute
    def set_Attribute(self, Attribute): self.Attribute = Attribute
    def add_Attribute(self, value): self.Attribute.append(value)
    def insert_Attribute(self, index, value): self.Attribute[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='AttributePoolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AttributePoolType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='AttributePoolType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='AttributePoolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Attribute_ in self.Attribute:
            Attribute_.export(outfile, level, 'cybox:', name_='Attribute', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Attribute
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AttributePoolType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Attribute=[\n')
        level += 1
        for Attribute_ in self.Attribute:
            showIndent(outfile, level)
            outfile.write('model_.AttributeType(\n')
            Attribute_.exportLiteral(outfile, level, name_='AttributeType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attribute':
            obj_ = ActionPertinentObjectAttributeType.factory()
            obj_.build(child_)
            self.Attribute.append(obj_)
# end class AttributePoolType

class ObfuscationTechniquesType(GeneratedsSuper):
    """The ObfuscationTechniquesType enables the description of a set of
    potential techniques an attacker could leverage to obfuscate the
    observability of this Observable."""
    subclass = None
    superclass = None
    def __init__(self, Obfuscation_Technique=None):
        if Obfuscation_Technique is None:
            self.Obfuscation_Technique = []
        else:
            self.Obfuscation_Technique = Obfuscation_Technique
    def factory(*args_, **kwargs_):
        if ObfuscationTechniquesType.subclass:
            return ObfuscationTechniquesType.subclass(*args_, **kwargs_)
        else:
            return ObfuscationTechniquesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Obfuscation_Technique(self): return self.Obfuscation_Technique
    def set_Obfuscation_Technique(self, Obfuscation_Technique): self.Obfuscation_Technique = Obfuscation_Technique
    def add_Obfuscation_Technique(self, value): self.Obfuscation_Technique.append(value)
    def insert_Obfuscation_Technique(self, index, value): self.Obfuscation_Technique[index] = value
    def export(self, outfile, level, namespace_='cybox:', name_='ObfuscationTechniquesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObfuscationTechniquesType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObfuscationTechniquesType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObfuscationTechniquesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Obfuscation_Technique_ in self.Obfuscation_Technique:
            Obfuscation_Technique_.export(outfile, level, 'cybox:', name_='Obfuscation_Technique', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Obfuscation_Technique
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ObfuscationTechniquesType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Obfuscation_Technique=[\n')
        level += 1
        for Obfuscation_Technique_ in self.Obfuscation_Technique:
            showIndent(outfile, level)
            outfile.write('model_.ObfuscationTechniqueType(\n')
            Obfuscation_Technique_.exportLiteral(outfile, level, name_='ObfuscationTechniqueType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Obfuscation_Technique':
            obj_ = ObfuscationTechniqueType.factory()
            obj_.build(child_)
            self.Obfuscation_Technique.append(obj_)
# end class ObfuscationTechniquesType

class ObfuscationTechniqueType(GeneratedsSuper):
    """The ObfuscationTechniqueType enables the description of a single
    potential technique an attacker could leverage to obfuscate the
    observability of this Observable."""
    subclass = None
    superclass = None
    def __init__(self, Description=None, Observables=None):
        self.Description = Description
        self.Observables = Observables
    def factory(*args_, **kwargs_):
        if ObfuscationTechniqueType.subclass:
            return ObfuscationTechniqueType.subclass(*args_, **kwargs_)
        else:
            return ObfuscationTechniqueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Observables(self): return self.Observables
    def set_Observables(self, Observables): self.Observables = Observables
    def export(self, outfile, level, namespace_='cybox:', name_='ObfuscationTechniqueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ObfuscationTechniqueType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='ObfuscationTechniqueType'):
        pass
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='ObfuscationTechniqueType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(outfile, level, 'cybox:', name_='Description', pretty_print=pretty_print)
        if self.Observables is not None:
            self.Observables.export(outfile, level, 'cybox:', name_='Observables', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Observables is not None
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='ObfuscationTechniqueType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Description is not None:
            showIndent(outfile, level)
            outfile.write('Description=model_.cybox_common_types_1_0.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Observables is not None:
            showIndent(outfile, level)
            outfile.write('Observables=model_.ObservablesType(\n')
            self.Observables.exportLiteral(outfile, level, name_='Observables')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = cybox_common_types_1_0.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Observables':
            obj_ = ObservablesType.factory()
            obj_.build(child_)
            self.set_Observables(obj_)
# end class ObfuscationTechniqueType

class AttributeType(cybox_common_types_1_0.BaseObjectAttributeType):
    """The AttibuteType is a complex type representing the specification of
    a single Object Attribute.The name attribute specifies a name
    for this attribute."""
    subclass = None
    superclass = cybox_common_types_1_0.BaseObjectAttributeType
    def __init__(self, end_range=None, pattern_type=None, has_changed=None, value_set=None, datatype='String', refanging_transform=None, refanging_transform_type=None, appears_random=None, trend=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, obfuscation_algorithm_ref=None, start_range=None, idref=None, is_defanged=None, id=None, condition=None, name=None, valueOf_=None):
        super(AttributeType, self).__init__(end_range, pattern_type, has_changed, value_set, datatype, refanging_transform, refanging_transform_type, appears_random, trend, defanging_algorithm_ref, is_obfuscated, regex_syntax, obfuscation_algorithm_ref, start_range, idref, is_defanged, id, condition, valueOf_, )
        self.name = _cast(None, name)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if AttributeType.subclass:
            return AttributeType.subclass(*args_, **kwargs_)
        else:
            return AttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='cybox:', name_='AttributeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AttributeType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='AttributeType'):
        super(AttributeType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AttributeType')
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            outfile.write(' name=%s' % (self.gds_format_string(quote_attrib(self.name).encode(ExternalEncoding), input_name='name'), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='AttributeType', fromsubclass_=False, pretty_print=True):
        super(AttributeType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(AttributeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AttributeType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.name is not None and 'name' not in already_processed:
            already_processed.append('name')
            showIndent(outfile, level)
            outfile.write('name = "%s",\n' % (self.name,))
        super(AttributeType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(AttributeType, self).exportLiteralChildren(outfile, level, name_)
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.append('name')
            self.name = value
        super(AttributeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class AttributeType

class AssociatedObjectType(ObjectType):
    """The AssociatedObjectType is a complex type representing the
    characterization of a cyber observable Object associated with a
    given cyber observable Action.The association_type attribute
    specifies the kind of association this Object holds for this
    Action."""
    subclass = None
    superclass = ObjectType
    def __init__(self, idref=None, type_=None, id=None, object_state=None, Description=None, Defined_Object=None, Domain_specific_Object_Attributes=None, Custom_Attributes=None, Related_Objects=None, Defined_Effect=None, Discovery_Method=None, association_type=None, ActionPertinentObjectAttributes=None):
        super(AssociatedObjectType, self).__init__(idref, type_, id, object_state, Description, Defined_Object, Domain_specific_Object_Attributes, Custom_Attributes, Related_Objects, Defined_Effect, Discovery_Method, )
        self.association_type = _cast(None, association_type)
        self.ActionPertinentObjectAttributes = ActionPertinentObjectAttributes
    def factory(*args_, **kwargs_):
        if AssociatedObjectType.subclass:
            return AssociatedObjectType.subclass(*args_, **kwargs_)
        else:
            return AssociatedObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ActionPertinentObjectAttributes(self): return self.ActionPertinentObjectAttributes
    def set_ActionPertinentObjectAttributes(self, ActionPertinentObjectAttributes): self.ActionPertinentObjectAttributes = ActionPertinentObjectAttributes
    def get_association_type(self): return self.association_type
    def set_association_type(self, association_type): self.association_type = association_type
    def export(self, outfile, level, namespace_='cybox:', name_='AssociatedObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='AssociatedObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='cybox:', name_='AssociatedObjectType'):
        super(AssociatedObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='AssociatedObjectType')
        if self.association_type is not None and 'association_type' not in already_processed:
            already_processed.append('association_type')
            outfile.write(' association_type=%s' % (quote_attrib(self.association_type), ))
    def exportChildren(self, outfile, level, namespace_='cybox:', name_='AssociatedObjectType', fromsubclass_=False, pretty_print=True):
        super(AssociatedObjectType, self).exportChildren(outfile, level, 'cybox:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ActionPertinentObjectAttributes is not None:
            self.ActionPertinentObjectAttributes.export(outfile, level, 'cybox:', name_='ActionPertinentObjectAttributes', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.ActionPertinentObjectAttributes is not None or
            super(AssociatedObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='AssociatedObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.association_type is not None and 'association_type' not in already_processed:
            already_processed.append('association_type')
            showIndent(outfile, level)
            outfile.write('association_type = %s,\n' % (self.association_type,))
        super(AssociatedObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(AssociatedObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.ActionPertinentObjectAttributes is not None:
            showIndent(outfile, level)
            outfile.write('ActionPertinentObjectAttributes=model_.ActionPertinentObjectAttributesType(\n')
            self.ActionPertinentObjectAttributes.exportLiteral(outfile, level, name_='ActionPertinentObjectAttributes')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('association_type', node)
        if value is not None and 'association_type' not in already_processed:
            already_processed.append('association_type')
            self.association_type = value
        super(AssociatedObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ActionPertinentObjectAttributes':
            obj_ = ActionPertinentObjectAttributesType.factory()
            obj_.build(child_)
            self.set_ActionPertinentObjectAttributes(obj_)
        super(AssociatedObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class AssociatedObjectType

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Observables'
        rootClass = ObservablesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    #doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_=rootTag,
    #    namespacedef_='',
    #    pretty_print=True)
    return rootObj

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Observables'
        rootClass = Observables
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Observables",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Observables'
        rootClass = ObservablesType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from cybox_core import *\n\n')
    sys.stdout.write('import cybox_core as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "ObservablesType",
    "ObservableType",
    "StatefulMeasureType",
    "EventType",
    "FrequencyType",
    "ActionsType",
    "ActionType",
    "ActionAliasesType",
    "ActionArgumentsType",
    "ActionArgumentType",
    "AssociatedObjectsType",
    "AssociatedObjectType",
    "ActionPertinentObjectAttributesType",
    "ActionPertinentObjectAttributeType",
    "RelationshipsType",
    "ActionRelationshipType",
    "ActionReferenceType",
    "ObjectType",
    "DomainSpecificObjectAttributesType",
    "CustomAttributesType",
    "RelatedObjectsType",
    "RelatedObjectType",
    "DefinedEffectType",
    "StateChangeEffectType",
    "StateType",
    "DataReadEffectType",
    "DataWrittenEffectType",
    "DataSentEffectType",
    "DataReceivedEffectType",
    "PropertyReadEffectType",
    "PropertiesEnumeratedEffectType",
    "PropertiesType",
    "ValuesEnumeratedEffectType",
    "ValuesType",
    "SendControlCodeEffectType",
    "AttributeType",
    "ObservableCompositionType",
    "PoolsType",
    "EventPoolType",
    "ActionPoolType",
    "ObjectPoolType",
    "AttributePoolType",
    "ObfuscationTechniquesType",
    "ObfuscationTechniqueType"
    ]
