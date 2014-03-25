# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from datetime import datetime
import dateutil

import stix
import stix.utils
import stix.bindings.course_of_action as coa_binding
from stix.common.related import (GenericRelationshipList, RelatedPackageRefs)
from stix.common import StructuredText, VocabString, InformationSource, Statement
from stix.data_marking import Marking
from .objective import Objective

class Stage(VocabString):
    # placeholder until Stage has vocabulary
    pass

class COAType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:CourseOfActionTypeVocab-1.0'
    
class CourseOfAction(stix.Entity):
    _binding = coa_binding
    _binding_class = coa_binding.CourseOfActionType
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    _version = "1.1"

    def __init__(self, id_=None, idref=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("coa")
        self.idref = idref
        self.timestamp = None
        self.version = self._version
        self.title = title
        self.description = description
        self.short_description = short_description
        self.stage = None
        self.impact = None
        self.cost = None
        self.efficacy = None
        self.information_source = None
        self.type_ = None
        self.handling = None
        self.objective = None
        self.related_packages = RelatedPackageRefs()
        # self.parameter_observables = None
        # self.structured_coa = None
        # self.related_coas = None

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not value:
            self._timestamp = None
        elif isinstance(value, datetime):
            self._timestamp = value
        else:
            self._timestamp = dateutil.parser.parse(value)
            
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._description = value
            else:
                self._description = StructuredText(value=value)
        else:
            self._description = None

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._short_description = value
            else:
                self._short_description = StructuredText(value=value)
        else:
            self._short_description = None
            
    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        if not value:
            self._stage = None
        elif isinstance(value, Stage):
            self._stage = value
        else:
            self._stage = Stage(value=value)
            
    @property
    def information_source(self):
        return self._information_source
    
    @information_source.setter
    def information_source(self, value):
        if not value:
            self._information_source = None
        elif isinstance(value, InformationSource):
            self._information_source = value
        else:
            raise ValueError('value must be instance of InformationSource')

    @property
    def impact(self):
        return self._impact
    
    @impact.setter
    def impact(self, impact):
        if not impact:
            self._impact = None
        elif isinstance(impact, Statement):
            self._impact = impact
        else:
            self._impact = Statement(value=impact)
            
    @property
    def cost(self):
        return self._cost
    
    @cost.setter
    def cost(self, cost):
        if not cost:
            self._cost = None
        elif isinstance(cost, Statement):
            self._cost = cost
        else:
            self._cost = Statement(value=cost)
            
    @property
    def efficacy(self):
        return self._efficacy
    
    @efficacy.setter
    def efficacy(self, efficacy):
        if not efficacy:
            self._efficacy = None
        elif isinstance(efficacy, Statement):
            self._efficacy = efficacy
        else:
            self._efficacy = Statement(value=efficacy)

    @property
    def type_(self):
        return self._type_

    @type_.setter
    def type_(self, value):
        if not value:
            self._type_ = None
        elif isinstance(value, COAType):
            self._type_ = value
        else:
            self._type_ = COAType(value=value)

    @property
    def handling(self):
        return self._handling

    @handling.setter
    def handling(self, value):
        if value and not isinstance(value, Marking):
            raise ValueError('value must be instance of Marking')

        self._handling = value

    @property
    def objective(self):
        return self._objective
    
    @objective.setter
    def objective(self, value):
        if not value:
            self._objective = None
        elif isinstance(value, Objective):
            self._objective = value
        else:
            raise ValueError('Cannot set objective to type %s' % type(value))

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)
        return_obj.set_version(self.version)
        return_obj.set_Title(self.title)
        
        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.short_description:
            return_obj.set_Short_Description(self.short_description.to_obj())
        if self.stage:
            return_obj.set_Stage(self.stage.to_obj())
        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())
        if self.cost:
            return_obj.set_Cost(self.cost.to_obj())
        if self.efficacy:
            return_obj.set_Efficacy(self.efficacy.to_obj())
        if self.impact:
            return_obj.set_Impact(self.impact.to_obj())
        if self.type_:
            return_obj.set_Type(self.type_.to_obj())
        if self.timestamp:
            return_obj.set_timestamp(self.timestamp.isoformat())
        if self.handling:
            return_obj.set_Handling(self.handling.to_obj())
        if self.objective:
            return_obj.set_Objective(self.objective.to_obj())
        if self.related_packages:
            return_obj.set_Related_Packages(self.related_packages.to_obj())
        
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        return_obj.id_ = obj.get_id()
        return_obj.idref = obj.get_idref()
        
        if isinstance(obj, cls._binding_class): # CourseOfActionType properties
            return_obj.version = obj.get_version() or cls._version
            return_obj.title = obj.get_Title()
            return_obj.description = StructuredText.from_obj(obj.get_Description())
            return_obj.short_description = StructuredText.from_obj(obj.get_Short_Description())
            return_obj.stage = Stage.from_obj(obj.get_Stage())
            return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())
            return_obj.cost = Statement.from_obj(obj.get_Cost())
            return_obj.efficacy = Statement.from_obj(obj.get_Efficacy())
            return_obj.impact = Statement.from_obj(obj.get_Impact())
            return_obj.type_ = COAType.from_obj(obj.get_Type())
            return_obj.timestamp = obj.get_timestamp()
            return_obj.handling = Marking.from_obj(obj.get_Handling())
            return_obj.objective = Objective.from_obj(obj.get_Objective())
            return_obj.related_packages = RelatedPackageRefs.from_obj(obj.get_Related_Packages())
            
        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = self.timestamp.isoformat()
        if self.version:
            d['version'] = self.version or self._version
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.stage:
            d['stage'] = self.stage.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.cost:
            d['cost'] = self.cost.to_dict()
        if self.efficacy:
            d['efficacy'] = self.efficacy.to_dict()
        if self.impact:
            d['impact'] = self.impact.to_dict()
        if self.type_:
            d['type'] = self.type_.to_dict()
        if self.handling:
            d['handling'] = self.handling.to_dict()
        if self.objective:
            d['objective'] = self.objective.to_dict()
        if self.related_packages:
            d['related_packages'] = self.related_packages.to_dict()
        
        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()
        
        return_obj.id_ = dict_repr.get('id')
        return_obj.idref = dict_repr.get('idref')
        return_obj.timestamp = dict_repr.get('timestamp')
        return_obj.version = dict_repr.get('version', cls._version)
        return_obj.title = dict_repr.get('title')
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.stage = Stage.from_dict(dict_repr.get('stage'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.cost = Statement.from_dict(dict_repr.get('cost'))
        return_obj.efficacy = Statement.from_dict(dict_repr.get('efficacy'))
        return_obj.impact = Statement.from_dict(dict_repr.get('impact'))
        return_obj.type_ = COAType.from_dict(dict_repr.get('type'))
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))
        return_obj.objective = Objective.from_dict(dict_repr.get('objective'))
        return_obj.related_packages = RelatedPackageRefs.from_dict(dict_repr.get('related_packages'))
        
        return return_obj

