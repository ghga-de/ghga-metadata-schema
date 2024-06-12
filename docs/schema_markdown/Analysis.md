
# Class: Analysis


An Analysis is a data transformation that transforms input data to output data.

URI: [GHGA:Analysis](https://w3id.org/GHGA/Analysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[ResearchDataFile],[ProcessDataFile],[IdentifiedByAliasMixin],[AnalysisMethod],[AnalysisMethod]<analysis_methods%201..*-%20[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;alias:string],[ProcessDataFile]<process_data_files%201..*-%20[Analysis],[ResearchDataFile]<research_data_files%201..*-%20[Analysis],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[ResearchDataFile],[ProcessDataFile],[IdentifiedByAliasMixin],[AnalysisMethod],[AnalysisMethod]<analysis_methods%201..*-%20[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;alias:string],[ProcessDataFile]<process_data_files%201..*-%20[Analysis],[ResearchDataFile]<research_data_files%201..*-%20[Analysis],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

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
 * [Analysis➞research_data_files](Analysis_research_data_files.md)  <sub>1..\*</sub>
     * Description: The Research Data Files associated with an entity.
     * Range: [ResearchDataFile](ResearchDataFile.md)
 * [Analysis➞process_data_files](Analysis_process_data_files.md)  <sub>1..\*</sub>
     * Description: The Process Files associated with an entity.
     * Range: [ProcessDataFile](ProcessDataFile.md)
 * [Analysis➞analysis_methods](Analysis_analysis_methods.md)  <sub>1..\*</sub>
     * Description: The Analysis Processes associated with an entity.
     * Range: [AnalysisMethod](AnalysisMethod.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | data analysis |

