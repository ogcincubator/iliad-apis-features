# Profile patterns

Standards can define very specific application behaviours, of general patterns common to many applications. Applications can be quite simple, but complexity emerges from many different solutions to the same common patterns. Alternatively powerful, flexible common patterns can be defined and re-used in applications. These however can be hard to understand - however **profiles** of such standards can provide simplified views by constraining and demonstrating implementation options.  Profiles can also extend common patterns with application specific capabilities, including re-use of other common standards and rules how things inter-relate.

**Profiles** allow all the underlying details of base standards to be automatically included in documentation, testing and validation - this _encapsulates_ the underlying complexity of base specifications.

This dramatically **simplifies** profiles in terms of both development and usage, and ensures **consistency** and conformance of profiles with base specifications.

Typical types of profiles are a layering of general to specific, with specific benefits accruing to each layer in terms of reuse of software through to reuse of application data.
![](https://lucid.app/publicSegments/view/5bebb494-e12f-46c6-a633-9c4cb3f0ba56/image.png)

In particular, if base specifications use the OGC BuildingBlocks then profiles can _leverage_ all the effort in design, testing and validation capabilities through CI/CT (*Continuous Integration/Continuus Testing),

Thus profiles based on OGC Building Blocks also use the same structures as the underlying standards, so they can be profiled in turn.

## What is a profile?

A profile defines a set of constraints on a base specification. Implementations of profiles conform to the base specification.

Because many technologies like JSON and RDF are permissive (by default) about additional information being present, definition of an *extension* is effectively defining a *constraint* on how additional information should be represented.

## What forms of constraints are possible?

The **OGC BuildingBlock** model supports a range of possible constraint approaches.  The goal is to make such constraints **_machine-readable_** to the extent possible.

Constraints SHOULD be defined in a form that allows for **_validation_** of test cases and examples.

Built-in support is provided for automatic validation of the following forms:
- project metadata (description)
- well-formed examples, using relevant encoding (e.g. JSON, TTL)
- JSON schema (for JSON examples) for **structure**
- SHACL (Shapes Constraint Language for RDF) for **content** and **logical consistency**
- Operations (functions or methods) - i.e. API definitions

SHACL and other validations can be performed using controlled vocabularies. Currently this is limited to using SHACL against a **Graph closure** - i.e. inclusion of vocabulary content in testing procedure confiduration, however it is planned to extend this to a more general mechanism supporting both Linked Data and Vocabulary Services - pending standardisation of access methods for these in emerging infrastructures such as "Data Spaces".

In addition [custom validators](VALIDATORS) can be added to the validation workflow.

Using a JSON-LD context "semantic uplift" of JSON to RDF supports use of SHACL and other forms of validators to

## Operations (APIs)

Defining the set of operations that are supported by a data model can be done in several forms, such as defining **entailment** rules, functions or API methods that operate on a standardised data model to implement or exploit the underlying semantics of the data.  For example, a time-series of observations could queried to select a specific time period, or even used to interpolate or extrapolate results. Dimensionally organised data can support dimension-specific functions, graph or network data structures can follow links according to rules etc.  All these functions a fundamental to the data semantics, but may be expressed using different data schemas. Profiles can be used to further specify exactly which operations can be supported for a given data model, where the data model may support a wider range of options, but the intended usage does not need these.

## Profiles of profiles...

The most powerful form of constraint is re-use of existing standards and inheritance of well-tested patterns with existing software support. **Profiles of profiles** is a typical inheritance pattern common in many programming languages, such as Interface and Class hierarchies. It is both powerful means to simplify development, but also provides clarity to consuming software allowing simplified re-use of systems based on this principle.

Profiles should themselves be designed as well documented and tested sets of constraints that can be reused - for example a time-series of water-quality monitoring observations could be specified as a profile of both a time-series profile of Observations and a water-quality profile for the results of such observations.
In turn the time-series profile could defined as data structure using GeoJSON, or Coverage JSON.  The water-quality content requirements could be described using constraints independent of the data structure.

## Testing

Test cases should be provided for each component part of a specification.  This requires a minimal conformant **base example** that the specific test case can be added to.

(Note consideration is being given to making such a baseline example resuable by reference instead of duplication, and potentially derived automatically from declared schema)

Testing should start by validating the **base example** passes all declared constraints, then for each profile constraint:
- identifying a set of valid cases that should conform to the constraint, testing each aspect
- creating a copy of the base under the **/tests/** folder with a name indicating which constraint and case is being tested - e.g. **my-building-block/tests/mything-property-b-number.json**
- adding the specific example to the example
- creating one or more failure tests with **-fail** file name endings - e.g. **my-building-block/tests/mything-property-b-number-fail.json**
