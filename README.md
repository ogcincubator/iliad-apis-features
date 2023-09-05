# OGC API Features Profiles

Profiles of the OGC API Features to support interoperability in the ILIAD Digital Twin of the Ocean context.

The compiled (ready to use) elements and documentation are available here: (https://ogcincubator.github.io/iliad-apis-features/)

These profiles demonstrate a scalable and extensible approach to creating different levels of interoperability for different sub-domains. 

The core of this profile is the SOSA component of the Oceans Information Model using a standardised JSON schema, JSON-LD context and SHACL rules regarding disposition of metadata across ObservationCollections and individual observations.

# Contents

## ILIAD Ocean Information Model - Observation Features

This profile defines a baseline for all APIs delivering observational data in the ILIAD system. 
The requirements are simple and pertain to metadata required to register services and data in the ILIAD ecosystem.

This profile defines transformations for the Features JSON schema to and from other APIs, such as EDR and STA.

## ILIAD Citizen Science Profile

Common constraints on Iliad Observations for Citizen Science applications.  These constraints match the semantics of the STA+ API defined by the OGC Citizen Science Working Group

Largely this is expected to describe the project using a standardised form.

## Jellyfish Pilot

Specific constraints for services delivering data for the Jellyfish Pilot.

Applies the ILIAD Citizen Science Profile to the Citizen Science general profile.

Defines specific procedures and observable properties required.

## Oilspills Pilot

# How to use

This repository can be used to define compatible application schemas or reusable Building Blocks for families of interoperable APIS that conform to the profiles defined here.

You can find information on using this as a template for defining Building Blocks in [USAGE.md](USAGE.md).
