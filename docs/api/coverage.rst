API Coverage
============

The *python-stix* APIs currently provide ⚠ partial coverage of all STIX-defined constructs. Development is ongoing toward the goal of providing ✓ full STIX language support in the APIs. Until such time that full coverage is provided, an overview of which constructs are available in these APIs will be maintained below.

.. note::

   Many STIX constructs can contain **CybOX** constructs. The **python-cybox** project provides its own APIs for interacting with the **CybOX** specification. Please see the `CybOX API Documentation`_ for information about CybOX API coverage.
   
   .. _CybOX API Documentation: http://cybox.readthedocs.org
   
   
STIX Core
---------

=============================   =====================  	===============================================
STIX Construct                  API Coverage            Documentation
=============================	=====================  	===============================================
STIX Package                    ✓ Full                  :class:`stix.core.stix_package.STIXPackage`
STIX Header                     ✓ Full                  :class:`stix.core.stix_header.STIXHeader`
Related Packages                ✓ Full                  :class:`stix.core.stix_package.RelatedPackages`
=============================   =====================	===============================================

STIX Top-level Constructs
-------------------------

=============================   ==========================  =====================
STIX Construct                  API Coverage                Documentation
=============================   ==========================  =====================
Campaign                        ✓ Full                      :class:`stix.campaign.Campaign`
Course of Action                ✓ Full                      :class:`stix.coa.CourseOfAction`
Exploit Target                  ✓ Full                      :class:`stix.exploit_target.ExploitTarget`
Incident                        ⚠ Partial                   :class:`stix.incident.Incident`
Indicator                       ✓ Full                      :class:`stix.indicator.indicator.Indicator`
Observable                      *Provided by* **CybOX**     
Threat Actor                    ✓ Full                      :class:`stix.threat_actor.ThreatActor`
TTP                             ⚠ Partial                   :class:`stix.ttp.TTP`
=============================   ==========================  =====================

STIX Features
-------------

=============================   ==========================  ==========================================
STIX Construct                  API Coverage                Documentation
=============================   ==========================  ==========================================
Confidence                      ⚠ Partial                   :class:`stix.common.confidence.Confidence`
Handling                        ✓ Full                      :class:`stix.data_marking.Marking`
Markup in Structured Text       × None                      
Relationships                   ✓ Full
=============================   ==========================  ==========================================

STIX Extensions
---------------

=============================   =====================   ==========================================================================================
STIX Construct                  API Coverage            Documentation
=============================   =====================   ==========================================================================================
**Address Extensions**
CIQ Address                     × None                  
|
**Attack Pattern Extensions**
CAPEC 2.7                       × None                  
|
**Identity Extensions**                                 
CIQ Identity                    ⚠ Partial               :class:`stix.extensions.identity.ciq_identity_3_0.CIQIdentity3_0Instance`
|
**Malware Extensions**
MAEC                            ✓ Full                  :class:`stix.extensions.malware.maec_4_1_malware.MAECInstance`
|
**Marking Extensions**
Simple Marking                  ✓ Full                  :class:`stix.extensions.marking.simple_marking.SimpleMarkingStructure`
TLP                             ✓ Full                  :class:`stix.extensions.marking.tlp.TLPMarkingStructure`
Terms of Use                    ✓ Full                  :class:`stix.extensions.marking.terms_of_use_marking.TermsOfUseMarkingStructure`
|
**Structured COA Extensions**
Generic Structured COA          ✓ Full                  :class:`stix.extensions.structured_coa.generic_structured_coa.GenericStructuredCOA`
|
**Test Mechanism Extensions**
Generic Test Mechanism          ✓ Full                  :class:`stix.extensions.test_mechanism.generic_test_mechanism.GenericTestMechanism`
OVAL                            × None
OpenIOC                         ✓ Full                  :class:`stix.extensions.test_mechanism.open_ioc_2010_test_mechanism.OpenIOCTestMechanism`
SNORT                           ✓ Full                  :class:`stix.extensions.test_mechanism.snort_test_mechanism.SnortTestMechanism`
YARA                            ✓ Full                  :class:`stix.extensions.test_mechanism.yara_test_mechanism.YaraTestMechanism`
|
**Vulnerability Extensions**                           
CVRF                            × None                  
=============================   =====================   ==========================================================================================

STIX Vocabularies
-----------------

=========================================   ========================================    ========================================================
STIX Construct                              API Coverage                                Documentation
=========================================   ========================================    ========================================================
AssetTypeVocab-1.0                          ✓ Full                                      :class:`stix.common.vocabs.AssetType_1_0`
AttackerInfrastructureTypeVocab-1.0         ✓ Full                                      :class:`stix.common.vocabs.AttackerInfrastructureType_1_0`
AttackerToolTypeVocab-1.0                   ✓ Full                                      :class:`stix.common.vocabs.AttackerToolType_1_0`
AvailabilityLossTypeVocab-1.0               ✓ Full                                      :class:`stix.common.vocabs.AvailabilityLossType_1_0`
AvailabilityLossTypeVocab-1.1.1             ✓ Full                                      :class:`stix.common.vocabs.AvailabilityLossType_1_1_1`
COAStageVocab-1.0                           ✓ Full                                      :class:`stix.common.vocabs.COAStage_1_0`
CampaignStatusVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.CampaignStatus_1_0`
CourseOfActionTypeVocab-1.0                 ✓ Full                                      :class:`stix.common.vocabs.CourseOfActionType_1_0`
DiscoveryMethodVocab-1.0                    ✓ Full                                      :class:`stix.common.vocabs.DiscoveryMethod_1_0`
DiscoveryMethodVocab-2.0                    ✓ Full                                      :class:`stix.common.vocabs.DiscoveryMethod_2_0`
HighMediumLowVocab-1.0                      ✓ Full                                      :class:`stix.common.vocabs.HighMediumLow_1_0`
ImpactQualificationVocab-1.0                ✓ Full                                      :class:`stix.common.vocabs.ImpactQualification_1_0`
ImpactRatingVocab-1.0                       ✓ Full                                      :class:`stix.common.vocabs.ImpactRating_1_0`
IncidentCategoryVocab-1.0                   ✓ Full                                      :class:`stix.common.vocabs.IncidentCategory_1_0`
IncidentEffectVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.IncidentEffect_1_0`
IncidentStatusVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.IncidentStatus_1_0`
IndicatorTypeVocab-1.0                      ✓ Full                                      :class:`stix.common.vocabs.IndicatorType_1_0`
IndicatorTypeVocab-1.1                      ✓ Full                                      :class:`stix.common.vocabs.IndicatorType_1_1`
InformationSourceRoleVocab-1.0              ✓ Full                                      :class:`stix.common.vocabs.InformationSourceRole_1_0`
InformationTypeVocab-1.0                    ✓ Full                                      :class:`stix.common.vocabs.InformationType_1_0`
IntendedEffectVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.IntendedEffect_1_0`
LocationClassVocab-1.0                      ✓ Full                                      :class:`stix.common.vocabs.LocationClass_1_0`
LossDurationVocab-1.0                       ✓ Full                                      :class:`stix.common.vocabs.LossDuration_1_0`
LossPropertyVocab-1.0                       ✓ Full                                      :class:`stix.common.vocabs.LossProperty_1_0`
MalwareTypeVocab-1.0                        ✓ Full                                      :class:`stix.common.vocabs.MalwareType_1_0`
ManagementClassVocab-1.0                    ✓ Full                                      :class:`stix.common.vocabs.ManagementClass_1_0`
MotivationVocab-1.0                         ✓ Full                                      :class:`stix.common.vocabs.Motivation_1_0`
MotivationVocab-1.0.1                       ✓ Full                                      :class:`stix.common.vocabs.Motivation_1_0_1`
MotivationVocab-1.1                         ✓ Full                                      :class:`stix.common.vocabs.Motivation_1_1`
OwnershipClassVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.OwnershipClass_1_0`
PackageIntentVocab-1.0                      ✓ Full                                      :class:`stix.common.vocabs.PackageIntent_1_0`
PlanningAndOperationalSupportVocab-1.0      ✓ Full                                      :class:`stix.common.vocabs.PlanningAndOperationalSupport_1_0`
PlanningAndOperationalSupportVocab-1.0.1    ✓ Full                                      :class:`stix.common.vocabs.PlanningAndOperationalSupport_1_0_1`
SecurityCompromiseVocab-1.0                 ✓ Full                                      :class:`stix.common.vocabs.SecurityCompromise_1_0`
SystemTypeVocab-1.0                         ✓ Full                                      :class:`stix.common.vocabs.SystemType_1_0`
ThreatActorSophisticationVocab-1.0          ✓ Full                                      :class:`stix.common.vocabs.ThreatActorSophistication_1_0`
ThreatActorTypeVocab-1.0                    ✓ Full                                      :class:`stix.common.vocabs.ThreatActorType_1_0`
=========================================   ========================================    ========================================================
