# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields
from mixbox import entities
from mixbox import typedlist

# cybox
from cybox.core import Observable, ObservableComposition
from cybox.common import Time

# internal
import stix
from stix.common.identity import Identity
from stix.common import (InformationSource, VocabString, Confidence, RelatedTTP,
    Statement, CampaignRef)
from stix.common.related import (GenericRelationshipList, RelatedCOA,
    RelatedIndicator, RelatedCampaignRef, RelatedPackageRefs)
from stix.common.vocabs import VocabField, IndicatorType
from stix.common.kill_chains import KillChainPhasesReference
from stix import utils
import stix.bindings.indicator as indicator_binding

# relative
from .test_mechanism import TestMechanisms
from .sightings import Sightings
from .valid_time import ValidTime

class SuggestedCOAs(GenericRelationshipList):
    """The ``SuggestedCOAs`` class provides functionality for adding
    :class:`stix.common.related.RelatedCOA` instances to an :class:`Indicator`
    instance.

    The ``SuggestedCOAs`` class implements methods found on
    ``collections.MutableSequence`` and as such can be interacted with as a
    ``list`` (e.g., ``append()``).

    The ``append()`` method can accept instances of
    :class:`stix.common.related.RelatedCOA` or :class:`stix.coa.CourseOfAction`
    as an argument.

    Note:
        Calling ``append()`` with an instance of
        :class:`stix.coa.CourseOfAction` will wrap that instance in a
        :class:`stix.common.related.RelatedCOA` layer, with the ``item`` set to
        the :class:`stix.coa.CourseOfAction` instance.

    Examples:
        Append an instance of :class:`stix.coa.CourseOfAction` to the
        ``Indicator.suggested_coas`` property. The instance of
        :class:`stix.coa.CourseOfAction` will be wrapped in an instance of
        :class:`stix.common.related.RelatedCOA`.

        >>> coa = CourseOfAction()
        >>> indicator = Indicator()
        >>> indicator.suggested_coas.append(coa)
        >>> print(type(indicator.suggested_coas[0]))
        <class 'stix.common.related.RelatedCOA'>

        Iterate over the ``suggested_coas`` property of an :class:`Indicator`
        instance and print the ids of each underlying
        :class:`stix.coa.CourseOfAction` instance.

        >>> for related_coa in indicator.suggested_coas:
        >>>     print(related_coa.item.id_)

    Args:
        suggested_coas(list): A list of :class:`stix.coa.CourseOfAction`
            or :class:`stix.common.related.RelatedCOA` instances.
        scope (str): The scope of the items. Can be set to ``"inclusive"``
            or ``"exclusive"``. See
            :class:`stix.common.related.GenericRelationshipList` documentation
            for more information.

    Attributes:
        scope (str): The scope of the items. Can be set to ``"inclusive"``
            or ``"exclusive"``. See
            :class:`stix.common.related.GenericRelationshipList` documentation
            for more information.
    """

    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = indicator_binding.SuggestedCOAsType

    suggested_coa = fields.TypedField("Suggested_COA", RelatedCOA, multiple=True, key_name="suggested_coas")

    def __init__(self, suggested_coas=None, scope=None):
        super(SuggestedCOAs, self).__init__(scope, suggested_coas)


class RelatedIndicators(GenericRelationshipList):
    """The ``RelatedIndicators`` class provides functionality for adding
    :class:`stix.common.related.RelatedIndicator` instances to an
    :class:`Indicator` instance.

    The ``RelatedIndicators`` class implements methods found on
    ``collections.MutableSequence`` and as such can be interacted with as a
    ``list`` (e.g., ``append()``).

    The ``append()`` method can accept instances of
    :class:`stix.common.related.RelatedIndicator` or
    :class:`Indicator` as an argument.

    Note:
        Calling ``append()`` with an instance of
        :class:`stix.coa.CourseOfAction` will wrap that instance in a
        :class:`stix.common.related.RelatedIndicator` layer, with ``item``
        set to the :class:`Indicator` instance.

    Examples:
        Append an instance of :class:`Indicator` to the
        ``Indicator.related_indicators`` property. The instance of
        :class:`Indicator` will be wrapped in an instance of
        :class:`stix.common.related.RelatedIndicator`:

        >>> related = Indicator()
        >>> parent_indicator = Indicator()
        >>> parent_indicator.related_indicators.append(related)
        >>> print(type(indicator.related_indicators[0]))
        <class 'stix.common.related.RelatedIndicator'>

        Iterate over the ``related_indicators`` property of an
        :class:`Indicator` instance and print the ids of each underlying
        :class:`Indicator`` instance:

        >>> for related in indicator.related_indicators:
        >>>     print(related.item.id_)

    Args:
        related_indicators (list, optional): A list of :class:`Indicator` or
            :class:`stix.common.related.RelatedIndicator` instances.
        scope (str, optional): The scope of the items. Can be set to
            ``"inclusive"`` or ``"exclusive"``. See
            :class:`stix.common.related.GenericRelationshipList` documentation
            for more information.

    Attributes:
        scope (str): The scope of the items. Can be set to ``"inclusive"``
            or ``"exclusive"``. See
            :class:`stix.common.related.GenericRelationshipList` documentation
            for more information.

    """
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = indicator_binding.RelatedIndicatorsType

    related_indicator = fields.TypedField("Related_Indicator", RelatedIndicator, multiple=True, key_name="related_indicators")

    def __init__(self, related_indicators=None, scope=None):
        super(RelatedIndicators, self).__init__(scope, related_indicators)


class Indicator(stix.BaseCoreComponent):
    """Implementation of the STIX Indicator.

    Args:
        id_ (optional): An identifier. If ``None``, a value will be generated
            via ``mixbox.idgen.create_id()``. If set, this will unset the
            ``idref`` property.
        idref (optional): An identifier reference. If set this will unset the
            ``id_`` property.
        title (optional): A string title.
        timestamp (optional): A timestamp value. Can be an instance of
            ``datetime.datetime`` or ``str``.
        description (optional): A string description.
        short_description (optional): A string short description.

    """
    _binding = indicator_binding
    _binding_class = indicator_binding.IndicatorType
    _namespace = 'http://stix.mitre.org/Indicator-2'
    _version = "2.2"
    _ALL_VERSIONS = ("2.0", "2.0.1", "2.1", "2.1.1", "2.2")
    _ALLOWED_COMPOSITION_OPERATORS = ('AND', 'OR')
    _ID_PREFIX = "indicator"
    _try_cast = False

    producer = fields.TypedField("Producer", InformationSource)
    observable = fields.TypedField("Observable", Observable)
    indicator_types = VocabField("Type", IndicatorType, multiple=True, key_name="indicator_types")
    confidence = fields.TypedField("Confidence", Confidence)
    indicated_ttps = fields.TypedField("Indicated_TTP", RelatedTTP, multiple=True, key_name="indicated_ttps")
    test_mechanisms = fields.TypedField("Test_Mechanisms",  TestMechanisms)
    alternative_id = fields.TypedField("Alternative_ID", multiple=True)
    suggested_coas = fields.TypedField("Suggested_COAs", SuggestedCOAs)
    sightings = fields.TypedField("Sightings", Sightings)
    composite_indicator_expression = fields.TypedField("Composite_Indicator_Expression", "stix.indicator.CompositeIndicatorExpression")
    kill_chain_phases = fields.TypedField("Kill_Chain_Phases", KillChainPhasesReference)
    valid_time_positions = fields.TypedField("Valid_Time_Position", ValidTime, multiple=True, key_name="valid_time_positions")
    related_indicators = fields.TypedField("Related_Indicators", RelatedIndicators)
    related_campaigns = fields.TypedField("Related_Campaigns", type_="stix.indicator.RelatedCampaignRefs")
    likely_impact = fields.TypedField("Likely_Impact", Statement)
    negate = fields.TypedField("negate")
    related_packages = fields.TypedField("Related_Packages", RelatedPackageRefs)

    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):

        super(Indicator, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )

        self.observable = None
        self.indicator_types = IndicatorTypes()
        self.test_mechanisms = TestMechanisms()
        self.alternative_id = None
        self.suggested_coas = SuggestedCOAs()
        self.sightings = Sightings()
        self.composite_indicator_expression = None
        self.kill_chain_phases = KillChainPhasesReference()
        self.related_indicators = RelatedIndicators()
        self.related_campaigns = RelatedCampaignRefs()
        self.observable_composition_operator = "OR"
        self.related_packages = RelatedPackageRefs()

    @property
    def observables(self):
        """A list of ``cybox.core.Observable`` instances. This can be set to
        a single object instance or a list of objects.

        Note:
            If only one Observable is set, this property will return a list
            with the ``observable`` property.

            If multiple ``cybox.core.Observable`` this property will return
            Observables under the ``cybox.core.ObservableComposition``.

            Access to the top level ``cybox.core.Observable`` is made via
            ``observable`` property.

        Default Value:
            Empty ``list``.

        Returns:
            A ``list`` of ``cybox.core.Observable`` instances.

        """
        if not self.observable:
            return []
        elif self.observable.observable_composition:
            return self.observable.observable_composition.observables

        return []

    @observables.setter
    def observables(self, value):
        """
        The method will automatically create a top ``cybox.core.Observable`` and
        append all ``cybox.core.Observable`` using ``observable_composition``
        property when a ``list`` is given with length greater than 1.

        Note:
            The top level ``cybox.core.Observable`` will set the ``operator``
            property for the ``cybox.core.ObservableComposition`` via the
            ``observable_composition_operator`` property. The value of
            ``operator`` can be changed via ``observable_composition_operator``
            property. By default, the composition layer will be set to ``"OR"``.

        Args:
            value: A ``list`` of ``cybox.core.Observable`` instances or a single
                ``cybox.core.Observable`` instance.

        Raises:
            ValueError: If set to a value that cannot be converted to an
                instance of ``cybox.core.Observable``.
        """
        if not value:
            return

        if isinstance(value, Observable):
            self.observable = value

        elif utils.is_sequence(value):
            if len(value) == 1:
                self.observable = value
                return

            observable_comp = ObservableComposition()
            observable_comp.operator = self.observable_composition_operator

            for element in value:
                observable_comp.add(element)

            self.observable = Observable()
            self.observable.observable_composition = observable_comp

    def set_observables(self, value):
        self.observables = value

    def add_observable(self, observable):
        """Adds an observable to the ``observable`` property of the
        :class:`Indicator`.

        If the `observable` parameter is ``None``, no item will be added
        to the ``observable`` property.

        Note:
            The STIX Language dictates that an :class:`Indicator` can have only
            one ``Observable`` under it. Because of this, when a user adds
            another ``Observable`` a new, empty ``Observable`` will be crated
            and append the existing and new ``observable`` using the
            ``ObservableComposition`` property. To access the top level
            ``Observable`` can be achieved by the ``observable`` property .By
            default, the ``operator`` of the composition layer will be set to
            ``"OR"``. The ``operator`` value can be changed via the
            ``observable_composition_operator`` property.

            Setting ``observable`` or ``observables`` with re-initialize the
            property and lose all ``Observable`` in the composition layer.

        Args:
            observable: An instance of ``cybox.core.Observable`` or an object
                type that can be converted into one.


        Raises:
            ValueError: If the `observable` param cannot be converted into an
                instance of ``cybox.core.Observable``.

        """
        if not observable:
            return

        # Sets the first observable.
        elif not self.observable:
            self.observable = observable

        # When another is inserted. A "root" Observable is created and the
        # user's Observables are appended to the composition.
        elif not self.observable.observable_composition:
            observable_comp = ObservableComposition()
            observable_comp.operator = self.observable_composition_operator

            observable_comp.add(self.observable)
            observable_comp.add(observable)

            self.observable = Observable()
            self.observable.observable_composition = observable_comp

        # Keep appending to "root" Observable.
        else:
            self.observable.observable_composition.add(observable)

    def add_alternative_id(self, value):
        """Adds an alternative id to the ``alternative_id`` list property.

        Note:
            If ``None`` is passed in no value is added to the
            ``alternative_id`` list property.

        Args:
            value: An identifier value.

        """
        if not value:
            return

        self.alternative_id.append(value)

    def add_valid_time_position(self, value):
        """Adds an valid time position to the ``valid_time_positions`` property
        list.

        If `value` is ``None``, no item is added to the ``value_time_positions``
        list.

        Args:
            value: An instance of :class:`stix.indicator.valid_time.ValidTime`.

        Raises:
            ValueError: If the `value` argument is not an instance of
                :class:`stix.indicator.valid_time.ValidTime`.

        """
        self.valid_time_positions.append(value)

    def add_indicator_type(self, value):
        """Adds a value to the ``indicator_types`` list property.

        The `value` parameter can be a ``str`` or an instance of
        :class:`stix.common.vocabs.VocabString`.

        Note:
            If the `value` parameter is a ``str`` instance, an attempt will be
            made to convert it into an instance of
            :class:`stix.common.vocabs.IndicatorType`

        Args:
            value: An instance of :class:`stix.common.vocabs.VocabString`
                or ``str``.

        Raises:
            ValueError: If the `value` param is a ``str`` instance that cannot
                be converted into an instance of
                :class:`stix.common.vocabs.IndicatorType`.
        """
        self.indicator_types.append(value)

    def add_indicated_ttp(self, v):
        """Adds an Indicated TTP to the ``indicated_ttps`` list property
        of this :class:`Indicator`.

        The `v` parameter must be an instance of
        :class:`stix.common.related.RelatedTTP` or :class:`stix.ttp.TTP`.

        If the `v` parameter is ``None``, no item wil be added to the
        ``indicated_ttps`` list property.

        Note:
            If the `v` parameter is not an instance of
            :class:`stix.common.related.RelatedTTP` an attempt will be made
            to convert it to one.

        Args:
            v: An instance of :class:`stix.common.related.RelatedTTP` or
                :class:`stix.ttp.TTP`.

        Raises:
            ValueError: If the `v` parameter cannot be converted into an
                instance of :class:`stix.common.related.RelatedTTP`

        """
        self.indicated_ttps.append(v)

    def add_test_mechanism(self, tm):
        """Adds an Test Mechanism to the ``test_mechanisms`` list property
        of this :class:`Indicator`.

        The `tm` parameter must be an instance of a
        :class:`stix.indicator.test_mechanism._BaseTestMechanism`
        implementation.

        If the `tm` parameter is ``None``, no item will be added to the
        ``test_mechanisms`` list property.

        See Also:
            Test Mechanism implementations are found under the
            :mod:`stix.extensions.test_mechanism` package.

        Args:
            tm: An instance of a
                :class:`stix.indicator.test_mechanism._BaseTestMechanism`
                implementation.

        Raises:
            ValueError: If the `tm` parameter is not an instance of
                :class:`stix.indicator.test_mechanism._BaseTestMechanism`

        """
        self.test_mechanisms.append(tm)

    def add_related_indicator(self, indicator):
        """Adds an Related Indicator to the ``related_indicators`` list
        property of this :class:`Indicator`.

        The `indicator` parameter must be an instance of
        :class:`stix.common.related.RelatedIndicator` or
        :class:`Indicator`.

        If the `indicator` parameter is ``None``, no item wil be added to the
        ``related_indicators`` list property.

        Calling this method is the same as calling ``append()`` on the
        ``related_indicators`` proeprty.

        See Also:
            The :class:`RelatedIndicators` documentation.

        Note:
            If the `tm` parameter is not an instance of
            :class:`stix.common.related.RelatedIndicator` an attempt will be
            made to convert it to one.

        Args:
            indicator: An instance of :class:`Indicator` or
                :class:`stix.common.related.RelatedIndicator`.

        Raises:
            ValueError: If the `indicator` parameter cannot be converted into
                an instance of :class:`stix.common.related.RelatedIndicator`

        """
        self.related_indicators.append(indicator)

    def add_related_campaign(self, value):
        """Adds a Related Campaign to this Indicator.

        The `value` parameter must be an instance of :class:`.RelatedCampaignRef`
        or :class:`.CampaignRef`.

        If the `value` parameter is ``None``, no item wil be added to the
        ``related_campaigns`` collection.

        Calling this method is the same as calling ``append()`` on the
        ``related_campaigns`` property.

        See Also:
            The :class:`.RelatedCampaignRef` documentation.

        Note:
            If the `value` parameter is not an instance of
            :class:`.RelatedCampaignRef` an attempt will be made to convert it
            to one.

        Args:
            value: An instance of :class:`.RelatedCampaignRef` or
                :class:`.Campaign`.

        Raises:
            ValueError: If the `value` parameter cannot be converted into
                an instance of :class:`.RelatedCampaignRef`

        """
        self.related_campaigns.append(value)

    @property
    def observable_composition_operator(self):
        return self._observable_composition_operator

    @observable_composition_operator.setter
    def observable_composition_operator(self, value):
        if value in self._ALLOWED_COMPOSITION_OPERATORS:
            self._observable_composition_operator = value

            if self.observable and self.observable.observable_composition:
                self.observable.observable_composition.operator = value

            return

        error = "observable_composition_operator must one of {0}"
        error = error.format(self._ALLOWED_COMPOSITION_OPERATORS)
        raise ValueError(error)

    def add_kill_chain_phase(self, value):
        """Add a new Kill Chain Phase reference to this Indicator.

        Args:
            value: a :class:`stix.common.kill_chains.KillChainPhase` or a `str`
                representing the phase_id of. Note that you if you are defining
                a custom Kill Chain, you need to add it to the STIX package
                separately.
        """
        self.kill_chain_phases.append(value)

    def add_related_package(self, value):
        self.related_packages.append(value)

    def set_producer_identity(self, identity):
        """Sets the name of the producer of this indicator.

        This is the same as calling
        ``indicator.producer.identity.name = identity``.

        If the ``producer`` property is ``None``, it will be initialized to
        an instance of
        :class:`stix.common.information_source.InformationSource`.

        If the ``identity`` property of the ``producer`` instance is ``None``,
        it will be initialized to an instance of
        :class:`stix.common.identity.Identity`.

        Note:
            if the `identity` parameter is not an instance
            :class:`stix.common.identity.Identity` an attempt will be made
            to convert it to one.

        Args:
            identity: An instance of ``str`` or
                ``stix.common.identity.Identity``.

        """
        def unset_producer_identity():
            try:
                self.producer.identity.name = None
            except AttributeError:
                pass

        if not identity:
            unset_producer_identity()
            return

        if not self.producer:
            self.producer = InformationSource()

        if isinstance(identity, Identity):
            self.producer.identity = identity
            return

        if not self.producer.identity:
            self.producer.identity = Identity()

        self.producer.identity.name = str(identity)

    def set_produced_time(self, produced_time):
        """Sets the ``produced_time`` property of the ``producer`` property
        instance fo `produced_time`.

        This is the same as calling
        ``indicator.producer.time.produced_time = produced_time``.

        The `produced_time` parameter must be an instance of ``str``,
        ``datetime.datetime``, or ``cybox.common.DateTimeWithPrecision``.

        Note:
            If `produced_time` is a ``str`` or ``datetime.datetime`` instance
            an attempt will be made to convert it into an instance of
            ``cybox.common.DateTimeWithPrecision``.

        Args:
            produced_time: An instance of ``str``,
                ``datetime.datetime``, or ``cybox.common.DateTimeWithPrecision``.

        """
        if not self.producer:
            self.producer = InformationSource()

        if not self.producer.time:
            self.producer.time = Time()

        self.producer.time.produced_time = produced_time

    def get_produced_time(self):
        """Gets the produced time for this :class:`Indicator`.

        This is the same as calling
        ``produced_time = indicator.producer.time.produced_time``.

        Returns:
            ``None`` or an instance of ``cybox.common.DateTimeWithPrecision``.

        """
        try:
            return self.producer.time.produced_time
        except AttributeError:
            return None

    def set_received_time(self, received_time):
        """Sets the received time for this :class:`Indicator`.

        This is the same as calling
        ``indicator.producer.time.produced_time = produced_time``.

        The `received_time` parameter must be an instance of ``str``,
        ``datetime.datetime``, or ``cybox.common.DateTimeWithPrecision``.

        Args:
            received_time: An instance of ``str``,
                ``datetime.datetime``, or ``cybox.common.DateTimeWithPrecision``.

        Note:
            If `received_time` is a ``str`` or ``datetime.datetime`` instance
            an attempt will be made to convert it into an instance of
            ``cybox.common.DateTimeWithPrecision``.

        """
        if not self.producer:
            self.producer = InformationSource()

        if not self.producer.time:
            self.producer.time = Time()

        self.producer.time.received_time = received_time

    def get_received_time(self):
        """Gets the received time for this :class:`Indicator`.

        This is the same as calling
        ``received_time = indicator.producer.time.received_time``.

        Returns:
            ``None`` or an instance of ``cybox.common.DateTimeWithPrecision``.

        """
        try:
            return self.producer.time.received_time
        except AttributeError:
            return None

    def _merge_observables(self, observables):
        observable_composition = ObservableComposition()
        observable_composition.operator = self.observable_composition_operator

        for observable in observables:
            observable_composition.add(observable)

        root_observable = Observable()
        root_observable.observable_composition = observable_composition

        return root_observable

    def add_object(self, object_):
        """Adds a python-cybox Object instance to the ``observables`` list
        property.

        This is the same as calling ``indicator.add_observable(object_)``.

        Note:
            If the `object` param is not an instance of ``cybox.core.Object``
            an attempt will be made to to convert it into one before wrapping
            it in an ``cybox.core.Observable`` layer.

        Args:
            object_: An instance of ``cybox.core.Object`` or an object
                that can be converted into an instance of
                ``cybox.core.Observable``

        Raises:
            ValueError: if the `object_` param cannot be converted to an
                instance of ``cybox.core.Observable``.
        """
        if not object_:
            return

        observable = Observable(object_)
        self.add_observable(observable)

    def _finalize_obj(self, entity_obj):
        """Omits the `negate` field if it is not equal to True.
        """
        if self.negate:
            entity_obj.negate = True
        elif hasattr(entity_obj, 'negate'):
           entity_obj.negate = None

    def _finalize_dict(self, entity_dict):
        """Omits the `negate` field if it is not equal to True.
        """
        if self.negate:
            entity_dict['negate'] = True
        elif 'negate' in entity_dict:
           del entity_dict['negate']


def check_operator(composite_indicator_exp, value):
    allowed = CompositeIndicatorExpression.OPERATORS

    if not value:
        raise ValueError("operator must not be None or empty")
    elif value not in allowed:
        raise ValueError("operator must be one of: %s" % allowed)
    else:
        return


class CompositeIndicatorExpression(entities.EntityList):
    """Implementation of the STIX ``CompositeIndicatorExpressionType``.

    The ``CompositeIndicatorExpression`` class implements methods found on
    ``collections.MutableSequence`` and as such can be interacted with as a
    ``list`` (e.g., ``append()``).

    Note:
        The ``append()`` method can only accept instances of :class:`Indicator`.

    Examples:
        Add a :class:`Indicator` instance to an instance of
        :class:`CompositeIndicatorExpression`:

        >>> i = Indicator()
        >>> comp = CompositeIndicatorExpression()
        >>> comp.append(i)

        Create a :class:`CompositeIndicatorExpression` from a list of
        :class:`Indicator` instances using ``*args`` argument list:

        >>> list_indicators = [Indicator() for i in xrange(10)]
        >>> comp = CompositeIndicatorExpression(CompositeIndicatorExpression.OP_OR, *list_indicators)
        >>> len(comp)
        10

    Args:
        operator (str, optional): The logical composition operator. Must be ``"AND"`` or
            ``"OR"``.
        *args: Variable length argument list of :class:`Indicator` instances.

    Attributes:
        OP_AND (str): String ``"AND"``
        OP_OR (str): String ``"OR"``
        OPERATORS (tuple): Tuple of allowed ``operator`` values.
        operator (str): The logical composition operator. Must be ``"AND"`` or
            ``"OR"``.

    """
    _binding = indicator_binding
    _binding_class = indicator_binding.CompositeIndicatorExpressionType
    _namespace = 'http://stix.mitre.org/Indicator-2'

    OP_AND = "AND"
    OP_OR = "OR"
    OPERATORS = (OP_AND, OP_OR)
    operator = fields.TypedField("operator", preset_hook=check_operator)
    indicator = fields.TypedField(
        name="Indicator",
        type_=Indicator,
        multiple=True,
        key_name="indicators"
    )

    # TODO (bworrell): Change this to *args, **kwargs to get around the weirdness
    # that occurs when creating with kwarg and arglist.
    # E.g, CompositeIndicatorExpression(operator="AND", arg1, arg2, arg3)
    # will raise an error.
    def __init__(self, operator="OR", *args):
        super(CompositeIndicatorExpression, self).__init__(*args)
        self.operator = operator


class _RelatedCampaignRefList(typedlist.TypedList):
    def __init__(self, *args):
        super(_RelatedCampaignRefList, self).__init__(type=RelatedCampaignRef, *args)

    def _fix_value(self, value):
        from stix.campaign import Campaign

        if isinstance(value, Campaign) and value.id_:
            return RelatedCampaignRef(CampaignRef(idref=value.id_))

        msg = "Cannot insert object of type '%s' into '%s'"
        msg = msg % (type(value), self.__class__.__name__)
        raise TypeError(msg)


class RelatedCampaignRefs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.RelatedCampaignReferencesType

    related_campaign = fields.TypedField(
        name="Related_Campaign",
        type_=RelatedCampaignRef,
        multiple=True,
        key_name="related_campaigns",
        listfunc=_RelatedCampaignRefList
    )

    def __init__(self, related_campaign_refs=None, scope=None):
        super(RelatedCampaignRefs, self).__init__(scope, related_campaign_refs)


# NOT ACTUAL STIX TYPES!
class IndicatorTypes(stix.TypedList):
    """A :class:`stix.common.vocabs.VocabString` collection which defaults to
    :class:`stix.common.vocabs.IndicatorType`. This class implements methods
    found on ``collections.MutableSequence`` and as such can be interacted with
    like a ``list``.

    Note:
        The ``append()`` method can accept ``str`` or
        :class:`stix.common.vocabs.VocabString` instances. If a ``str`` instance
        is passed in, an attempt will be made to convert it to an instance of
        :class:`stix.common.vocabs.IndicatorType`.

    Examples:
        Add an instance of :class:`stix.common.vocabs.IndicatorType`:

        >>> from stix.common.vocabs import IndicatorType
        >>> itypes = IndicatorTypes()
        >>> type_ = IndicatorType(IndicatorType.TERM_IP_WATCHLIST)
        >>> itypes.append(type_)
        >>> print(len(itypes))
        1

        Add a string value:

        >>> from stix.common.vocabs import IndicatorType
        >>> itypes = IndicatorTypes()
        >>> type(IndicatorType.TERM_IP_WATCHLIST)
        <type 'str'>
        >>> itypes.append(IndicatorType.TERM_IP_WATCHLIST)
        >>> print(len(itypes))
        1

    Args:
        *args: Variable length argument list of strings or
            :class:`stix.common.vocabs.VocabString` instances.

    """
    _namespace = "http://stix.mitre.org/Indicator-2"
    _contained_type = VocabString

    def _fix_value(self, value):
        return IndicatorType(value)


class _Observables(stix.TypedList):
    _contained_type = Observable
