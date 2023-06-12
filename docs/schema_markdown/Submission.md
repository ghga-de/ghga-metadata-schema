
# Class: Submission


A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Submission](https://w3id.org/GHGA-Submission-Metadata-Schema/Submission)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio],[Trio]<trios%201..*-++[Submission],[StudyFile]<study_files%201..*-++[Submission],[Study]<studies%201..*-++[Submission],[SequencingProtocol]<sequencing_protocols%200..*-++[Submission],[SequencingProcess]<sequencing_processes%201..*-++[Submission],[SequencingProcessFile]<sequencing_process_files%201..*-++[Submission],[SequencingExperiment]<sequencing_experiments%200..*-++[Submission],[Sample]<samples%200..*-++[Submission],[SampleFile]<sample_files%201..*-++[Submission],[Publication]<publications%200..*-++[Submission],[Member]<members%201..*-++[Submission],[LibraryPreparationProtocol]<library_preparation_protocols%200..*-++[Submission],[Individual]<individuals%200..*-++[Submission],[Dataset]<datasets%201..*-++[Submission],[DataAccessPolicy]<data_access_policies%201..*-++[Submission],[DataAccessCommittee]<data_access_committees%201..*-++[Submission],[Condition]<conditions%201..*-++[Submission],[Biospecimen]<biospecimens%200..*-++[Submission],[AnalysisProcess]<analysis_processes%201..*-++[Submission],[AnalysisProcessOutputFile]<analysis_process_output_files%201..*-++[Submission],[Analysis]<analyses%200..*-++[Submission],[StudyFile],[Study],[SequencingProtocol],[SequencingProcessFile],[SequencingProcess],[SequencingExperiment],[SampleFile],[Sample],[Publication],[Member],[LibraryPreparationProtocol],[Individual],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[AnalysisProcessOutputFile],[AnalysisProcess],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Trio],[Trio]<trios%201..*-++[Submission],[StudyFile]<study_files%201..*-++[Submission],[Study]<studies%201..*-++[Submission],[SequencingProtocol]<sequencing_protocols%200..*-++[Submission],[SequencingProcess]<sequencing_processes%201..*-++[Submission],[SequencingProcessFile]<sequencing_process_files%201..*-++[Submission],[SequencingExperiment]<sequencing_experiments%200..*-++[Submission],[Sample]<samples%200..*-++[Submission],[SampleFile]<sample_files%201..*-++[Submission],[Publication]<publications%200..*-++[Submission],[Member]<members%201..*-++[Submission],[LibraryPreparationProtocol]<library_preparation_protocols%200..*-++[Submission],[Individual]<individuals%200..*-++[Submission],[Dataset]<datasets%201..*-++[Submission],[DataAccessPolicy]<data_access_policies%201..*-++[Submission],[DataAccessCommittee]<data_access_committees%201..*-++[Submission],[Condition]<conditions%201..*-++[Submission],[Biospecimen]<biospecimens%200..*-++[Submission],[AnalysisProcess]<analysis_processes%201..*-++[Submission],[AnalysisProcessOutputFile]<analysis_process_output_files%201..*-++[Submission],[Analysis]<analyses%200..*-++[Submission],[StudyFile],[Study],[SequencingProtocol],[SequencingProcessFile],[SequencingProcess],[SequencingExperiment],[SampleFile],[Sample],[Publication],[Member],[LibraryPreparationProtocol],[Individual],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Condition],[Biospecimen],[AnalysisProcessOutputFile],[AnalysisProcess],[Analysis])

## Referenced by Class


## Attributes


### Own

 * [Submission➞analyses](Submission_analyses.md)  <sub>0..\*</sub>
     * Description: Information about one or more Analysis entities associated with this submission.
     * Range: [Analysis](Analysis.md)
 * [Submission➞analysis_process_output_files](Submission_analysis_process_output_files.md)  <sub>1..\*</sub>
     * Description: The AnalysisProcessOutputFiles that are part of this submission.
     * Range: [AnalysisProcessOutputFile](AnalysisProcessOutputFile.md)
 * [Submission➞analysis_processes](Submission_analysis_processes.md)  <sub>1..\*</sub>
     * Description: The AnalysisProcesses that are part of this submission.
     * Range: [AnalysisProcess](AnalysisProcess.md)
 * [Submission➞biospecimens](Submission_biospecimens.md)  <sub>0..\*</sub>
     * Description: Information about one or more Biospecimen entities associated with this submission.
     * Range: [Biospecimen](Biospecimen.md)
 * [Submission➞conditions](Submission_conditions.md)  <sub>1..\*</sub>
     * Description: The Conditions associated with this Submission.
     * Range: [Condition](Condition.md)
 * [Submission➞data_access_committees](Submission_data_access_committees.md)  <sub>1..\*</sub>
     * Description: The Data Access Committee that applies to Dataset in this submission.
     * Range: [DataAccessCommittee](DataAccessCommittee.md)
 * [Submission➞data_access_policies](Submission_data_access_policies.md)  <sub>1..\*</sub>
     * Description: The Data Access Policy that applies to Dataset in this submission.
     * Range: [DataAccessPolicy](DataAccessPolicy.md)
 * [Submission➞datasets](Submission_datasets.md)  <sub>1..\*</sub>
     * Description: One or more Dataset that are part of this submission.
     * Range: [Dataset](Dataset.md)
 * [Submission➞individuals](Submission_individuals.md)  <sub>0..\*</sub>
     * Description: Information about one or more Individual entities associated with this submission.
     * Range: [Individual](Individual.md)
 * [Submission➞library_preparation_protocols](Submission_library_preparation_protocols.md)  <sub>0..\*</sub>
     * Description: One or more library preparation protocol entities associated with this Submission.
     * Range: [LibraryPreparationProtocol](LibraryPreparationProtocol.md)
 * [Submission➞members](Submission_members.md)  <sub>1..\*</sub>
     * Description: The members associated with a committee referenced in this submission
     * Range: [Member](Member.md)
 * [Submission➞publications](Submission_publications.md)  <sub>0..\*</sub>
     * Description: One or more Publication entities associated with this Submission.
     * Range: [Publication](Publication.md)
 * [Submission➞sample_files](Submission_sample_files.md)  <sub>1..\*</sub>
     * Description: The SampleFiles that are part of this submission.
     * Range: [SampleFile](SampleFile.md)
 * [Submission➞samples](Submission_samples.md)  <sub>0..\*</sub>
     * Description: Information about one or more Sample entities associated with this submission.
     * Range: [Sample](Sample.md)
 * [Submission➞sequencing_experiments](Submission_sequencing_experiments.md)  <sub>0..\*</sub>
     * Description: Information about one or more Experiment entities associated with this submission.
     * Range: [SequencingExperiment](SequencingExperiment.md)
 * [Submission➞sequencing_process_files](Submission_sequencing_process_files.md)  <sub>1..\*</sub>
     * Description: The SequencingProcessFiles that are part of this submission.
     * Range: [SequencingProcessFile](SequencingProcessFile.md)
 * [Submission➞sequencing_processes](Submission_sequencing_processes.md)  <sub>1..\*</sub>
     * Description: The SequencingProcesses that are part of this submission.
     * Range: [SequencingProcess](SequencingProcess.md)
 * [Submission➞sequencing_protocols](Submission_sequencing_protocols.md)  <sub>0..\*</sub>
     * Description: One or more sequencing protocol entities associated with this Submission.
     * Range: [SequencingProtocol](SequencingProtocol.md)
 * [Submission➞studies](Submission_studies.md)  <sub>1..\*</sub>
     * Description: Information about a Study entities associated with this submission.
     * Range: [Study](Study.md)
 * [Submission➞study_files](Submission_study_files.md)  <sub>1..\*</sub>
     * Description: The StudyFiles that are part of this submission.
     * Range: [StudyFile](StudyFile.md)
 * [Submission➞trios](Submission_trios.md)  <sub>1..\*</sub>
     * Description: The Trios associated with this Submission.
     * Range: [Trio](Trio.md)
