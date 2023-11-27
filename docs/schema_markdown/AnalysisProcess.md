
# Class: AnalysisProcess


An Analysis Process captures the workflow steps that were performed to analyze data obtained from a Sequencing Experiment.

URI: [GHGA:AnalysisProcess](https://w3id.org/GHGA/AnalysisProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[StudyFile],[SequencingProcessFile],[SampleFile],[IdentifiedByAliasMixin],[AnalysisProcessOutputFile],[SequencingProcessFile]<sequencing_process_input_files%200..*-%20[AnalysisProcess&#124;name:string;alias:string],[SampleFile]<sample_input_files%200..*-%20[AnalysisProcess],[StudyFile]<study_input_files%200..*-%20[AnalysisProcess],[Analysis]<analysis%201..1-%20[AnalysisProcess],[AnalysisProcessOutputFile]-%20analysis_process%201..1>[AnalysisProcess],[Submission]++-%20analysis_processes%201..*>[AnalysisProcess],[AnalysisProcessOutputFile]-%20analysis_process(i)%200..1>[AnalysisProcess],[Submission]-%20analysis_processes(i)%200..*>[AnalysisProcess],[AnalysisProcess]uses%20-.->[IdentifiedByAliasMixin],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[StudyFile],[SequencingProcessFile],[SampleFile],[IdentifiedByAliasMixin],[AnalysisProcessOutputFile],[SequencingProcessFile]<sequencing_process_input_files%200..*-%20[AnalysisProcess&#124;name:string;alias:string],[SampleFile]<sample_input_files%200..*-%20[AnalysisProcess],[StudyFile]<study_input_files%200..*-%20[AnalysisProcess],[Analysis]<analysis%201..1-%20[AnalysisProcess],[AnalysisProcessOutputFile]-%20analysis_process%201..1>[AnalysisProcess],[Submission]++-%20analysis_processes%201..*>[AnalysisProcess],[AnalysisProcessOutputFile]-%20analysis_process(i)%200..1>[AnalysisProcess],[Submission]-%20analysis_processes(i)%200..*>[AnalysisProcess],[AnalysisProcess]uses%20-.->[IdentifiedByAliasMixin],[Analysis])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)** *[AnalysisProcessOutputFile➞analysis_process](AnalysisProcessOutputFile_analysis_process.md)*  <sub>1..1</sub>  **[AnalysisProcess](AnalysisProcess.md)**
 *  **[Submission](Submission.md)** *[Submission➞analysis_processes](Submission_analysis_processes.md)*  <sub>1..\*</sub>  **[AnalysisProcess](AnalysisProcess.md)**
 *  **None** *[analysis_process](analysis_process.md)*  <sub>0..1</sub>  **[AnalysisProcess](AnalysisProcess.md)**
 *  **None** *[analysis_processes](analysis_processes.md)*  <sub>0..\*</sub>  **[AnalysisProcess](AnalysisProcess.md)**

## Attributes


### Own

 * [AnalysisProcess➞name](AnalysisProcess_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [AnalysisProcess➞analysis](AnalysisProcess_analysis.md)  <sub>1..1</sub>
     * Description: The Analysis that this Analysis Process is part of.
     * Range: [Analysis](Analysis.md)
 * [AnalysisProcess➞study_input_files](AnalysisProcess_study_input_files.md)  <sub>0..\*</sub>
     * Description: The associated Study File used as an input for this Analysis Process.
     * Range: [StudyFile](StudyFile.md)
 * [AnalysisProcess➞sample_input_files](AnalysisProcess_sample_input_files.md)  <sub>0..\*</sub>
     * Description: The associated Sample File used as an input for this Analysis Process.
     * Range: [SampleFile](SampleFile.md)
 * [AnalysisProcess➞sequencing_process_input_files](AnalysisProcess_sequencing_process_input_files.md)  <sub>0..\*</sub>
     * Description: The associated Sequencing Process File used as an input for this Analysis Process.
     * Range: [SequencingProcessFile](SequencingProcessFile.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
