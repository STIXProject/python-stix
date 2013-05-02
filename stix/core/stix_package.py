# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix_header import STIXHeader
from stix.indicator import Indicator
import stix.bindings.stix_core as stix_core_binding
from lxml import etree
from StringIO import StringIO

class STIXPackage(stix.Entity):
    '''
    classdocs
    '''

    def __init__(self, id_=None, idref_=None, stix_header=None, indicators=None, incidents=None, ttps=None, campaigns=None, coas=None, threat_actors=None, exploit_targets=None):
        '''
        Constructor
        '''
        self.id_ = id_ if id_ else stix.utils.create_id() 
        self.idref_ = idref_
        self.version = '1.0-draft2'
        self.indicators = indicators
        self.stix_header = stix_header
    
    @property
    def stix_header(self):
        return self._stix_header
    
    @stix_header.setter
    def stix_header(self, value):
        if value and not isinstance(value, STIXHeader):
            raise ValueError('value must be instance of STIXHeader')
        
        self._stix_header = value
    
    @property
    def indicators(self):
        return self._indicators
    
    @indicators.setter
    def indicators(self, valuelist):
        self._indicators = [] # initialize
        
        if valuelist:   
            for value in valuelist:
                self.add_indicator(value)
        
    def add_indicator(self, indicator):
        if indicator and not isinstance(indicator, Indicator):
            raise ValueError('indicator must be instance of stix.indicator.Indicator')
    
        self.indicators.append(indicator)
        
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = stix_core_binding.STIXType()
        
        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref_)
        return_obj.set_version(self.version)
        
        if self.stix_header:
            return_obj.set_STIXHeader(self.stix_header.to_obj())
        
        if self.indicators:
            indicators_obj = stix_core_binding.IndicatorsType()
            
            for indicator in self.indicators:
                indicators_obj.add_Indicator(indicator.to_obj())
            
            return_obj.set_Indicators(indicators_obj)
            
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.id_:
            return_dict['id'] = self.id_
            
        return_dict['version'] = self.version
        
        if self.idref_:
            return_dict['idref'] = self.idref_
        
        if self.stix_header:
            return_dict['stix_header'] = self.stix_header.to_dict()
            
        if self.indicators:
            for indicator in self.indicators:
                return_dict.setdefault('indicators', []).append(indicator.to_dict())
        
        return return_dict
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            return_obj = cls()
            
        return_obj.id_ = obj.get_id()
        return_obj.idref_ = obj.get_idref()
        return_obj.version = obj.get_version()
        return_obj.stix_header = STIXHeader.from_obj(obj.get_STIXHeader())
        
        if obj.get_Indicators():
            indicators_obj = obj.get_Indicators()
            if indicators_obj.get_Indicator():
                for indicator_obj in indicators_obj.get_Indicator():
                    return_obj.add_indicator(Indicator.from_obj(indicator_obj))
        
        return return_obj
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not return_obj:
            return_obj = cls()
        
        return_obj.id_ = dict_repr.get('id', None)
        return_obj.idref_ = dict_repr.get('idref', None)
        return_obj.version = dict_repr.get('version', None)
        
        header_dict = dict_repr.get('stix_header', None)
        return_obj.stix_header = STIXHeader.from_dict(header_dict)
        
        indicators = dict_repr.get('indicators', [])
        for indicator_dict in indicators:
            return_obj.add_indicator(Indicator.from_dict(indicator_dict))
            
        return return_obj
    
    @classmethod
    def from_xml(cls, xml_file):
        '''
        Returns a tuple of (api_object, binding_object).
        Parameters:
        xml_file - either a filename or a stream object
        '''
        
        if isinstance(xml_file, basestring):
            f = open(xml_file, "rb")
        else:
            f = xml_file
        
        doc = etree.parse(f)
        stix_package_obj = stix_core_binding.STIXType()
        stix_package_obj.build(doc.getroot())
        stix_package = STIXPackage().from_obj(stix_package_obj)
        
        return (stix_package, stix_package_obj)
            
    
    def to_xml(self):
        '''Overrides the stix.to_xml() method. Namespace definitions are hardcoded--this is only temporary'''
        s = StringIO()
        self.to_obj().export(s, 0, name_="STIX_Package",
                             namespacedef_='xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\
                                            xmlns:WinRegistryKeyObj="http://cybox.mitre.org/objects#WinRegistryKeyObject"\
                                            xmlns:WinMutexObj="http://cybox.mitre.org/objects#WinMutexObject"\
                                            xmlns:campaign="http://stix.mitre.org/Campaign"\
                                            xmlns:PortObj="http://cybox.mitre.org/objects#PortObject"\
                                            xmlns:CodeObj="http://cybox.mitre.org/objects#CodeObject"\
                                            xmlns:UnixPipeObj="http://cybox.mitre.org/objects#UnixPipeObject"\
                                            xmlns:ProcessObj="http://cybox.mitre.org/objects#ProcessObject"\
                                            xmlns:xlink="http://www.w3.org/1999/xlink"\
                                            xmlns:COA="http://stix.mitre.org/COA"\
                                            xmlns:WinProcessObj="http://cybox.mitre.org/objects#WinProcessObject"\
                                            xmlns:WinEventLogObj="http://cybox.mitre.org/objects#WinEventLogObject"\
                                            xmlns:UserSessionObj="http://cybox.mitre.org/objects#UserSessionObject"\
                                            xmlns:xs="http://www.w3.org/2001/XMLSchema"\
                                            xmlns:LibraryObj="http://cybox.mitre.org/objects#LibraryObject"\
                                            xmlns:sch="http://purl.oclc.org/dsdl/schematron"\
                                            xmlns:WinSystemObj="http://cybox.mitre.org/XMLSchema/objects#WinSystemObject"\
                                            xmlns:indicator="http://stix.mitre.org/Indicator"\
                                            xmlns:DNSCacheObj="http://cybox.mitre.org/objects#DNSCacheObject"\
                                            xmlns:maecBundle="http://maec.mitre.org/XMLSchema/maec-bundle-3"\
                                            xmlns:AccountObj="http://cybox.mitre.org/objects#AccountObject"\
                                            xmlns:ProductObj="http://cybox.mitre.org/objects#ProductObject"\
                                            xmlns:stixCommon="http://stix.mitre.org/Common"\
                                            xmlns:WinUserAccountObj="http://cybox.mitre.org/objects#WinUserAccountObject"\
                                            xmlns:X509CertificateObj="http://cybox.mitre.org/objects#X509CertificateObject"\
                                            xmlns:GUIDialogboxObj="http://cybox.mitre.org/objects#GUIDialogboxObject"\
                                            xmlns:capec="http://capec.mitre.org/capec_v1"\
                                            xmlns:Incident="http://stix.mitre.org/Incident"\
                                            xmlns:WinServiceObj="http://cybox.mitre.org/objects#WinServiceObject"\
                                            xmlns:xal="urn:oasis:names:tc:ciq:xal:3"\
                                            xmlns:maecPackage="http://maec.mitre.org/XMLSchema/maec-package-1"\
                                            xmlns:UnixVolumeObj="http://cybox.mitre.org/objects#UnixVolumeObject"\
                                            xmlns:WinFileObj="http://cybox.mitre.org/objects#WinFileObject"\
                                            xmlns:ExpTgt="http://stix.mitre.org/ExploitTarget"\
                                            xmlns:a="urn:oasis:names:tc:ciq:xal:3"\
                                            xmlns:xsd="http://www.w3.org/2001/XMLSchema"\
                                            xmlns:WinEventObj="http://cybox.mitre.org/objects#WinEventObject"\
                                            xmlns:WinKernelHookObj="http://cybox.mitre.org/objects#WinKernelHookObject"\
                                            xmlns:UnixFileObj="http://cybox.mitre.org/objects#UnixFileObject"\
                                            xmlns:VolumeObj="http://cybox.mitre.org/objects#VolumeObject"\
                                            xmlns:cvrf-common="http://www.icasi.org/CVRF/schema/common/1.1"\
                                            xmlns:dc="http://purl.org/dc/elements/1.1/"\
                                            xmlns:APIObj="http://cybox.mitre.org/objects#APIObject"\
                                            xmlns:x509CertificateObj="http://cybox.mitre.org/objects#X509CertificateObject"\
                                            xmlns:EmailMessageObj="http://cybox.mitre.org/objects#EmailMessageObject"\
                                            xmlns:DeviceObj="http://cybox.mitre.org/objects#DeviceObject"\
                                            xmlns:WinSystemRestoreObj="http://cybox.mitre.org/objects#WinSystemRestoreObject"\
                                            xmlns:ns1="http://cybox.mitre.org/objects#FileObject"\
                                            xmlns:SystemObj="http://cybox.mitre.org/objects#SystemObject"\
                                            xmlns:common="http://cybox.mitre.org/Common_v1"\
                                            xmlns:NetworkConnectionObj="http://cybox.mitre.org/objects#NetworkConnectionObject"\
                                            xmlns:WinComputerAccountObj="http://cybox.mitre.org/objects#WinComputerAccountObject"\
                                            xmlns:WinThreadObj="http://cybox.mitre.org/objects#WinThreadObject"\
                                            xmlns:WinExecutableFileObj="http://cybox.mitre.org/objects#WinExecutableFileObject"\
                                            xmlns:WinMemoryPageRegionObj="http://cybox.mitre.org/objects#WinMemoryPageRegionObject"\
                                            xmlns:WinKernelObj="http://cybox.mitre.org/objects#WinKernelObject"\
                                            xmlns:iodef="urn:ietf:params:xml:ns:iodef-1.0"\
                                            xmlns:WinNetworkRouteEntryObj="http://cybox.mitre.org/objects#WinNetworkRouteEntryObject"\
                                            xmlns:WinPrefetchObj="http://cybox.mitre.org/objects#WinPrefetchObject"\
                                            xmlns:n="urn:oasis:names:tc:ciq:xnl:3"\
                                            xmlns:cvrf="http://www.icasi.org/CVRF/schema/cvrf/1.1"\
                                            xmlns:SemaphoreObj="http://cybox.mitre.org/objects#SemaphoreObject"\
                                            xmlns:ciq="urn:oasis:names:tc:ciq:xpil:3"\
                                            xmlns:SocketObj="http://cybox.mitre.org/objects#SocketObject"\
                                            xmlns:HTTPSessionObj="http://cybox.mitre.org/objects#HTTPSessionObject"\
                                            xmlns:GUIObj="http://cybox.mitre.org/objects#GUIObject"\
                                            xmlns:metadata="http://xml/metadataSharing.xsd"\
                                            xmlns:WinCriticalSectionObj="http://cybox.mitre.org/objects#WinCriticalSectionObject"\
                                            xmlns:DNSRecordObj="http://cybox.mitre.org/objects#DNSRecordObject"\
                                            xmlns:UserAccountObj="http://cybox.mitre.org/objects#UserAccountObject"\
                                            xmlns:WinNetworkShareObj="http://cybox.mitre.org/objects#WinNetworkShareObject"\
                                            xmlns:cyboxCommon="http://cybox.mitre.org/Common_v1"\
                                            xmlns:None="urn:oasis:names:tc:ciq:xpil:3"\
                                            xmlns:aciq="urn:oasis:names:tc:ciq:xal:3"\
                                            xmlns:WinWaitableTimerObj="http://cybox.mitre.org/objects#WinWaitableTimerObject"\
                                            xmlns:vuln="http://www.icasi.org/CVRF/schema/vuln/1.1"\
                                            xmlns:ct="urn:oasis:names:tc:ciq:ct:3"\
                                            xmlns:DNSQueryObj="http://cybox.mitre.org/objects#DNSQueryObject"\
                                            xmlns:FileObj="http://cybox.mitre.org/objects#FileObject"\
                                            xmlns:WinVolumeObj="http://cybox.mitre.org/objects#WinVolumeObject"\
                                            xmlns:PipeObj="http://cybox.mitre.org/objects#PipeObject"\
                                            xmlns:AddressObj="http://cybox.mitre.org/objects#AddressObject"\
                                            xmlns:ArtifactObj="http://cybox.mitre.org/objects#ArtifactObject"\
                                            xmlns:marking="http://data-marking.mitre.org"\
                                            xmlns:DiskObj="http://cybox.mitre.org/objects#DiskObject"\
                                            xmlns:HandleObj="http://cybox.mitre.org/objects#HandleObject"\
                                            xmlns:TTP="http://stix.mitre.org/TTP"\
                                            xmlns:UnixProcessObj="http://cybox.mitre.org/objects#UnixProcessObject"\
                                            xmlns:NetworkRouteObj="http://cybox.mitre.org/objects#NetworkRouteObject"\
                                            xmlns:GUIWindowObj="http://cybox.mitre.org/objects#GUIWindowObject"\
                                            xmlns:NetworkRouteEntryObj="http://cybox.mitre.org/objects#NetworkRouteEntryObject"\
                                            xmlns:stix="http://stix.mitre.org"\
                                            xmlns:prod="http://www.icasi.org/CVRF/schema/prod/1.1"\
                                            xmlns:TA="http://stix.mitre.org/ThreatActor"\
                                            xmlns:URIObj="http://cybox.mitre.org/objects#URIObject"\
                                            xmlns:WinMailslotObj="http://cybox.mitre.org/objects#WinMailslotObject"\
                                            xmlns:PacketObj="http://cybox.mitre.org/objects#PacketObject"\
                                            xmlns:UnixNetworkRouteEntryObj="http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject"\
                                            xmlns:WinDriverObj="http://cybox.mitre.org/objects#WinDriverObject"\
                                            xmlns:NetworkSubnetObj="http://cybox.mitre.org/objects#NetworkSubnetObject"\
                                            xmlns:DiskPartitionObj="http://cybox.mitre.org/objects#DiskPartitionObject"\
                                            xmlns:WhoisObj="http://cybox.mitre.org/objects#WhoisObject"\
                                            xmlns:incident="http://stix.mitre.org/Incident"\
                                            xmlns:Common="http://cybox.mitre.org/Common_v1"\
                                            xmlns:UnixUserAccountObj="http://cybox.mitre.org/objects#UnixUserAccountObject"\
                                            xmlns:NetFlowObj="http://cybox.mitre.org/objects#NetworkFlowObject"\
                                            xmlns:MutexObj="http://cybox.mitre.org/objects#MutexObject"\
                                            xmlns:MemoryObj="http://cybox.mitre.org/objects#MemoryObject"\
                                            xmlns:WinHandleObj="http://cybox.mitre.org/objects#WinHandleObject"\
                                            xmlns:WinTaskObj="http://cybox.mitre.org/objects#WinTaskObject"\
                                            xmlns:LinuxPackageObj="http://cybox.mitre.org/objects#LinuxPackageObject"\
                                            xmlns:maecContainer="http://maec.mitre.org/XMLSchema/maec-container-1"\
                                            xmlns:cybox="http://cybox.mitre.org/cybox_v1"\
                                            xmlns:WinSemaphoreObj="http://cybox.mitre.org/objects#WinSemaphoreObject"\
                                            xmlns:WinPipeObj="http://cybox.mitre.org/objects#WinPipeObject"\
                                            xmlns:xnl="urn:oasis:names:tc:ciq:xnl:3"')
        return s.getvalue()
        
        
    
        
    