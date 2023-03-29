
# Class: protocol


A plan specification which has sufficient level of detail and quantitative information to communicate it between investigation agents, so that different investigation agents will reliably be able to independently reproduce the process.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Protocol](https://w3id.org/GHGA-Submission-Metadata-Schema/Protocol)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProtocol],[Attribute]<has%20attribute%201..*-++[Protocol&#124;name:string;type:string;description:string;url:string;alias:string;xref:string%20%2B;id(i):string],[Submission]-%20has%20protocol(i)%200..1>[Protocol],[Submission]++-%20has%20protocol%200..*>[Protocol],[Protocol]uses%20-.->[AttributeMixin],[Protocol]^-[SequencingProtocol],[Protocol]^-[LibraryPreparationProtocol],[InformationContentEntity]^-[Protocol],[LibraryPreparationProtocol],[InformationContentEntity],[AttributeMixin],[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[SequencingProtocol],[Attribute]<has%20attribute%201..*-++[Protocol&#124;name:string;type:string;description:string;url:string;alias:string;xref:string%20%2B;id(i):string],[Submission]-%20has%20protocol(i)%200..1>[Protocol],[Submission]++-%20has%20protocol%200..*>[Protocol],[Protocol]uses%20-.->[AttributeMixin],[Protocol]^-[SequencingProtocol],[Protocol]^-[LibraryPreparationProtocol],[InformationContentEntity]^-[Protocol],[LibraryPreparationProtocol],[InformationContentEntity],[AttributeMixin],[Attribute])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.

## Children

 * [LibraryPreparationProtocol](LibraryPreparationProtocol.md) - Information about the library preparation of an sequencing experiment.
 * [SequencingProtocol](SequencingProtocol.md) - Information about the sequencing of a sample.

## Referenced by Class

 *  **None** *[has protocol](has_protocol.md)*  <sub>0..1</sub>  **[Protocol](Protocol.md)**
 *  **[Submission](Submission.md)** *[submission➞has protocol](submission_has_protocol.md)*  <sub>0..\*</sub>  **[Protocol](Protocol.md)**

## Attributes


### Own

 * [protocol➞name](protocol_name.md)  <sub>1..1</sub>
     * Description: Name of the protocol (eg: Sample extraction_PCR amplification).
     * Range: [String](types/String.md)
 * [protocol➞type](protocol_type.md)  <sub>1..1</sub>
     * Description: Type of the protocol (eg: Target enrichment).
     * Range: [String](types/String.md)
 * [protocol➞description](protocol_description.md)  <sub>1..1</sub>
     * Description: Detailed description of the Protocol.
     * Range: [String](types/String.md)
 * [protocol➞url](protocol_url.md)  <sub>1..1</sub>
     * Description: URL for the resource that describes this Protocol.
     * Range: [String](types/String.md)
 * [protocol➞alias](protocol_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [protocol➞xref](protocol_xref.md)  <sub>1..\*</sub>
     * Description: One or more cross-references for this Protocol.  (Eg: manufacturer protocol, protocol from publication etc )
     * Range: [String](types/String.md)
 * [protocol➞has attribute](protocol_has_attribute.md)  <sub>1..\*</sub>
     * Description: One or more attributes that further characterizes this Protocol.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Inherited from information content entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | OBI:0000272 |

