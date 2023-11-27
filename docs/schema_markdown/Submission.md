
# Class: Submission


A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

URI: [GHGA:Submission](https://w3id.org/GHGA/Submission)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio],[Trio]<trios%201..*-++[Submission],[StudyFile]<study_files%201..*-++[Submission],[Study]<studies%201..*-++[Submission],[SequencingProtocol]<sequencing_protocols%201..*-++[Submission],[SequencingProcess]<sequencing_processes%201..*-++[Submission],[SequencingProcessFile]<sequencing_process_files%201..*-++[Submission],[SequencingExperiment]<sequencing_experiments%201..*-++[Submission],[Sample]<samples%201..*-++[Submission],[SampleFile]<sample_files%201..*-++[Submission],[Publication]<publications%201..*-++[Submission],[LibraryPreparationProtocol]<library_preparation_protocols%201..*-++[Submission],[Individual]<individuals%201..*-++[Submission],[Dataset]<datasets%201..*-++[Submission],[DataAccessPolicy]<data_access_policies%201..*-++[Submission],[DataAccessCommittee]<data_access_committees%201..*-++[Submission],[Condition]<conditions%201..*-++[Submission],[Biospecimen]<biospecimens%201..*-++[Submission],[AnalysisProcess]<analysis_processes%201..*-++[Submission],[AnalysisProcessOutputFile]<analysis_process_output_files%201..*-++[Submission],[Analysis]<analyses%201..*-++[Submission],[StudyFile],[Study],[SequencingProtocol],[SequencingProcessFile],[SequencingProcess],[SequencingExperiment],[SampleFile],[Sample],[Publication],[LibraryPreparationProtocol],[Individual],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[AnalysisProcessOutputFile],[AnalysisProcess],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio],[Trio]<trios%201..*-++[Submission],[StudyFile]<study_files%201..*-++[Submission],[Study]<studies%201..*-++[Submission],[SequencingProtocol]<sequencing_protocols%201..*-++[Submission],[SequencingProcess]<sequencing_processes%201..*-++[Submission],[SequencingProcessFile]<sequencing_process_files%201..*-++[Submission],[SequencingExperiment]<sequencing_experiments%201..*-++[Submission],[Sample]<samples%201..*-++[Submission],[SampleFile]<sample_files%201..*-++[Submission],[Publication]<publications%201..*-++[Submission],[LibraryPreparationProtocol]<library_preparation_protocols%201..*-++[Submission],[Individual]<individuals%201..*-++[Submission],[Dataset]<datasets%201..*-++[Submission],[DataAccessPolicy]<data_access_policies%201..*-++[Submission],[DataAccessCommittee]<data_access_committees%201..*-++[Submission],[Condition]<conditions%201..*-++[Submission],[Biospecimen]<biospecimens%201..*-++[Submission],[AnalysisProcess]<analysis_processes%201..*-++[Submission],[AnalysisProcessOutputFile]<analysis_process_output_files%201..*-++[Submission],[Analysis]<analyses%201..*-++[Submission],[StudyFile],[Study],[SequencingProtocol],[SequencingProcessFile],[SequencingProcess],[SequencingExperiment],[SampleFile],[Sample],[Publication],[LibraryPreparationProtocol],[Individual],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[AnalysisProcessOutputFile],[AnalysisProcess],[Analysis])

## Referenced by Class


## Attributes


### Own

 * [Submission➞analyses](Submission_analyses.md)  <sub>1..\*</sub>
     * Description: One or more Analysis entities associated with this Submission.
     * Range: [Analysis](Analysis.md)
 * [Submission➞analysis_process_output_files](Submission_analysis_process_output_files.md)  <sub>1..\*</sub>
     * Description: The Analysis Process Output Files that are part of this Submission.
     * Range: [AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)
 * [Submission➞analysis_processes](Submission_analysis_processes.md)  <sub>1..\*</sub>
     * Description: The Analysis Processes that are part of this Submission.
     * Range: [AnalysisProcess](AnalysisProcess.md)
 * [Submission➞biospecimens](Submission_biospecimens.md)  <sub>1..\*</sub>
     * Description: One or more Biospecimen entities associated with this Submission.
     * Range: [Biospecimen](Biospecimen.md)
 * [Submission➞conditions](Submission_conditions.md)  <sub>1..\*</sub>
     * Description: One or more Condition entities associated with this Submission.
     * Range: [Condition](Condition.md)
 * [Submission➞data_access_committees](Submission_data_access_committees.md)  <sub>1..\*</sub>
     * Description: The Data Access Committees that apply to the Data Access Policies in this Submission.
     * Range: [DataAccessCommittee](DataAccessCommittee.md)
 * [Submission➞data_access_policies](Submission_data_access_policies.md)  <sub>1..\*</sub>
     * Description: The Data Access Policies that apply to the Datasets in this Submission.
     * Range: [DataAccessPolicy](DataAccessPolicy.md)
 * [Submission➞datasets](Submission_datasets.md)  <sub>1..\*</sub>
     * Description: One or more Dataset entities that are part of this Submission.
     * Range: [Dataset](Dataset.md)
 * [Submission➞individuals](Submission_individuals.md)  <sub>1..\*</sub>
     * Description: One or more Individual entities associated with this Submission.
     * Range: [Individual](Individual.md)
 * [Submission➞library_preparation_protocols](Submission_library_preparation_protocols.md)  <sub>1..\*</sub>
     * Description: One or more Library Preparation Protocol entities associated with this Submission.
     * Range: [LibraryPreparationProtocol](LibraryPreparationProtocol.md)
 * [Submission➞publications](Submission_publications.md)  <sub>1..\*</sub>
     * Description: One or more Publication entities associated with this Submission.
     * Range: [Publication](Publication.md)
 * [Submission➞sample_files](Submission_sample_files.md)  <sub>1..\*</sub>
     * Description: The Sample Files that are part of this submission.
     * Range: [SampleFile](SampleFile.md)
 * [Submission➞samples](Submission_samples.md)  <sub>1..\*</sub>
     * Description: One or more Sample entities associated with this Submission.
     * Range: [Sample](Sample.md)
 * [Submission➞sequencing_experiments](Submission_sequencing_experiments.md)  <sub>1..\*</sub>
     * Description: One or more Sequencing Experiment entities associated with this Submission.
     * Range: [SequencingExperiment](SequencingExperiment.md)
 * [Submission➞sequencing_process_files](Submission_sequencing_process_files.md)  <sub>1..\*</sub>
     * Description: The Sequencing Process Files that are part of this Submission.
     * Range: [SequencingProcessFile](SequencingProcessFile.md)
 * [Submission➞sequencing_processes](Submission_sequencing_processes.md)  <sub>1..\*</sub>
     * Description: The Sequencing Processes that are part of this Submission.
     * Range: [SequencingProcess](SequencingProcess.md)
 * [Submission➞sequencing_protocols](Submission_sequencing_protocols.md)  <sub>1..\*</sub>
     * Description: One or more Sequencing Protocol entities associated with this Submission.
     * Range: [SequencingProtocol](SequencingProtocol.md)
 * [Submission➞studies](Submission_studies.md)  <sub>1..\*</sub>
     * Description: Study entities associated with this Submission.
     * Range: [Study](Study.md)
 * [Submission➞study_files](Submission_study_files.md)  <sub>1..\*</sub>
     * Description: The Study Files that are part of this Submission.
     * Range: [StudyFile](StudyFile.md)
 * [Submission➞trios](Submission_trios.md)  <sub>1..\*</sub>
     * Description: One or more Trio entities associated with this Submission.
     * Range: [Trio](Trio.md)
