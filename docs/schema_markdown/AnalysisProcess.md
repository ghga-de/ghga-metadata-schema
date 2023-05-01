
# Class: AnalysisProcess




URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/AnalysisProcess](https://w3id.org/GHGA-Submission-Metadata-Schema/AnalysisProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SequencingProcessFile],[AnalysisProcessOutputFile],[SequencingProcessFile]<sequencing_process_files%201..*-%20[AnalysisProcess],[Analysis]<analysis%201..1-%20[AnalysisProcess],[AnalysisProcessOutputFile]++-%20analysis_process%201..1>[AnalysisProcess],[AnalysisProcessOutputFile]++-%20analysis_process(i)%200..1>[AnalysisProcess],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[SequencingProcessFile],[AnalysisProcessOutputFile],[SequencingProcessFile]<sequencing_process_files%201..*-%20[AnalysisProcess],[Analysis]<analysis%201..1-%20[AnalysisProcess],[AnalysisProcessOutputFile]++-%20analysis_process%201..1>[AnalysisProcess],[AnalysisProcessOutputFile]++-%20analysis_process(i)%200..1>[AnalysisProcess],[Analysis])

## Referenced by Class

 *  **[AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)** *[AnalysisProcessOutputFile➞analysis_process](AnalysisProcessOutputFile_analysis_process.md)*  <sub>1..1</sub>  **[AnalysisProcess](AnalysisProcess.md)**
 *  **None** *[analysis_process](analysis_process.md)*  <sub>0..1</sub>  **[AnalysisProcess](AnalysisProcess.md)**

## Attributes


### Own

 * [AnalysisProcess➞analysis](AnalysisProcess_analysis.md)  <sub>1..1</sub>
     * Description: The Analysis the AnalysisProcess was part of
     * Range: [Analysis](Analysis.md)
 * [AnalysisProcess➞sequencing_process_files](AnalysisProcess_sequencing_process_files.md)  <sub>1..\*</sub>
     * Description: The SequencingProcessFiles associated with an entity.
     * Range: [SequencingProcessFile](SequencingProcessFile.md)
