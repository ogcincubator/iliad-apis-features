# OGC API Profiles for ILIAD

This repository defines profiles of the OGC APIs to support interoperability in the ILIAD Digital Twin of the Ocean context. [About Profiles](PROFILES.md)

The profiles link OGC APIs such as OGC API Features to specific schemas supporting the Oceans Information Model used by ILIAD, and show how these can be used to define specific application profiles.

[Here](https://drive.google.com/file/d/1kKC2Wx8wItdoH_ZVDQA-KW-f4wv46xcU/view?usp=sharing) is  a short (11mins) video describing this from a "Best Practices" perspective.

The compiled (ready to use) elements and documentation are available here: (https://ogcincubator.github.io/iliad-apis-features/)

These profiles demonstrate a scalable and extensible approach to creating different levels of interoperability for different sub-domains.

The core of this profile is the SOSA component of the Oceans Information Model using a standardised JSON schema, JSON-LD context and SHACL rules regarding disposition of metadata across ObservationCollections and individual observations.

![Overview](https://lucid.app/publicSegments/view/bba7b5a1-722d-4046-aad9-08cc87735287/image.png)

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

### Note - this is a "straw man"

The schema and content of this are based on an draft implementation based on early analysis by PSNC and OGC and will be finalised as pilot design progresses.

## Oilspills Pilot
(TBD)

# Deployment and testing

The interoperability specifications defined here will be tested and deployed as working examples and tested in context of alternative representations using other OGC APIs according to the following approach:

![](
https://lucid.app/publicSegments/view/77d9155c-1f93-4698-8168-94ad8adf8761/image.png)

Note the common semantic model target achieved using the JSON-LD binding, inherited from the [ogcapi-sosa building block](https://github.com/opengeospatial/ogcapi-sosa)


## General Building block repository structure


The `build/` directory contains the **_reusable assets_** for implementing this building block, in full or part, and the rest of the repository contain *sources* to build these assets.  *Sources* minimise redundant information and preserve original forms of inputs, such as externally published schemas etc.  This allow these to be updated safely, and also allows for alternative forms of original source material to be used whilst preserving uniformity of the reusable assets.

Note that the these components will be consistently structured for a given type of building block, and the editable components may vary according to the source material used to derive the building block, and therefore cannot be directly referenced.

### Editable components

- `features/`: schemas for the feature types defined by this bb (which is a "super-bb" containing at least oneOf these defined features)
- `datatypes/`: reusable schemas for (potentially complex) datatypes defined by this bb
- `aspects/`: groups of properties that may be included in feature types (equivalent to attribute groups in XML schema)
- `assets/`: Documentation assets (e.g. images) directory. See [Assets](#assets) below.

[More information on design and usage](https://github.com/opengeospatial/bblock-template/blob/master/USAGE.md)
