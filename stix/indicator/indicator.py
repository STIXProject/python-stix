# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.utils import dates
from stix.common import (
    Identity, InformationSource, StructuredText, VocabString, Confidence,
    RelatedTTP, Statement
)
import stix.bindings.indicator as indicator_binding
from .test_mechanism import _BaseTestMechanism
from .sightings import Sightings
from .valid_time import ValidTime
from stix.common.related import (
    GenericRelationshipList, RelatedCOA, RelatedIndicator
)
from stix.data_marking import Marking
from cybox.core import Observable, ObservableComposition
from cybox.common import Time

from stix.common.vocabs import IndicatorType
from stix.common.kill_chains import KillChainPhasesReference

from datetime import datetime
from dateutil.tz import tzutc

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
        >>> print type(indicator.suggested_coas[0])
        <class 'stix.common.related.RelatedCOA'>

        Iterate over the ``suggested_coas`` property of an :class:`Indicator`
        instance and print the ids of each underlying
        :class:`stix.coa.CourseOfAction` instance.

        >>> for related_coa in indicator.suggested_coas:
        >>>     print related_coa.item.id_

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
    _binding_var = "Suggested_COA"
    _contained_type = RelatedCOA
    _inner_name = "suggested_coas"

    def __init__(self, suggested_coas=None, scope=None):
         if suggested_coas is None:
             suggested_coas = []
         super(SuggestedCOAs, self).__init__(scope, *suggested_coas)


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
        >>> print type(indicator.related_indicators[0])
        <class 'stix.common.related.RelatedIndicator'>

        Iterate over the ``related_indicators`` property of an
        :class:`Indicator` instance and print the ids of each underlying
        :class:`Indicator`` instance:

        >>> for related in indicator.related_indicators:
        >>>     print related.item.id_

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
    _binding_var = "Related_Indicator"
    _contained_type = RelatedIndicator
    _inner_name = "related_indicators"

    def __init__(self, related_indicators=None, scope=None):
        if related_indicators is None:
            related_indicators = []
        super(RelatedIndicators, self).__init__(scope, *related_indicators)

class Indicator(stix.Entity):
    """Implementation of the STIX ``IndicatorType``.

    Args:
        id_ (optional): An identifier. If ``None``, a value will be generated
            via ``stix.utils.create_id()``. If set, this will unset the
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
    _version = "2.1.1"
    _ALL_VERSIONS = ("2.0", "2.0.1", "2.1", "2.1.1")

    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("indicator")
        self.idref = idref
        self.version = None # self._version
        self.producer = None
        self.observables = None
        self.title = title
        self.description = description
        self.short_description = short_description
        self.indicator_types = IndicatorTypes()
        self.confidence = None
        self.indicated_ttps = None
        self.test_mechanisms = None
        self.alternative_id = None
        self.suggested_coas = SuggestedCOAs()
        self.sightings = Sightings()
        self.composite_indicator_expression = None
        self.handling = None
        self.kill_chain_phases = KillChainPhasesReference()
        self.valid_time_positions = None
        self.related_indicators = None
        self.observable_composition_operator = "OR"
        self.likely_impact = None
        self.negate = None
    
        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.now(tzutc()) if not idref else None
    
    @property
    def id_(self):
        """The ``id_`` property for this :class:`Indicator` which serves as
        an identifier. This is automatically set during ``__init__()``.

        Default Value: ``None``

        Note:
            The :class:`Indicator` class cannot have both its ``id_`` and
            ``idref`` properties set at the same time. As such, setting the
            ``idref`` property will unset the ``id_`` property and setting
            the ``id_`` property will unset the ``idref`` property.

        Returns:
            A string id.

        """
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
        """The ``version`` property of this :class:`Indicator`. This property
        will always return ``None`` unless it is set to a value different than
        ``Indicator._version``.

        Note:
            This property refers to the version of the ``Indicator`` schema
            type and should not be used for the purpose of content versioning.

        Default Value: ``None``

        Returns:
            The value of the ``version`` property if set to a value different
            than ``Indicator._version``

        """
        return self._version
    
    @version.setter
    def version(self, value):
        if not value:
            self._version = None
        else:
            if value not in self._ALL_VERSIONS:
                msg = ("Version must be one of %s. Found '%s'" %
                      (self._ALL_VERSIONS, value))
                raise ValueError(msg)
            self._version = value
    
    @property
    def idref(self):
        """The ``idref`` property for this :class:`Indicator`.

        The ``idref`` property must be set to the ``id_`` value of another
        :class:`Indicator` instance. An idref does not need to resolve to a
        local :class`Indicator` instance.

        Default Value: ``None``.

        Note:
            The :class:`Indicator` class cannot have both its ``id_`` and
            ``idref`` properties set at the same time. As such, setting the
            ``idref`` property will unset the ``id_`` property and setting
            the ``id_`` property will unset the ``idref`` property.

        Returns:
            The value of the ``idref`` property

        """
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
        """The ``timestamp`` propety for this :class:`Indicator` instance. This
        property declares the time of creation and is automatically set in
        ``__init__()``.

        This property can accept ``datetime.datetime`` or ``str`` values.
        If an ``str`` value is supplied, a best-effort attempt is made to
        parse it into an instance of ``datetime.datetime``.

        Default Value: A ``datetime.dateime`` instance with a value of the
        date/time when ``__init__()`` was called.

        Note:
            If an ``idref`` is set during ``__init__()``, the value of
            ``timestamp`` will not automatically generated and instead default
            to the ``timestamp`` parameter, which has a default value of
            ``None``.

        Returns:
            An instance of ``datetime.datetime``.

        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = dates.parse_value(value)

    @property
    def description(self):
        """The ``description`` property for this :class:`Indicator`.

        Default Value: ``None``

        Note:
            If set to a value that is not an instance of
            :class:`stix.common.structured_text.StructuredText`, an attempt to
            will be made to convert the value into an instance of
            :class:`stix.common.structured_text.StructuredText`.

        Returns:
            An instance of
            :class:`stix.common.structured_text.StructuredText`

        """
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
        """The ``short_description`` property for this :class:`Indicator`.

        Default Value: ``None``

        Note:
            If set to a value that is not an instance of
            :class:`stix.common.structured_text.StructuredText`, an attempt to
            will be made to convert the value into an instance of
            :class:`stix.common.structured_text.StructuredText`.

        Returns:
            An instance of
            :class:`stix.common.structured_text.StructuredText`

        """
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
    def producer(self):
        """Contains information about the source of the :class:`Indicator`.

        Default Value: ``None``

        Returns:
            An instance of
            :class:`stix.common.information_source.InformationSource`

        Raises:
            ValueError: If set to a value that is not ``None`` and not an
                instance of
                :class:`stix.common.information_source.InformationSource`

        """
        return self._producer

    @producer.setter
    def producer(self, value):
        if value and not isinstance(value, InformationSource):
            raise ValueError('value must be instance of InformationSource')

        self._producer = value

    @property
    def observable(self):
        """A convenience property for accessing or setting the only
        ``cybox.core.Observable`` instance held by this Indicator.

        Default Value: Empty ``list``.

        Setting this property results in the ``observables`` property being
        reinitialized to an empty ``list`` and appending the input value,
        resulting in a ``list`` containing one value.

        Note:
            If the ``observables`` list contains more than one item, this
            property will only return the first item in the list.

        Returns:
            An instance of ``cybox.core.Observable``.

        Raises:
            ValueError: If set to a value that cannot be converted to an
                instance of ``cybox.core.Observable``.


        """
        if self.observables:
            return self.observables[0]
        else:
            return None
    
    @observable.setter
    def observable(self, observable):
        self._observables = []
        self.add_observable(observable)

    @property
    def observables(self):
        """A list of ``cybox.core.Observable`` instances. This can be set to
        a single object instance or a list of objects.

        Note:
            If the input value or values are not instance(s) of
            ``cybox.core.Observable``, an attempt will be made to
            convert the value to an instance of ``cybox.core.Observable``.

        Default Value: Empty ``list``

        Returns:
            A ``list`` of ``cybox.core.Observable`` instances.

        Raises:
            ValueError: If set to a value that cannot be converted to an
                instance of ``cybox.core.Observable``.

        """
        return self._observables

    @observables.setter
    def observables(self, valuelist):
        self._observables = [] # initialize the variable

        if valuelist:
            for value in valuelist:
                self.add_observable(value)
                
    @property
    def alternative_id(self):
        """An alternative identifi  er for this :class:`Indicator`

        This property can be set to a single string identifier or a list of
        identifiers. If set to a single object, the object will be inserted
        into an empty list internally.

        Default Value: Empty ``list``

        Returns:
            A list of alternative ids.

        """
        return self._alternative_id

    @alternative_id.setter
    def alternative_id(self, value):
        self._alternative_id = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_alternative_id(v)
        else:
            self.add_alternative_id(value)

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
        else:
            self.alternative_id.append(value)
                
    @property
    def valid_time_positions(self):
        """A list of valid time positions for this :class:`Indicator`.

        This property can be set to a single instance or a list of
        :class:`stix.indicator.valid_time.ValidTime` instances. If set to a
        single instance, that object is converted into a list containing
        one item.

        Default Value: Empty ``list``

        Returns:
            A list of
            :class:`stix.indicator.valid_time.ValidTime` instances.

        """
        return self._valid_time_positions

    @valid_time_positions.setter
    def valid_time_positions(self, value):
        self._valid_time_positions = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_valid_time_position(v)
        else:
            self.add_valid_time_position(value)

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
        if not value:
            return
        elif isinstance(value, ValidTime):
            self.valid_time_positions.append(value)
        else:
            raise ValueError("value must be instance of ValidTime")

    @property
    def indicator_types(self):
        """A list of indicator types for this :class:`Indicator`.

        This property can be set to lists or single instances of ``str``
        or :class:`stix.common.vocabs.VocabString` or an instance
        of :class:`IndicatorTypes`.

        Note:
            If an instance of ``str`` is passed in (or a ``list`` containing
            ``str`` values) an attempt will be made to convert that string
            value to an instance of :class:`stix.common.vocabs.IndicatorType`.

        Default Value: An empty ``IndicatorTypes`` instance.

        See Also:
            Documentation for :class:`IndicatorTypes`.

        Returns:
            An instance of ``IndicatorTypes``.

        """
        return self._indicator_types

    @indicator_types.setter
    def indicator_types(self, value):
        if not value:
            self._indicator_types = IndicatorTypes()
        elif isinstance(value, IndicatorTypes):
            self._indicator_types = value
        elif hasattr(value, "__getitem__"):
            for v in value:
                self.add_indicator_type(v)
        else:
            self.add_indicator_type(value)

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
        if not value:
            return
        elif isinstance(value, VocabString):
            self.indicator_types.append(value)
        else:
            tmp_indicator_type = IndicatorType(value=value)
            self.indicator_types.append(tmp_indicator_type)
    
    @property
    def confidence(self):
        """The confidence for this :class:`Indicator`.

        This property can be set to an instance of ``str``,
        :class:`stix.common.vocabs.VocabString`, or
        :class:`stix.common.confidence.Confidence`.

        Default Value: ``None``

        Note:
            If set to an instance of ``str`` or
            :class:`stix.common.vocabs.VocabString`, that value will be wrapped
            in an instance of
            :class:`stix.common.confidence.Confidence`.

        Returns:
            An instance of of
            :class:`stix.common.confidence.Confidence`.

        Raises:
            ValueError: If set to a ``str`` value that cannot be converted into
                an instance of :class:`stix.common.confidence.Confidence`.

        """
        return self._confidence
    
    @confidence.setter
    def confidence(self, value):
        if not value:
            self._confidence = None
        elif isinstance(value, Confidence):
            self._confidence = value
        else:
            self._confidence = Confidence(value=value)

    @property
    def indicated_ttps(self):
        return self._indicated_ttps
    
    @indicated_ttps.setter
    def indicated_ttps(self, value):
        self._indicated_ttps = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_indicated_ttp(v)
        else:
            self.add_indicated_ttp(value)
            
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
        if not v:
            return
        elif isinstance(v, RelatedTTP):
            self.indicated_ttps.append(v)
        else:
            self.indicated_ttps.append(RelatedTTP(v))
        
    @property
    def test_mechanisms(self):
        return self._test_mechanisms
    
    @test_mechanisms.setter
    def test_mechanisms(self, value):
        self._test_mechanisms = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_test_mechanism(v)
        else:
            self.add_test_mechanism(value)
            
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
        if not tm:
            return
        elif isinstance(tm, _BaseTestMechanism):
            self.test_mechanisms.append(tm)
        else:
            raise ValueError('Cannot add type %s to test_mechanisms list' % type(tm))

    @property
    def handling(self):
        return self._handling
    
    @handling.setter
    def handling(self, value):
        if not value:
            self._handling = None
        elif isinstance(value, Marking):
            self._handling = value
        else:
            raise ValueError('unable to set handling to type %s' % type(value))

    @property
    def related_indicators(self):
        return self._related_indicators

    @related_indicators.setter
    def related_indicators(self, value):
        self._related_indicators = RelatedIndicators()
        
        if not value:
            return
        elif isinstance(value, RelatedIndicators):
            self._related_indicators = value
        elif isinstance(value, list):
            for v in value:
                self.add_related_indicator(v)
        else:
            self.add_related_indicator(value)
    
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
        if not indicator:
            return
        elif isinstance(indicator, RelatedIndicator):
            self.related_indicators.append(indicator)
        else:
            self.related_indicators.append(RelatedIndicator(indicator))

    @property
    def observable_composition_operator(self):
        return self._observable_composition_operator

    @observable_composition_operator.setter
    def observable_composition_operator(self, value):
        if value not in ("AND", "OR"):
            raise ValueError("observable_composition_operator must be 'AND' "
                             "or 'OR'")
        
        self._observable_composition_operator = value
    
    @property
    def likely_impact(self):
        return self._likely_impact
    
    @likely_impact.setter
    def likely_impact(self, value):
        if not value:
            self._likely_impact = None
        elif isinstance(value, Statement):
            self._likely_impact = value
        else:
            self._likely_impact = Statement(value=value)
            
    @property
    def negate(self):
        return self._negate
    
    @negate.setter
    def negate(self, value):
        if value in (1, True, '1'):
            self._negate = True
        else:  # set to None so that binding will not output negate attribute
            self._negate = None
    
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
        if not identity:
            try:
                self.producer.identity.name = None
            except AttributeError:
                pass
            return

        if not self.producer:
            self.producer = InformationSource()

        if isinstance(identity, Identity):
            self.producer.identity = identity
        else:
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
        except:
            return None

    def add_observable(self, observable):
        """Adds an observable to the ``observables`` list property of the
        :class:`Indicator`.

        If the `observable` parameter is ``None``, no item will be added
        to the ``observables`` list.

        Note:
            The STIX Language dictates that an :class:`Indicator` can have only
            one ``Observable`` under it. Because of this, the ``to_xml()``
            method will convert the ``observables`` list into  an
            ``cybox.core.ObservableComposition``  instance, in which each item
            in the ``observables`` list will be added to the composition. By
            default, the ``operator`` of the composition layer will be set to
            ``"OR"``. The ``operator`` value can be changed via the
            ``observable_composition_operator`` property.

        Args:
            observable: An instance of ``cybox.core.Observable`` or an object
                type that can be converted into one.


        Raises:
            ValueError: If the `observable` param cannot be converted into an
                instance of ``cybox.core.Observable``.

        """
        if not observable:
            return

        if isinstance(observable, Observable):
            self.observables.append(observable)
        else:
            # try to cast it to an Observable type
            self.observables.append(Observable(observable))

    def _merge_observables(self, observables):
        observable_composition = ObservableComposition()
        observable_composition.operator = self.observable_composition_operator

        for observable_ in observables:
            observable_composition.add(observable_)

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

    def to_obj(self, return_obj=None, ns_info=None):
        super(Indicator, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.timestamp = dates.serialize_value(self.timestamp)
        return_obj.Title = self.title
        
        if self.negate:
            return_obj.negate = self._negate
        if self.version:
            return_obj.version = self._version
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
        if self.confidence:
            return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
        if self.indicator_types:
            for indicator_type in self.indicator_types:
                tmp_indicator_type = indicator_type.to_obj(ns_info=ns_info)
                return_obj.add_Type(tmp_indicator_type)
        if self.indicated_ttps:
            return_obj.Indicated_TTP = [x.to_obj(ns_info=ns_info) for x in self.indicated_ttps]
        if self.observables:
            if len(self.observables) > 1:
                root_observable = self._merge_observables(self.observables)
            else:
                root_observable = self.observables[0]
            return_obj.Observable = root_observable.to_obj(ns_info=ns_info)
        if self.producer:
            return_obj.Producer = self.producer.to_obj(ns_info=ns_info)
        if self.test_mechanisms:
            tms_obj = self._binding.TestMechanismsType()
            tms_obj.Test_Mechanism = [x.to_obj(ns_info=ns_info) for x in self.test_mechanisms]
            return_obj.Test_Mechanisms = tms_obj
        if self.likely_impact:
            return_obj.Likely_Impact = self.likely_impact.to_obj(ns_info=ns_info)
        if self.alternative_id:
            return_obj.Alternative_ID = self.alternative_id
        if self.valid_time_positions:
            return_obj.Valid_Time_Position = [x.to_obj(ns_info=ns_info) for x in self.valid_time_positions]
        if self.suggested_coas:
            return_obj.Suggested_COAs = self.suggested_coas.to_obj(ns_info=ns_info)
        if self.sightings:
            return_obj.Sightings = self.sightings.to_obj(ns_info=ns_info)
        if self.composite_indicator_expression:
            return_obj.Composite_Indicator_Expression = self.composite_indicator_expression.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)
        if self.kill_chain_phases:
            return_obj.Kill_Chain_Phases = self.kill_chain_phases.to_obj(ns_info=ns_info)
        if self.related_indicators:
            return_obj.Related_Indicators = self.related_indicators.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):        
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_              = obj.id
        return_obj.idref            = obj.idref
        return_obj.timestamp        = obj.timestamp
        
        if isinstance(obj, cls._binding_class):
            return_obj.title            = obj.Title
            return_obj.description      = StructuredText.from_obj(obj.Description)
            return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
            return_obj.producer         = InformationSource.from_obj(obj.Producer)
            return_obj.confidence       = Confidence.from_obj(obj.Confidence)
            return_obj.sightings        = Sightings.from_obj(obj.Sightings)
            return_obj.composite_indicator_expression = CompositeIndicatorExpression.from_obj(obj.Composite_Indicator_Expression)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.kill_chain_phases = KillChainPhasesReference.from_obj(obj.Kill_Chain_Phases)
            return_obj.related_indicators = RelatedIndicators.from_obj(obj.Related_Indicators)
            return_obj.likely_impact = Statement.from_obj(obj.Likely_Impact)
            
            if obj.negate:
                return_obj.negate = obj.negate
            if obj.version:
                return_obj.version = obj.version
            if obj.Type:
                for indicator_type in obj.Type:
                    return_obj.add_indicator_type(VocabString.from_obj(indicator_type)) 
            if obj.Observable:
                observable_obj = obj.Observable
                observable = Observable.from_obj(observable_obj)
                return_obj.observables.append(observable)
            if obj.Indicated_TTP:
                return_obj.indicated_ttps = [RelatedTTP.from_obj(x) for x in obj.Indicated_TTP]
            if obj.Test_Mechanisms:
                return_obj.test_mechanisms = [_BaseTestMechanism.from_obj(x) for x in obj.Test_Mechanisms.Test_Mechanism]
            if obj.Suggested_COAs:
                return_obj.suggested_coas = SuggestedCOAs.from_obj(obj.Suggested_COAs)
            if obj.Alternative_ID:
                return_obj.alternative_id = obj.Alternative_ID
            if obj.Valid_Time_Position:
                return_obj.valid_time_positions = [ValidTime.from_obj(x) for x in obj.Valid_Time_Position]    
            
        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = dates.serialize_value(self.timestamp)
        if self.negate:
            d['negate'] = self.negate
        if self.version:
            d['version'] = self.version
        if self.observables:
            if len(self.observables) == 1:
                d['observable'] = self.observables[0].to_dict()
            else:
                composite_observable = self._merge_observables(self.observables)
                d['observable'] = composite_observable.to_dict()
        if self.producer:
            d['producer'] = self.producer.to_dict()
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.indicator_types:
            d['indicator_types'] = [x.to_dict() for x in self.indicator_types]
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()
        if self.indicated_ttps:
            d['indicated_ttps'] = [x.to_dict() for x in self.indicated_ttps]
        if self.test_mechanisms:
            d['test_mechanisms'] = [x.to_dict() for x in self.test_mechanisms]
        if self.likely_impact:
            d['likely_impact'] = self.likely_impact.to_dict()
        if self.alternative_id:
            d['alternative_id'] = self.alternative_id
        if self.valid_time_positions:
            d['valid_time_positions'] = [x.to_dict() for x in self.valid_time_positions]
        if self.suggested_coas:
            d['suggested_coas'] = self.suggested_coas.to_dict()
        if self.sightings:
            d['sightings'] = self.sightings.to_dict()
        if self.composite_indicator_expression:
            d['composite_indicator_expression'] = self.composite_indicator_expression.to_dict()
        if self.handling:
            d['handling'] = self.handling.to_dict()
        if self.kill_chain_phases:
            d['kill_chain_phases'] = self.kill_chain_phases.to_dict()
        if self.related_indicators:
            d['related_indicators'] = self.related_indicators.to_dict()
        
        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_       = dict_repr.get('id')
        return_obj.idref     = dict_repr.get('idref')
        return_obj.timestamp = dict_repr.get('timestamp')
        return_obj.title     = dict_repr.get('title')
        return_obj.negate    = dict_repr.get('negate', None)
        return_obj.version   = dict_repr.get('version')
        observable_dict      = dict_repr.get('observable')
        producer_dict        = dict_repr.get('producer')
        description_dict     = dict_repr.get('description')
        indicator_type_list  = dict_repr.get('indicator_types', [])
        confidence_dict      = dict_repr.get('confidence')
        alternative_id_dict  = dict_repr.get('alternative_id')
        valid_time_position_dict  = dict_repr.get('valid_time_positions')

        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.indicated_ttps = [RelatedTTP.from_dict(x) for x in dict_repr.get('indicated_ttps', [])]
        return_obj.test_mechanisms = [_BaseTestMechanism.from_dict(x) for x in dict_repr.get('test_mechanisms', [])]
        return_obj.suggested_coas = SuggestedCOAs.from_dict(dict_repr.get('suggested_coas'))
        return_obj.sightings = Sightings.from_dict(dict_repr.get('sightings'))
        return_obj.composite_indicator_expression = CompositeIndicatorExpression.from_dict(dict_repr.get('composite_indicator_expression'))
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))
        return_obj.kill_chain_phases = KillChainPhasesReference.from_dict(dict_repr.get('kill_chain_phases'))
        return_obj.related_indicators = RelatedIndicators.from_dict(dict_repr.get('related_indicators'))
        return_obj.likely_impact = Statement.from_dict(dict_repr.get('likely_impact'))
        
        if observable_dict:
            return_obj.add_observable(Observable.from_dict(observable_dict))
        if producer_dict:
            return_obj.producer = InformationSource.from_dict(producer_dict)
        if description_dict:
            return_obj.description = StructuredText.from_dict(description_dict)
        for indicator_type_dict in indicator_type_list:
            return_obj.add_indicator_type(VocabString.from_dict(indicator_type_dict))
        if confidence_dict:
            return_obj.confidence = Confidence.from_dict(confidence_dict)
        if alternative_id_dict:
            return_obj.alternative_id = alternative_id_dict
        if valid_time_position_dict:
            for valid_time_position_type_dict in valid_time_position_dict:
                return_obj.add_valid_time_position(ValidTime.from_dict(valid_time_position_type_dict))
        
        return return_obj

class CompositeIndicatorExpression(stix.EntityList):
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
    _contained_type = Indicator
    _binding_var = "Indicator"
    _inner_name = "indicators"
    
    OP_AND = "AND"
    OP_OR = "OR"
    OPERATORS = (OP_AND, OP_OR)
    
    def __init__(self, operator="OR", *args):
        super(CompositeIndicatorExpression, self).__init__(*args)
        self.operator = operator

    @property
    def operator(self):
        return self._operator
    
    @operator.setter
    def operator(self, value):
        if not value:
            raise ValueError("operator must not be None or empty")
        elif value not in self.OPERATORS:
            raise ValueError("operator must be one of: %s" % ",".join(self.OPERATORS))
        else:
            self._operator = value
            
    def __nonzero__(self):
        return super(CompositeIndicatorExpression, self).__nonzero__()

    def to_obj(self, return_obj=None, ns_info=None):
        list_obj = super(CompositeIndicatorExpression, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        list_obj.operator = self.operator
        return list_obj

    def to_dict(self):
        d = super(CompositeIndicatorExpression, self).to_dict()
        if self.operator:
            d['operator'] = self.operator
        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if return_obj is None:
            return_obj = cls()

        super(CompositeIndicatorExpression, cls).from_obj(obj, return_obj=return_obj)
        return_obj.operator = obj.operator
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if return_obj is None:
            return_obj = cls()

        super(CompositeIndicatorExpression, cls).from_dict(dict_repr, return_obj=return_obj)
        return_obj.operator = dict_repr.get('operator')
        return return_obj

class IndicatorTypes(stix.EntityList):
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
        >>> print len(itypes)
        1

        Add a string value:

        >>> from stix.common.vocabs import IndicatorType
        >>> itypes = IndicatorTypes()
        >>> type(IndicatorType.TERM_IP_WATCHLIST)
        <type 'str'>
        >>> itypes.append(IndicatorType.TERM_IP_WATCHLIST)
        >>> print len(itypes)
        1

    Args:
        *args: Variable length argument list of strings or
            :class:`stix.common.vocabs.VocabString` instances.

    """
    _namespace = "http://stix.mitre.org/Indicator-2"
    _contained_type = VocabString

    def _fix_value(self, value):
        return IndicatorType(value)
