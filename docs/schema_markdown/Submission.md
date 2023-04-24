
# Class: Submission


A grouping entity that represents information about one or more entities. A submission can be considered as a set of inter-related (and inter-connected) entities that represent a data submission to GHGA.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Submission](https://w3id.org/GHGA-Submission-Metadata-Schema/Submission)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication]<publications%200..1-++[Submission&#124;id:string;affiliations:string%20%2B;submission_date:string%20%3F;submission_status:string%20%3F],[Member]<members%201..*-++[Submission],[DataAccessCommittee]<data_access_committees%201..*-++[Submission],[DataAccessPolicy]<data_access_policies%201..*-++[Submission],[Dataset]<datasets%201..*-++[Submission],[File]<files%201..*-++[Submission],[Analysis]<analyses%200..*-++[Submission],[LibraryPreparationProtocol]<library_preparation_protocols%200..*-++[Submission],[SequencingProtocol]<sequencing_protocols%200..*-++[Submission],[SequencingExperiment]<sequencing_experiments%200..*-++[Submission],[Individual]<individuals%200..*-++[Submission],[Biospecimen]<biospecimens%200..*-++[Submission],[Sample]<samples%200..*-++[Submission],[Study]<studies%201..*-++[Submission],[Study],[SequencingProtocol],[SequencingExperiment],[Sample],[Publication],[Member],[LibraryPreparationProtocol],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Biospecimen],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Publication]<publications%200..1-++[Submission&#124;id:string;affiliations:string%20%2B;submission_date:string%20%3F;submission_status:string%20%3F],[Member]<members%201..*-++[Submission],[DataAccessCommittee]<data_access_committees%201..*-++[Submission],[DataAccessPolicy]<data_access_policies%201..*-++[Submission],[Dataset]<datasets%201..*-++[Submission],[File]<files%201..*-++[Submission],[Analysis]<analyses%200..*-++[Submission],[LibraryPreparationProtocol]<library_preparation_protocols%200..*-++[Submission],[SequencingProtocol]<sequencing_protocols%200..*-++[Submission],[SequencingExperiment]<sequencing_experiments%200..*-++[Submission],[Individual]<individuals%200..*-++[Submission],[Biospecimen]<biospecimens%200..*-++[Submission],[Sample]<samples%200..*-++[Submission],[Study]<studies%201..*-++[Submission],[Study],[SequencingProtocol],[SequencingExperiment],[Sample],[Publication],[Member],[LibraryPreparationProtocol],[Individual],[File],[Dataset],[DataAccessPolicy],[DataAccessCommittee],[Biospecimen],[Analysis])

## Referenced by Class


## Attributes


### Own

 * [Submission➞id](Submission_id.md)  <sub>1..1</sub>
     * Description: A internal unique identifier for the Submission.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [Submission➞affiliations](Submission_affiliations.md)  <sub>1..\*</sub>
     * Description: Institution/Center/Data Hub that is providing this submission.
     * Range: [String](types/String.md)
 * [Submission➞studies](Submission_studies.md)  <sub>1..\*</sub>
     * Description: Information about a Study entities associated with this submission.
     * Range: [Study](Study.md)
 * [Submission➞samples](Submission_samples.md)  <sub>0..\*</sub>
     * Description: Information about one or more Sample entities associated with this submission.
     * Range: [Sample](Sample.md)
     * in subsets: (restricted)
 * [Submission➞biospecimens](Submission_biospecimens.md)  <sub>0..\*</sub>
     * Description: Information about one or more Biospecimen entities associated with this submission.
     * Range: [Biospecimen](Biospecimen.md)
     * in subsets: (restricted)
 * [Submission➞individuals](Submission_individuals.md)  <sub>0..\*</sub>
     * Description: Information about one or more Individual entities associated with this submission.
     * Range: [Individual](Individual.md)
     * in subsets: (restricted)
 * [Submission➞sequencing_experiments](Submission_sequencing_experiments.md)  <sub>0..\*</sub>
     * Description: Information about one or more Experiment entities associated with this submission.
     * Range: [SequencingExperiment](SequencingExperiment.md)
     * in subsets: (restricted)
 * [Submission➞sequencing_protocols](Submission_sequencing_protocols.md)  <sub>0..\*</sub>
     * Description: One or more sequencing protocol entities associated with this Submission.
     * Range: [SequencingProtocol](SequencingProtocol.md)
 * [Submission➞library_preparation_protocols](Submission_library_preparation_protocols.md)  <sub>0..\*</sub>
     * Description: One or more library preparation protocol entities associated with this Submission.
     * Range: [LibraryPreparationProtocol](LibraryPreparationProtocol.md)
 * [Submission➞analyses](Submission_analyses.md)  <sub>0..\*</sub>
     * Description: Information about one or more Analysis entities associated with this submission.
     * Range: [Analysis](Analysis.md)
     * in subsets: (restricted)
 * [Submission➞files](Submission_files.md)  <sub>1..\*</sub>
     * Description: Information about one or more File entities associated with this submission.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [Submission➞datasets](Submission_datasets.md)  <sub>1..\*</sub>
     * Description: One or more Dataset that are part of this submission.
     * Range: [Dataset](Dataset.md)
 * [Submission➞data_access_policies](Submission_data_access_policies.md)  <sub>1..\*</sub>
     * Description: The Data Access Policy that applies to Dataset in this submission.
     * Range: [DataAccessPolicy](DataAccessPolicy.md)
     * in subsets: (restricted)
 * [Submission➞data_access_committees](Submission_data_access_committees.md)  <sub>1..\*</sub>
     * Description: The Data Access Committee that applies to Dataset in this submission.
     * Range: [DataAccessCommittee](DataAccessCommittee.md)
     * in subsets: (restricted)
 * [Submission➞members](Submission_members.md)  <sub>1..\*</sub>
     * Description: The members associated with a committee referenced in this submission
     * Range: [Member](Member.md)
     * in subsets: (restricted)
 * [Submission➞publications](Submission_publications.md)  <sub>0..1</sub>
     * Description: One or more Publication entities associated with this Submission.
     * Range: [Publication](Publication.md)
 * [submission_date](submission_date.md)  <sub>0..1</sub>
     * Description: The timestamp (in ISO 8601 format) when submission was marked completed.
     * Range: [String](types/String.md)
 * [Submission➞submission_status](Submission_submission_status.md)  <sub>0..1</sub>
     * Description: The status of a Submission.
     * Range: [String](types/String.md)
