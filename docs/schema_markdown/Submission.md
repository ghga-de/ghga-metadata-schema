
# Class: submission


A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Submission](https://w3id.org/GHGA-Submission-Metadata-Schema/Submission)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication]<has%20publication%200..*-++[Submission&#124;id:string;affiliation:string;submission_date:string%20%3F;submission_status:string%20%3F],[Member]<has%20member%201..*-++[Submission],[DataAccessCommittee]<has%20data%20access%20committee%201..*-++[Submission],[DataAccessPolicy]<has%20data%20access%20policy%201..*-++[Submission],[Dataset]<has%20dataset%201..*-++[Submission],[File]<has%20file%201..*-++[Submission],[Analysis]<has%20analysis%200..*-++[Submission],[Protocol]<has%20protocol%200..*-++[Submission],[SequencingExperiment]<has%20sequencing%20experiment%200..*-++[Submission],[Individual]<has%20individual%200..*-++[Submission],[Biospecimen]<has%20biospecimen%200..*-++[Submission],[Sample]<has%20sample%200..*-++[Submission],[Project]<has%20project%200..1-++[Submission],[Study]<has%20study%201..1-++[Submission],[Study],[SequencingExperiment],[Sample],[Publication],[Protocol],[Project],[Member],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Biospecimen],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication]<has%20publication%200..*-++[Submission&#124;id:string;affiliation:string;submission_date:string%20%3F;submission_status:string%20%3F],[Member]<has%20member%201..*-++[Submission],[DataAccessCommittee]<has%20data%20access%20committee%201..*-++[Submission],[DataAccessPolicy]<has%20data%20access%20policy%201..*-++[Submission],[Dataset]<has%20dataset%201..*-++[Submission],[File]<has%20file%201..*-++[Submission],[Analysis]<has%20analysis%200..*-++[Submission],[Protocol]<has%20protocol%200..*-++[Submission],[SequencingExperiment]<has%20sequencing%20experiment%200..*-++[Submission],[Individual]<has%20individual%200..*-++[Submission],[Biospecimen]<has%20biospecimen%200..*-++[Submission],[Sample]<has%20sample%200..*-++[Submission],[Project]<has%20project%200..1-++[Submission],[Study]<has%20study%201..1-++[Submission],[Study],[SequencingExperiment],[Sample],[Publication],[Protocol],[Project],[Member],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Biospecimen],[Analysis])

## Referenced by Class


## Attributes


### Own

 * [submission➞id](submission_id.md)  <sub>1..1</sub>
     * Description: A internal unique identifier for the Submission.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [submission➞affiliation](submission_affiliation.md)  <sub>1..1</sub>
     * Description: Institution/Center/Data Hub that is providing this submission.
     * Range: [String](types/String.md)
 * [submission➞has study](submission_has_study.md)  <sub>1..1</sub>
     * Description: Information about a Study entities associated with this submission.
     * Range: [Study](Study.md)
 * [submission➞has project](submission_has_project.md)  <sub>0..1</sub>
     * Description: Information about a Project entity associated with this submission.
     * Range: [Project](Project.md)
 * [submission➞has sample](submission_has_sample.md)  <sub>0..\*</sub>
     * Description: Information about one or more Sample entities associated with this submission.
     * Range: [Sample](Sample.md)
     * in subsets: (restricted)
 * [submission➞has biospecimen](submission_has_biospecimen.md)  <sub>0..\*</sub>
     * Description: Information about one or more Biospecimen entities associated with this submission.
     * Range: [Biospecimen](Biospecimen.md)
     * in subsets: (restricted)
 * [submission➞has individual](submission_has_individual.md)  <sub>0..\*</sub>
     * Description: Information about one or more Individual entities associated with this submission.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [submission➞has sequencing experiment](submission_has_sequencing_experiment.md)  <sub>0..\*</sub>
     * Description: Information about one or more Experiment entities associated with this submission.
     * Range: [SequencingExperiment](SequencingExperiment.md)
     * in subsets: (restricted)
 * [submission➞has protocol](submission_has_protocol.md)  <sub>0..\*</sub>
     * Description: One or more Protocol entities associated with this Submission.
     * Range: [Protocol](Protocol.md)
     * in subsets: (restricted)
 * [submission➞has analysis](submission_has_analysis.md)  <sub>0..\*</sub>
     * Description: Information about one or more Analysis entities associated with this submission.
     * Range: [Analysis](Analysis.md)
     * in subsets: (restricted)
 * [submission➞has file](submission_has_file.md)  <sub>1..\*</sub>
     * Description: Information about one or more File entities associated with this submission.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [submission➞has dataset](submission_has_dataset.md)  <sub>1..\*</sub>
     * Description: One or more Dataset that are part of this submission.
     * Range: [Dataset](Dataset.md)
 * [submission➞has data access policy](submission_has_data_access_policy.md)  <sub>1..\*</sub>
     * Description: The Data Access Policy that applies to Dataset in this submission.
     * Range: [DataAccessPolicy](DataAccessPolicy.md)
     * in subsets: (restricted)
 * [submission➞has data access committee](submission_has_data_access_committee.md)  <sub>1..\*</sub>
     * Description: The Data Access Committee that applies to Dataset in this submission.
     * Range: [DataAccessCommittee](DataAccessCommittee.md)
     * in subsets: (restricted)
 * [submission➞has member](submission_has_member.md)  <sub>1..\*</sub>
     * Description: The members associated with a committee referenced in this submission
     * Range: [Member](Member.md)
     * in subsets: (restricted)
 * [submission➞has publication](submission_has_publication.md)  <sub>0..\*</sub>
     * Description: One or more Publication entities associated with this Submission.
     * Range: [Publication](Publication.md)
 * [submission date](submission_date.md)  <sub>0..1</sub>
     * Description: The timestamp (in ISO 8601 format) when submission was marked completed.
     * Range: [String](types/String.md)
 * [submission➞submission status](submission_submission_status.md)  <sub>0..1</sub>
     * Description: The status of a Submission.
     * Range: [String](types/String.md)
