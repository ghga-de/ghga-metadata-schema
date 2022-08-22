
# Class: attribute


A key/value pair that further characterizes an entity.

URI: [GHGA:Attribute](https://w3id.org/GHGA/Attribute)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[SequencingProtocol],[Protocol],[Project],[LibraryPreparationProtocol],[AttributeMixin]++-%20has%20attribute%200..*>[Attribute&#124;key:string;key_type:string%20%3F;value:string;value_type:string%20%3F],[LibraryPreparationProtocol]++-%20has%20attribute%200..*>[Attribute],[Project]++-%20has%20attribute%200..*>[Attribute],[Protocol]++-%20has%20attribute%200..*>[Attribute],[SequencingProtocol]++-%20has%20attribute%200..*>[Attribute],[Study]++-%20has%20attribute%200..*>[Attribute],[AttributeMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[SequencingProtocol],[Protocol],[Project],[LibraryPreparationProtocol],[AttributeMixin]++-%20has%20attribute%200..*>[Attribute&#124;key:string;key_type:string%20%3F;value:string;value_type:string%20%3F],[LibraryPreparationProtocol]++-%20has%20attribute%200..*>[Attribute],[Project]++-%20has%20attribute%200..*>[Attribute],[Protocol]++-%20has%20attribute%200..*>[Attribute],[SequencingProtocol]++-%20has%20attribute%200..*>[Attribute],[Study]++-%20has%20attribute%200..*>[Attribute],[AttributeMixin])

## Referenced by Class

 *  **None** *[has attribute](has_attribute.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)** *[library preparation protocol➞has attribute](library_preparation_protocol_has_attribute.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **[Project](Project.md)** *[project➞has attribute](project_has_attribute.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **[Protocol](Protocol.md)** *[protocol➞has attribute](protocol_has_attribute.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **[SequencingProtocol](SequencingProtocol.md)** *[sequencing protocol➞has attribute](sequencing_protocol_has_attribute.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **[Study](Study.md)** *[study➞has attribute](study_has_attribute.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [attribute➞key](attribute_key.md)  <sub>1..1</sub>
     * Description: The key for an attribute.
     * Range: [String](types/String.md)
 * [attribute➞key type](attribute_key_type.md)  <sub>0..1</sub>
     * Description: A semantic type that characterizes the attribute key. Usually this is a term from an ontology. For example, 'MAXO:0000616' indicates that the attribute is a measurement of oxygen saturation in the blood.
     * Range: [String](types/String.md)
 * [attribute➞value](attribute_value.md)  <sub>1..1</sub>
     * Description: The value for an attribute. Usually this is a numerical value (without the units).
     * Range: [String](types/String.md)
 * [attribute➞value type](attribute_value_type.md)  <sub>0..1</sub>
     * Description: The value type that characterizes the attribute value. Usually this is a term from an ontology that describes how to interpret the value. For example, 'SIO:001413' indicates that the value is to be interpreted as a percentage.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000614 |

