
# Class: Submission


A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

URI: [GHGA:Submission](https://w3id.org/GHGA/Submission)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[IndividualSupportingFile]<individual_supporting_files%200..*-++[Submission],[AnalysisMethodSupportingFile]<analysis_method_supporting_files%200..*-++[Submission],[ExperimentMethodSupportingFile]<experiment_method_supporting_files%200..*-++[Submission],[ProcessDataFile]<process_data_files%200..*-++[Submission],[ResearchDataFile]<research_data_files%201..*-++[Submission],[Study]<studies%201..*-++[Submission],[ExperimentMethod]<experiment_methods%201..*-++[Submission],[Experiment]<experiments%201..*-++[Submission],[Sample]<samples%201..*-++[Submission],[Publication]<publications%201..*-++[Submission],[Individual]<individuals%201..*-++[Submission],[Dataset]<datasets%201..*-++[Submission],[DataAccessPolicy]<data_access_policies%201..*-++[Submission],[DataAccessCommittee]<data_access_committees%201..*-++[Submission],[AnalysisMethod]<analysis_methods%201..*-++[Submission],[Analysis]<analyses%201..*-++[Submission],[Study],[Sample],[ResearchDataFile],[Publication],[ProcessDataFile],[IndividualSupportingFile],[Individual],[ExperimentMethodSupportingFile],[ExperimentMethod],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[AnalysisMethodSupportingFile],[AnalysisMethod],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[IndividualSupportingFile]<individual_supporting_files%200..*-++[Submission],[AnalysisMethodSupportingFile]<analysis_method_supporting_files%200..*-++[Submission],[ExperimentMethodSupportingFile]<experiment_method_supporting_files%200..*-++[Submission],[ProcessDataFile]<process_data_files%200..*-++[Submission],[ResearchDataFile]<research_data_files%201..*-++[Submission],[Study]<studies%201..*-++[Submission],[ExperimentMethod]<experiment_methods%201..*-++[Submission],[Experiment]<experiments%201..*-++[Submission],[Sample]<samples%201..*-++[Submission],[Publication]<publications%201..*-++[Submission],[Individual]<individuals%201..*-++[Submission],[Dataset]<datasets%201..*-++[Submission],[DataAccessPolicy]<data_access_policies%201..*-++[Submission],[DataAccessCommittee]<data_access_committees%201..*-++[Submission],[AnalysisMethod]<analysis_methods%201..*-++[Submission],[Analysis]<analyses%201..*-++[Submission],[Study],[Sample],[ResearchDataFile],[Publication],[ProcessDataFile],[IndividualSupportingFile],[Individual],[ExperimentMethodSupportingFile],[ExperimentMethod],[Experiment],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[AnalysisMethodSupportingFile],[AnalysisMethod],[Analysis])

## Referenced by Class


## Attributes


### Own

 * [Submission➞analyses](Submission_analyses.md)  <sub>1..\*</sub>
     * Description: One or more Analysis entities associated with this Submission.
     * Range: [Analysis](Analysis.md)
 * [Submission➞analysis_methods](Submission_analysis_methods.md)  <sub>1..\*</sub>
     * Description: The Analysis Methods that are part of this Submission.
     * Range: [AnalysisMethod](AnalysisMethod.md)
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
 * [Submission➞publications](Submission_publications.md)  <sub>1..\*</sub>
     * Description: One or more Publication entities associated with this Submission.
     * Range: [Publication](Publication.md)
 * [Submission➞samples](Submission_samples.md)  <sub>1..\*</sub>
     * Description: One or more Sample entities associated with this Submission.
     * Range: [Sample](Sample.md)
 * [Submission➞experiments](Submission_experiments.md)  <sub>1..\*</sub>
     * Description: One or more Experiment entities associated with this Submission.
     * Range: [Experiment](Experiment.md)
 * [Submission➞experiment_methods](Submission_experiment_methods.md)  <sub>1..\*</sub>
     * Description: The Experiment Methods that are part of this Submission.
     * Range: [ExperimentMethod](ExperimentMethod.md)
 * [Submission➞studies](Submission_studies.md)  <sub>1..\*</sub>
     * Description: Study entities associated with this Submission.
     * Range: [Study](Study.md)
 * [Submission➞research_data_files](Submission_research_data_files.md)  <sub>1..\*</sub>
     * Description: One or more Research Data Files associated with this Submission.
     * Range: [ResearchDataFile](ResearchDataFile.md)
 * [Submission➞process_data_files](Submission_process_data_files.md)  <sub>0..\*</sub>
     * Description: One or more Process Data Files associated with this Submission.
     * Range: [ProcessDataFile](ProcessDataFile.md)
 * [Submission➞experiment_method_supporting_files](Submission_experiment_method_supporting_files.md)  <sub>0..\*</sub>
     * Description: One or more Experiment Method Supporting Files associated with this Submission.
     * Range: [ExperimentMethodSupportingFile](ExperimentMethodSupportingFile.md)
 * [Submission➞analysis_method_supporting_files](Submission_analysis_method_supporting_files.md)  <sub>0..\*</sub>
     * Description: One or more Analysis Method Supporting Files associated with this Submission.
     * Range: [AnalysisMethodSupportingFile](AnalysisMethodSupportingFile.md)
 * [Submission➞individual_supporting_files](Submission_individual_supporting_files.md)  <sub>0..\*</sub>
     * Description: One or more Individual Supporting Files associated with this Submission.
     * Range: [IndividualSupportingFile](IndividualSupportingFile.md)
