
# Class: Protocol


A plan specification which has sufficient level of detail and quantitative information to communicate it between Investigation agents, so that different Investigation agents will reliably be able to independently reproduce the process.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Protocol](https://w3id.org/GHGA-Submission-Metadata-Schema/Protocol)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProtocol],[Attribute]<has_attribute%201..*-++[Protocol&#124;name:string;type:string;description:string;url:string;alias:string;xref:string%20%2B;id(i):string],[Submission]++-%20has_protocol%200..*>[Protocol],[Submission]-%20has_protocol(i)%200..1>[Protocol],[Protocol]uses%20-.->[AttributeMixin],[Protocol]^-[SequencingProtocol],[Protocol]^-[LibraryPreparationProtocol],[InformationContentEntity]^-[Protocol],[LibraryPreparationProtocol],[InformationContentEntity],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProtocol],[Attribute]<has_attribute%201..*-++[Protocol&#124;name:string;type:string;description:string;url:string;alias:string;xref:string%20%2B;id(i):string],[Submission]++-%20has_protocol%200..*>[Protocol],[Submission]-%20has_protocol(i)%200..1>[Protocol],[Protocol]uses%20-.->[AttributeMixin],[Protocol]^-[SequencingProtocol],[Protocol]^-[LibraryPreparationProtocol],[InformationContentEntity]^-[Protocol],[LibraryPreparationProtocol],[InformationContentEntity],[AttributeMixin],[Attribute])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Children

 * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) - Information about the library_preparation of an sequencing experiment.
 * [SequencingProtocol](SequencingProtocol.md) - Information about the sequencing of a sample.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞has_protocol](Submission_has_protocol.md)*  <sub>0..\*</sub>  **[Protocol](Protocol.md)**
 *  **None** *[has_protocol](has_protocol.md)*  <sub>0..1</sub>  **[Protocol](Protocol.md)**

## Attributes


### Own

 * [Protocol➞name](Protocol_name.md)  <sub>1..1</sub>
     * Description: Name of the Protocol (eg: Sample extraction_PCR amplification).
     * Range: [String](types/String.md)
 * [Protocol➞type](Protocol_type.md)  <sub>1..1</sub>
     * Description: Type of the protocol (eg: Target enrichment).
     * Range: [String](types/String.md)
 * [Protocol➞description](Protocol_description.md)  <sub>1..1</sub>
     * Description: Detailed description of the protocol.
     * Range: [String](types/String.md)
 * [Protocol➞url](Protocol_url.md)  <sub>1..1</sub>
     * Description: URL for the resource that describes this protocol.
     * Range: [String](types/String.md)
 * [Protocol➞alias](Protocol_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Protocol➞xref](Protocol_xref.md)  <sub>1..\*</sub>
     * Description: One or more cross-references for this protocol.  (Eg: manufacturer protocol, protocol from publication etc )
     * Range: [String](types/String.md)
 * [Protocol➞has_attribute](Protocol_has_attribute.md)  <sub>1..\*</sub>
     * Description: One or more attributes that further characterizes this protocol.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Inherited from InformationContentEntity:

 * [NamedThing➞id](NamedThing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | OBI:0000272 |

