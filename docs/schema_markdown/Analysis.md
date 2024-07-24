
# Class: Analysis


An Analysis is a data transformation that transforms input data to output data.

URI: [GHGA:Analysis](https://w3id.org/GHGA/Analysis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[ResearchDataFile],[ProcessDataFile],[IdentifiedByAliasMixin],[AnalysisMethod],[ResearchDataFile]<research_data_files%201..*-%20[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;ega_accession:string%20%3F;alias:string],[AnalysisMethod]<analysis_method%201..1-%20[Analysis],[ProcessDataFile]-%20analysis%201..1>[Analysis],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[ProcessDataFile]-%20analysis(i)%200..1>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[ResearchDataFile],[ProcessDataFile],[IdentifiedByAliasMixin],[AnalysisMethod],[ResearchDataFile]<research_data_files%201..*-%20[Analysis&#124;title:string;description:string%20%3F;type:string%20%3F;ega_accession:string%20%3F;alias:string],[AnalysisMethod]<analysis_method%201..1-%20[Analysis],[ProcessDataFile]-%20analysis%201..1>[Analysis],[Submission]++-%20analyses%201..*>[Analysis],[Submission]-%20analyses(i)%200..*>[Analysis],[ProcessDataFile]-%20analysis(i)%200..1>[Analysis],[Analysis]uses%20-.->[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[ProcessDataFile](ProcessDataFile.md)** *[ProcessDataFile➞analysis](ProcessDataFile_analysis.md)*  <sub>1..1</sub>  **[Analysis](Analysis.md)**
 *  **[Submission](Submission.md)** *[Submission➞analyses](Submission_analyses.md)*  <sub>1..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analyses](analyses.md)*  <sub>0..\*</sub>  **[Analysis](Analysis.md)**
 *  **None** *[analysis](analysis.md)*  <sub>0..1</sub>  **[Analysis](Analysis.md)**

## Attributes


### Own

 * [Analysis➞analysis_method](Analysis_analysis_method.md)  <sub>1..1</sub>
     * Description: The alias of the Analysis Method that is associated with this Analysis.
     * Range: [AnalysisMethod](AnalysisMethod.md)
 * [Analysis➞title](Analysis_title.md)  <sub>1..1</sub>
     * Description: The title that describes an entity.
     * Range: [String](types/String.md)
 * [Analysis➞description](Analysis_description.md)  <sub>0..1</sub>
     * Description: A description summarizing how this Analysis was carried out (e.g., description of computational tools, pipelines, workflows).
     * Range: [String](types/String.md)
 * [Analysis➞type](Analysis_type.md)  <sub>0..1</sub>
     * Description: The type of this Analysis.
     * Range: [String](types/String.md)
 * [Analysis➞ega_accession](Analysis_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession of the 'Analysis' entity (EGAZ).
     * Range: [String](types/String.md)
 * [Analysis➞research_data_files](Analysis_research_data_files.md)  <sub>1..\*</sub>
     * Description: One or more aliases of the Research Data Files that this Analysis used as input to create Process Data Files.
     * Range: [ResearchDataFile](ResearchDataFile.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | data analysis |

