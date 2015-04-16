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
CIQ Identity                    ✓ Full                  :class:`stix.extensions.identity.ciq_identity_3_0.CIQIdentity3_0Instance`
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
Generic Structured COA          × None                  
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
AssetTypeVocab-1.0                          ✓ Full                                      :class:`stix.common.vocabs.AssetType`
AttackerInfrastructureTypeVocab-1.0         ✓ Full                                      :class:`stix.common.vocabs.AttackerInfrastructureType`
AttackerToolTypeVocab-1.0                   ✓ Full                                      :class:`stix.common.vocabs.AttackerToolType`
AvailabilityLossTypeVocab-1.0               × None *(replaced by version 1.1.1)*                                      
AvailabilityLossTypeVocab-1.1.1             ✓ Full                                      :class:`stix.common.vocabs.AvailabilityLossType`
COAStageVocab-1.0                           ✓ Full                                      :class:`stix.common.vocabs.COAStage`
CampaignStatusVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.CampaignStatus`
CourseOfActionTypeVocab-1.0                 ✓ Full                                      :class:`stix.common.vocabs.CourseOfActionType`
DiscoveryMethodVocab-1.0                    ✓ Full                                      :class:`stix.common.vocabs.DiscoveryMethod`
HighMediumLowVocab-1.0                      ✓ Full                                      :class:`stix.common.vocabs.HighMediumLow`
ImpactQualificationVocab-1.0                ✓ Full                                      :class:`stix.common.vocabs.ImpactQualification`
ImpactRatingVocab-1.0                       ✓ Full                                      :class:`stix.common.vocabs.ImpactRating`
IncidentCategoryVocab-1.0                   ✓ Full                                      :class:`stix.common.vocabs.IncidentCategory`
IncidentEffectVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.IncidentEffect`
IncidentStatusVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.IncidentStatus`
IndicatorTypeVocab-1.0                      × None *(replaced by version 1.1)*                                      
IndicatorTypeVocab-1.1                      ✓ Full                                      :class:`stix.common.vocabs.IndicatorType`
InformationSourceRoleVocab-1.0              ✓ Full                                      :class:`stix.common.vocabs.InformationSourceRole`
InformationTypeVocab-1.0                    ✓ Full                                      :class:`stix.common.vocabs.InformationType`
IntendedEffectVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.IntendedEffect`
LocationClassVocab-1.0                      ✓ Full                                      :class:`stix.common.vocabs.LocationClass`
LossDurationVocab-1.0                       ✓ Full                                      :class:`stix.common.vocabs.LossDuration`
LossPropertyVocab-1.0                       ✓ Full                                      :class:`stix.common.vocabs.LossProperty`
MalwareTypeVocab-1.0                        ✓ Full                                      :class:`stix.common.vocabs.MalwareType`
ManagementClassVocab-1.0                    ✓ Full                                      :class:`stix.common.vocabs.ManagementClass`
MotivationVocab-1.0                         × None *(replaced by version 1.0.1)*                                      
MotivationVocab-1.0.1                       × None *(replaced by version 1.1)*                                      
MotivationVocab-1.1                         ✓ Full                                      :class:`stix.common.vocabs.Motivation`
OwnershipClassVocab-1.0                     ✓ Full                                      :class:`stix.common.vocabs.OwnershipClass`
PackageIntentVocab-1.0                      ✓ Full                                      :class:`stix.common.vocabs.PackageIntent`
PlanningAndOperationalSupportVocab-1.0      × None *(replaced by version 1.0.1)*                                      
PlanningAndOperationalSupportVocab-1.0.1    ✓ Full                                      :class:`stix.common.vocabs.PlanningAndOperationalSupport`
SecurityCompromiseVocab-1.0                 ✓ Full                                      :class:`stix.common.vocabs.SecurityCompromise`
SystemTypeVocab-1.0                         ✓ Full                                      :class:`stix.common.vocabs.SystemType`
ThreatActorSophisticationVocab-1.0          ✓ Full                                      :class:`stix.common.vocabs.ThreatActorSophistication`
ThreatActorTypeVocab-1.0                    ✓ Full                                      :class:`stix.common.vocabs.ThreatActorType`
=========================================   ========================================    ========================================================
