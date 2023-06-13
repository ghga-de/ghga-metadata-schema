
# Class: AnalysisProcess




URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/AnalysisProcess](https://w3id.org/GHGA-Submission-Metadata-Schema/AnalysisProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[StudyFile],[SequencingProcessFile],[SampleFile],[AnalysisProcessOutputFile],[SequencingProcessFile]<sequencing_process_input_files%201..*-%20[AnalysisProcess],[SampleFile]<sample_input_files%201..*-%20[AnalysisProcess],[StudyFile]<study_input_files%201..*-%20[AnalysisProcess],[Analysis]<analysis%201..1-++[AnalysisProcess],[AnalysisProcessOutputFile]++-%20analysis_process%201..1>[AnalysisProcess],[Submission]++-%20analysis_processes%201..*>[AnalysisProcess],[AnalysisProcessOutputFile]++-%20analysis_process(i)%200..1>[AnalysisProcess],[Submission]++-%20analysis_processes(i)%200..*>[AnalysisProcess],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[StudyFile],[SequencingProcessFile],[SampleFile],[AnalysisProcessOutputFile],[SequencingProcessFile]<sequencing_process_input_files%201..*-%20[AnalysisProcess],[SampleFile]<sample_input_files%201..*-%20[AnalysisProcess],[StudyFile]<study_input_files%201..*-%20[AnalysisProcess],[Analysis]<analysis%201..1-++[AnalysisProcess],[AnalysisProcessOutputFile]++-%20analysis_process%201..1>[AnalysisProcess],[Submission]++-%20analysis_processes%201..*>[AnalysisProcess],[AnalysisProcessOutputFile]++-%20analysis_process(i)%200..1>[AnalysisProcess],[Submission]++-%20analysis_processes(i)%200..*>[AnalysisProcess],[Analysis])

## Referenced by Class

 *  **[AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)** *[AnalysisProcessOutputFile➞analysis_process](AnalysisProcessOutputFile_analysis_process.md)*  <sub>1..1</sub>  **[AnalysisProcess](AnalysisProcess.md)**
 *  **[Submission](Submission.md)** *[Submission➞analysis_processes](Submission_analysis_processes.md)*  <sub>1..\*</sub>  **[AnalysisProcess](AnalysisProcess.md)**
 *  **None** *[analysis_process](analysis_process.md)*  <sub>0..1</sub>  **[AnalysisProcess](AnalysisProcess.md)**
 *  **None** *[analysis_processes](analysis_processes.md)*  <sub>0..\*</sub>  **[AnalysisProcess](AnalysisProcess.md)**

## Attributes


### Own

 * [AnalysisProcess➞analysis](AnalysisProcess_analysis.md)  <sub>1..1</sub>
     * Description: The Analysis the AnalysisProcess was part of
     * Range: [Analysis](Analysis.md)
 * [AnalysisProcess➞study_input_files](AnalysisProcess_study_input_files.md)  <sub>1..\*</sub>
     * Description: The StudyFile associated used as an input for an entity.
     * Range: [StudyFile](StudyFile.md)
 * [AnalysisProcess➞sample_input_files](AnalysisProcess_sample_input_files.md)  <sub>1..\*</sub>
     * Description: The SampleFile associated used as an input for an entity.
     * Range: [SampleFile](SampleFile.md)
 * [AnalysisProcess➞sequencing_process_input_files](AnalysisProcess_sequencing_process_input_files.md)  <sub>1..\*</sub>
     * Description: The SequencingProcessFile associated used as an input for an entity.
     * Range: [SequencingProcessFile](SequencingProcessFile.md)
