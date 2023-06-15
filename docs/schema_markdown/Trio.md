
# Class: Trio


A trio is defined by three individuals representing an individual and their parents.

URI: [GHGA:Trio](https://w3id.org/GHGA/Trio)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual]<child%201..1-%20[Trio],[Individual]<father%201..1-%20[Trio],[Individual]<mother%201..1-%20[Trio],[Submission]++-%20trios%201..*>[Trio],[Submission]++-%20trios(i)%200..*>[Trio],[Submission],[Individual])](https://yuml.me/diagram/nofunky;dir:TB/class/[Individual]<child%201..1-%20[Trio],[Individual]<father%201..1-%20[Trio],[Individual]<mother%201..1-%20[Trio],[Submission]++-%20trios%201..*>[Trio],[Submission]++-%20trios(i)%200..*>[Trio],[Submission],[Individual])

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
