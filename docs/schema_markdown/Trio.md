
# Class: Trio


A trio is defined by three individuals representing an individual and their parents.

URI: [GHGA:Trio](https://w3id.org/GHGA/Trio)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual]<child%201..1-%20[Trio&#124;alias:string],[Individual]<father%201..1-%20[Trio],[Individual]<mother%201..1-%20[Trio],[Submission]++-%20trios%201..*>[Trio],[Submission]-%20trios(i)%200..*>[Trio],[Trio]uses%20-.->[IdentifiedByAliasMixin],[Submission],[Individual],[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual]<child%201..1-%20[Trio&#124;alias:string],[Individual]<father%201..1-%20[Trio],[Individual]<mother%201..1-%20[Trio],[Submission]++-%20trios%201..*>[Trio],[Submission]-%20trios(i)%200..*>[Trio],[Trio]uses%20-.->[IdentifiedByAliasMixin],[Submission],[Individual],[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞trios](Submission_trios.md)*  <sub>1..\*</sub>  **[Trio](Trio.md)**
 *  **None** *[trios](trios.md)*  <sub>0..\*</sub>  **[Trio](Trio.md)**

## Attributes


### Own

 * [Trio➞mother](Trio_mother.md)  <sub>1..1</sub>
     * Description: The mother of an individual.
     * Range: [Individual](Individual.md)
 * [Trio➞father](Trio_father.md)  <sub>1..1</sub>
     * Description: The father of an individual.
     * Range: [Individual](Individual.md)
 * [Trio➞child](Trio_child.md)  <sub>1..1</sub>
     * Description: The child of two individuals.
     * Range: [Individual](Individual.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
