# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
from cybox.core import Observables

# internal
import stix
from stix.common import vocabs
from stix.common.related import GenericRelationshipList, RelatedPackageRefs, RelatedCOA
from stix.common.vocabs import VocabField
from stix.common.statement import Statement
from stix.common.information_source import InformationSource
import stix.bindings.course_of_action as coa_binding

# relative
from .objective import Objective
from .structured_coa import StructuredCOAFactory, _BaseStructuredCOA

# Redefines
Stage = vocabs.COAStage
COAType = vocabs.CourseOfActionType


class RelatedCOAs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    _binding = coa_binding
    _binding_class = coa_binding.RelatedCOAsType

    related_coa = fields.TypedField(
        name="Related_COA",
        type_=RelatedCOA,
        multiple=True,
        key_name="coas"
    )


class CourseOfAction(stix.BaseCoreComponent):
    """Implementation of the STIX Course of Action.

    Args:
        id_ (optional): An identifier. If ``None``, a value will be generated
            via ``mixbox.idgen.create_id()``. If set, this will unset the
            ``idref`` property.
        idref (optional): An identifier reference. If set this will unset the
            ``id_`` property.
        timestamp (optional): A timestamp value. Can be an instance of
            ``datetime.datetime`` or ``str``.
        description: A description of the purpose or intent of this object.
        short_description: A short description of the intent
            or purpose of this object.
        title: The title of this object.

    """
    _binding = coa_binding
    _binding_class = coa_binding.CourseOfActionType
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    _version = "1.2"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1", "1.2")
    _ID_PREFIX = 'coa'

    stage = VocabField("Stage", Stage)
    type_ = VocabField("Type", COAType)
    objective = fields.TypedField("Objective", Objective)
    parameter_observables = fields.TypedField("Parameter_Observables", Observables)
    structured_coa = fields.TypedField("Structured_COA", type_=_BaseStructuredCOA, factory=StructuredCOAFactory)
    impact = fields.TypedField("Impact", Statement)
    cost = fields.TypedField("Cost", Statement)
    efficacy = fields.TypedField("Efficacy", Statement)
    related_coas = fields.TypedField("Related_COAs", RelatedCOAs)
    related_packages = fields.TypedField("Related_Packages", RelatedPackageRefs)
    information_source = fields.TypedField("Information_Source", InformationSource)

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

        self.related_coas = RelatedCOAs()
        self.related_packages = RelatedPackageRefs()

# alias for CourseOfAction
COA = CourseOfAction
