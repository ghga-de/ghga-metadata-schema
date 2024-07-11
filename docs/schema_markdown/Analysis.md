
# Class: Analysis


An Analysis is a data transformation that transforms input data to output data.

URI: [GHGA:Analysis](https://w3id.org/GHGA/Analysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[ResearchDataFile],[ProcessDataFile],[IdentifiedByAliasMixin],[AnalysisMethod],[AnalysisMethod]<analysis_methods%201..*-%20[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;ega_accession:string%20%3F;alias:string],[ProcessDataFile]-%20analysis%201..1>[Analysis],[ResearchDataFile]-%20analysis%200..*>[Analysis],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[ResearchDataFile]-%20analysis(i)%200..1>[Analysis],[ProcessDataFile]-%20analysis(i)%200..1>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[ResearchDataFile],[ProcessDataFile],[IdentifiedByAliasMixin],[AnalysisMethod],[AnalysisMethod]<analysis_methods%201..*-%20[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;ega_accession:string%20%3F;alias:string],[ProcessDataFile]-%20analysis%201..1>[Analysis],[ResearchDataFile]-%20analysis%200..*>[Analysis],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[ResearchDataFile]-%20analysis(i)%200..1>[Analysis],[ProcessDataFile]-%20analysis(i)%200..1>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[ProcessDataFile](ProcessDataFile.md)** *[ProcessDataFile➞analysis](ProcessDataFile_analysis.md)*  <sub>1..1</sub>  **[Analysis](Analysis.md)**
 *  **[ResearchDataFile](ResearchDataFile.md)** *[ResearchDataFile➞analysis](ResearchDataFile_analysis.md)*  <sub>0..\*</sub>  **[Analysis](Analysis.md)**
 *  **[Submission](Submission.md)** *[Submission➞analyses](Submission_analyses.md)*  <sub>1..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analyses](analyses.md)*  <sub>0..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analysis](analysis.md)*  <sub>0..1</sub>  **[Analysis](Analysis.md)**

## Attributes


### Own

 * [Analysis➞analysis_methods](Analysis_analysis_methods.md)  <sub>1..\*</sub>
     * Description: The alias of one or more Analysis Methods that are associated with this Analysis.
     * Range: [AnalysisMethod](AnalysisMethod.md)
 * [Analysis➞title](Analysis_title.md)  <sub>1..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [Analysis➞description](Analysis_description.md)  <sub>0..1</sub>
     * Description: A description summarizing how this Analysis was carried out (e.g., computational tools, pipelines, workflows).
     * Range: [String](types/String.md)
 * [Analysis➞type](Analysis_type.md)  <sub>0..1</sub>
     * Description: The type of this Analysis.
     * Range: [String](types/String.md)
 * [Analysis➞ega_accession](Analysis_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession ID of an entity.
     * Range: [String](types/String.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | data analysis |

