# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from cybox.core import Observables

# internal
import stix
import stix.utils as utils
from stix.data_marking import Marking
from stix.common import (
    vocabs, related, StructuredText, VocabString, InformationSource, Statement
)
import stix.bindings.course_of_action as coa_binding

# relative
from .objective import Objective


# Redefines
Stage = vocabs.COAStage
COAType = vocabs.CourseOfActionType


class RelatedCOAs(related.GenericRelationshipList):
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    _binding = coa_binding
    _binding_class = coa_binding.RelatedCOAsType
    _binding_var = "Related_COA"
    _contained_type = related.RelatedCOA
    _inner_name = "coas"


class CourseOfAction(stix.Entity):
    _binding = coa_binding
    _binding_class = coa_binding.CourseOfActionType
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    _version = "1.1.1"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1")

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("coa")
        self.idref = idref
        self.version = None
        self.title = title
        self.stage = None
        self.type_ = None
        self.description = description
        self.short_description = short_description
        self.objective = None
        self.parameter_observables = None
        # self.structured_coa = None
        self.impact = None
        self.cost = None
        self.efficacy = None
        self.information_source = None
        self.handling = None
        self.related_coas = RelatedCOAs()
        self.related_packages = related.RelatedPackageRefs()

        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = utils.dates.now() if not idref else None

    @property
    def id_(self):
        return self._id
    
    @id_.setter
    def id_(self, value):
        if not value:
            self._id = None
        else:
            self._id = value
            self.idref = None
    
    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value):
        if not value:
            self._version = None
        else:
            utils.check_version(self._ALL_VERSIONS, value)
            self._version = value
    
    @property
    def idref(self):
        return self._idref
    
    @idref.setter
    def idref(self, value):
        if not value:
            self._idref = None
        else:
            self._idref = value
            self.id_ = None # unset id_ if idref is present

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        if not value:
            self._stage = None
        elif isinstance(value, VocabString):
            self._stage = value
        else:
            self._stage = Stage(value=value)

    @property
    def type_(self):
        return self._type_

    @type_.setter
    def type_(self, value):
        if not value:
            self._type_ = None
        elif isinstance(value, VocabString):
            self._type_ = value
        else:
            self._type_ = COAType(value=value)

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
    def handling(self):
        return self._handling

    @handling.setter
    def handling(self, value):
        if value and not isinstance(value, Marking):
            raise ValueError('value must be instance of Marking')

        self._handling = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(CourseOfAction, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        if self.timestamp:
            return_obj.timestamp = self.timestamp.isoformat()
        return_obj.version = self.version
        return_obj.Title = self.title
        if self.stage:
            return_obj.Stage = self.stage.to_obj(ns_info=ns_info)
        if self.type_:
            return_obj.Type = self.type_.to_obj(ns_info=ns_info)
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
        if self.objective:
            return_obj.Objective = self.objective.to_obj(ns_info=ns_info)
        if self.parameter_observables:
            return_obj.Parameter_Observables = self.parameter_observables.to_obj(ns_info=ns_info)
        if self.impact:
            return_obj.Impact = self.impact.to_obj(ns_info=ns_info)
        if self.cost:
            return_obj.Cost = self.cost.to_obj(ns_info=ns_info)
        if self.efficacy:
            return_obj.Efficacy = self.efficacy.to_obj(ns_info=ns_info)
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)
        if self.related_coas:
            return_obj.Related_COAs = self.related_coas.to_obj(ns_info=ns_info)
        if self.related_packages:
            return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp

        if isinstance(obj, cls._binding_class): # CourseOfActionType properties
            return_obj.version = obj.version
            return_obj.title = obj.Title
            return_obj.stage = VocabString.from_obj(obj.Stage)
            return_obj.type_ = VocabString.from_obj(obj.Type)
            return_obj.description = StructuredText.from_obj(obj.Description)
            return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
            return_obj.objective = Objective.from_obj(obj.Objective)
            return_obj.parameter_observables = \
                    Observables.from_obj(obj.Parameter_Observables)
            return_obj.impact = Statement.from_obj(obj.Impact)
            return_obj.cost = Statement.from_obj(obj.Cost)
            return_obj.efficacy = Statement.from_obj(obj.Efficacy)
            return_obj.information_source = InformationSource.from_obj(obj.Information_Source)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.related_coas = \
                    RelatedCOAs.from_obj(obj.Related_COAs)
            return_obj.related_packages = \
                    related.RelatedPackageRefs.from_obj(obj.Related_Packages)

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
            d['version'] = self.version
        if self.title:
            d['title'] = self.title
        if self.stage:
            d['stage'] = self.stage.to_dict()
        if self.type_:
            d['type'] = self.type_.to_dict()
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.objective:
            d['objective'] = self.objective.to_dict()
        if self.parameter_observables:
            d['parameter_observables'] = self.parameter_observables.to_dict()
        if self.impact:
            d['impact'] = self.impact.to_dict()
        if self.cost:
            d['cost'] = self.cost.to_dict()
        if self.efficacy:
            d['efficacy'] = self.efficacy.to_dict()
        if self.type_:
            d['type'] = self.type_.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.handling:
            d['handling'] = self.handling.to_dict()
        if self.related_coas:
            d['related_coas'] = self.related_coas.to_dict()
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
        return_obj.version = dict_repr.get('version')
        return_obj.title = dict_repr.get('title')
        return_obj.stage = VocabString.from_dict(dict_repr.get('stage'))
        return_obj.type_ = VocabString.from_dict(dict_repr.get('type'))
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.objective = Objective.from_dict(dict_repr.get('objective'))
        return_obj.parameter_observables = \
                Observables.from_dict(dict_repr.get('parameter_observables'))
        return_obj.impact = Statement.from_dict(dict_repr.get('impact'))
        return_obj.cost = Statement.from_dict(dict_repr.get('cost'))
        return_obj.efficacy = Statement.from_dict(dict_repr.get('efficacy'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))
        return_obj.related_coas = \
                RelatedCOAs.from_dict(dict_repr.get('related_coas'))
        return_obj.related_packages = \
                related.RelatedPackageRefs.from_dict(dict_repr.get('related_packages'))

        return return_obj

# alias for CourseOfAction
COA = CourseOfAction