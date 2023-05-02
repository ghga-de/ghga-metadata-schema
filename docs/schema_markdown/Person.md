
# Class: Person


A member of the species Homo sapiens.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Person](https://w3id.org/GHGA-Submission-Metadata-Schema/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Person&#124;given_name:string%20%3F;family_name:string%20%3F;additional_name:string%20%3F]^-[Member],[Person]^-[Individual],[Member],[Individual])](https://yuml.me/diagram/nofunky;dir:TB/class/[Person&#124;given_name:string%20%3F;family_name:string%20%3F;additional_name:string%20%3F]^-[Member],[Person]^-[Individual],[Member],[Individual])

## Children

 * [Individual](Individual.md) - An Individual is a Person who is participating in a Study.
 * [Member](Member.md) - Member of an Organization or a Committee.

## Referenced by Class


## Attributes


### Own

 * [Person➞given_name](Person_given_name.md)  <sub>0..1</sub>
     * Description: First name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Person➞family_name](Person_family_name.md)  <sub>0..1</sub>
     * Description: Last name.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Person➞additional_name](Person_additional_name.md)  <sub>0..1</sub>
     * Description: additional_name(s).
     * Range: [String](types/String.md)
     * in subsets: (restricted)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | NCIT:C25190 |
|  | | SIO:000498 |
|  | | prov:Person |

