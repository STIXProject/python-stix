# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from cybox.core import Observables

# internal
import stix
from stix.data_marking import Marking
from stix.common import vocabs, related, VocabString, Statement
import stix.bindings.course_of_action as coa_binding

# relative
from .objective import Objective
from .structured_coa import _BaseStructuredCOA

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


class CourseOfAction(stix.BaseCoreComponent):
    _binding = coa_binding
    _binding_class = coa_binding.CourseOfActionType
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    _version = "1.1.1"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1")
    _ID_PREFIX = 'coa'

    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):

        super(CourseOfAction, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )

        self.stage = None
        self.type_ = None
        self.objective = None
        self.parameter_observables = None
        self.structured_coa = None
        self.impact = None
        self.cost = None
        self.efficacy = None
        self.handling = None
        self.related_coas = RelatedCOAs()
        self.related_packages = related.RelatedPackageRefs()

    @property
    def stage(self):
        return self._stage

    @stage.setter
    def stage(self, value):
        self._set_vocab(Stage, stage=value)

    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, value):
        self._set_vocab(COAType, type=value)

    @property
    def objective(self):
        return self._objective

    @objective.setter
    def objective(self, value):
        self._set_var(Objective, try_cast=False, objective=value)

    @property
    def impact(self):
        return self._impact

    @impact.setter
    def impact(self, value):
        self._set_var(Statement, impact=value)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._set_var(Statement, cost=value)

    @property
    def efficacy(self):
        return self._efficacy

    @efficacy.setter
    def efficacy(self, value):
        self._set_var(Statement, efficacy=value)

    @property
    def handling(self):
        return self._handling

    @handling.setter
    def handling(self, value):
        self._set_var(Marking, try_cast=False, handling=value)

    @property
    def structured_coa(self):
        return self._structured_coa

    @structured_coa.setter
    def structured_coa(self, value):
        self._set_var(_BaseStructuredCOA, try_cast=False, structured_coa=value)

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(CourseOfAction, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.stage:
            return_obj.Stage = self.stage.to_obj(ns_info=ns_info)
        if self.type_:
            return_obj.Type = self.type_.to_obj(ns_info=ns_info)
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
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)
        if self.related_coas:
            return_obj.Related_COAs = self.related_coas.to_obj(ns_info=ns_info)
        if self.related_packages:
            return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)
        if self.structured_coa:
            return_obj.Structured_COA = self.structured_coa.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(CourseOfAction, cls).from_obj(obj, return_obj=return_obj)

        if isinstance(obj, cls._binding_class):  # CourseOfActionType properties
            return_obj.title = obj.Title
            return_obj.stage = VocabString.from_obj(obj.Stage)
            return_obj.type_ = VocabString.from_obj(obj.Type)
            return_obj.objective = Objective.from_obj(obj.Objective)
            return_obj.parameter_observables = \
                Observables.from_obj(obj.Parameter_Observables)
            return_obj.impact = Statement.from_obj(obj.Impact)
            return_obj.cost = Statement.from_obj(obj.Cost)
            return_obj.efficacy = Statement.from_obj(obj.Efficacy)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.related_coas = \
                RelatedCOAs.from_obj(obj.Related_COAs)
            return_obj.related_packages = \
                related.RelatedPackageRefs.from_obj(obj.Related_Packages)
            return_obj.structured_coa = \
                _BaseStructuredCOA.from_obj(obj.Structured_COA)

        return return_obj

    def to_dict(self):
        return super(CourseOfAction, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        super(CourseOfAction, cls).from_dict(dict_repr, return_obj=return_obj)

        get = dict_repr.get
        return_obj.stage = VocabString.from_dict(get('stage'))
        return_obj.type_ = VocabString.from_dict(get('type'))
        return_obj.objective = Objective.from_dict(get('objective'))
        return_obj.parameter_observables = \
            Observables.from_dict(get('parameter_observables'))
        return_obj.impact = Statement.from_dict(get('impact'))
        return_obj.cost = Statement.from_dict(get('cost'))
        return_obj.efficacy = Statement.from_dict(get('efficacy'))
        return_obj.handling = Marking.from_dict(get('handling'))
        return_obj.related_coas = \
            RelatedCOAs.from_dict(get('related_coas'))
        return_obj.related_packages = \
            related.RelatedPackageRefs.from_dict(get('related_packages'))
        return_obj.structured_coa = \
            _BaseStructuredCOA.from_dict(get('structured_coa'))

        return return_obj

# alias for CourseOfAction
COA = CourseOfAction
