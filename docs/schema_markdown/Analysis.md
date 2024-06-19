
# Class: Analysis


An Analysis is a data transformation that transforms input data to output data.

URI: [GHGA:Analysis](https://w3id.org/GHGA/Analysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[ResearchDataFile],[ProcessDataFile],[IdentifiedByAliasMixin],[AnalysisMethod],[ProcessDataFile]<process_data_file%201..1-%20[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;alias:string],[ResearchDataFile]<research_data_file%201..1-%20[Analysis],[AnalysisMethod]<analysis_methods%201..*-%20[Analysis],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[ResearchDataFile],[ProcessDataFile],[IdentifiedByAliasMixin],[AnalysisMethod],[ProcessDataFile]<process_data_file%201..1-%20[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;alias:string],[ResearchDataFile]<research_data_file%201..1-%20[Analysis],[AnalysisMethod]<analysis_methods%201..*-%20[Analysis],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

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
 * [Analysis➞research_data_file](Analysis_research_data_file.md)  <sub>1..1</sub>
     * Description: The alias of one or more Research Data Files that are associated with this Analysis.
     * Range: [ResearchDataFile](ResearchDataFile.md)
 * [Analysis➞process_data_file](Analysis_process_data_file.md)  <sub>1..1</sub>
     * Description: The alias of one or more Process Data Files that are associated with this Analysis.
     * Range: [ProcessDataFile](ProcessDataFile.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | data analysis |

