
# Class: Attribute


A key/value pair that further characterizes an entity.

URI: [GHGA:Attribute](https://w3id.org/GHGA/Attribute)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[SequencingProtocol],[LibraryPreparationProtocol],[AttributeMixin],[AttributeMixin]++-%20attributes%200..*>[Attribute&#124;key:string;key_type:string%20%3F;value:string;value_type:string%20%3F],[LibraryPreparationProtocol]++-%20attributes%200..*>[Attribute],[SequencingProtocol]++-%20attributes%200..*>[Attribute],[Study]++-%20attributes%200..*>[Attribute],[AttributeMixin]++-%20attributes(i)%200..*>[Attribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study],[SequencingProtocol],[LibraryPreparationProtocol],[AttributeMixin],[AttributeMixin]++-%20attributes%200..*>[Attribute&#124;key:string;key_type:string%20%3F;value:string;value_type:string%20%3F],[LibraryPreparationProtocol]++-%20attributes%200..*>[Attribute],[SequencingProtocol]++-%20attributes%200..*>[Attribute],[Study]++-%20attributes%200..*>[Attribute],[AttributeMixin]++-%20attributes(i)%200..*>[Attribute])

## Referenced by Class

 *  **[AttributeMixin](AttributeMixin.md)** *[AttributeMixin➞attributes](AttributeMixin_attributes.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **[LibraryPreparationProtocol](LibraryPreparationProtocol.md)** *[LibraryPreparationProtocol➞attributes](LibraryPreparationProtocol_attributes.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **[SequencingProtocol](SequencingProtocol.md)** *[SequencingProtocol➞attributes](SequencingProtocol_attributes.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **[Study](Study.md)** *[Study➞attributes](Study_attributes.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**
 *  **None** *[attributes](attributes.md)*  <sub>0..\*</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [Attribute➞key](Attribute_key.md)  <sub>1..1</sub>
     * Description: The key of an attribute.
     * Range: [String](types/String.md)
 * [Attribute➞key_type](Attribute_key_type.md)  <sub>0..1</sub>
     * Description: A semantic type that characterizes the attribute key (e.g., oxygen saturation measurement (MAXO:0000616)).
     * Range: [String](types/String.md)
 * [Attribute➞value](Attribute_value.md)  <sub>1..1</sub>
     * Description: The value for an attribute (e.g., a numerical value without the units).
     * Range: [String](types/String.md)
 * [Attribute➞value_type](Attribute_value_type.md)  <sub>0..1</sub>
     * Description: The value_type that characterizes the attribute value (e.g., percentage (SIO:001413)).
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000614 |

