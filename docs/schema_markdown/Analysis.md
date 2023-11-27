
# Class: Analysis


An Analysis is a data transformation that transforms input data to output data.

URI: [GHGA:Analysis](https://w3id.org/GHGA/Analysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[AnalysisProcess],[AnalysisProcess]-%20analysis%201..1>[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;reference_genome:string;reference_chromosome:string;alias:string],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[AnalysisProcess]-%20analysis(i)%200..1>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[AnalysisProcess],[AnalysisProcess]-%20analysis%201..1>[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;reference_genome:string;reference_chromosome:string;alias:string],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[AnalysisProcess]-%20analysis(i)%200..1>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[AnalysisProcess](AnalysisProcess.md)** *[AnalysisProcess➞analysis](AnalysisProcess_analysis.md)*  <sub>1..1</sub>  **[Analysis](Analysis.md)**
 *  **[Submission](Submission.md)** *[Submission➞analyses](Submission_analyses.md)*  <sub>1..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analyses](analyses.md)*  <sub>0..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analysis](analysis.md)*  <sub>0..1</sub>  **[Analysis](Analysis.md)**

## Attributes


### Own

 * [Analysis➞title](Analysis_title.md)  <sub>1..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [Analysis➞description](Analysis_description.md)  <sub>0..1</sub>
     * Description: A description summarizing how this Analysis was carried out (e.g., computational tools, pipelines, workflows).
     * Range: [String](types/String.md)
 * [Analysis➞type](Analysis_type.md)  <sub>0..1</sub>
     * Description: The type of this Analysis.
     * Range: [String](types/String.md)
 * [Analysis➞reference_genome](Analysis_reference_genome.md)  <sub>1..1</sub>
     * Description: The reference genome or annotation used for prior analyses (e.g., GRCh38.p13).
     * Range: [String](types/String.md)
 * [Analysis➞reference_chromosome](Analysis_reference_chromosome.md)  <sub>1..1</sub>
     * Description: The reference chromosome used for this Analysis.
     * Range: [String](types/String.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | data analysis |

