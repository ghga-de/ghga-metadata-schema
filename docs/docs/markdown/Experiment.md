
# Class: experiment


An experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

URI: [GHGA:Experiment](https://w3id.org/GHGA/Experiment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[Protocol],[Investigation],[File],[ExperimentProcess],[ExperimentProcess]<has%20experiment%20process%200..*-++[Experiment&#124;type:string%20%3F;biological_replicates:string%20%3F;technical_replicates:string%20%3F;experimental_replicates:string%20%3F;alias:string;title:string%20%3F;description:string;accession:string%20%3F;ega_accession:string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Protocol]<has%20protocol%201..*-++[Experiment],[File]<has%20file%200..*-++[Experiment],[Sample]<has%20sample%201..*-++[Experiment],[Study]<has%20study%201..1-++[Experiment],[Dataset]++-%20has%20experiment%201..*>[Experiment],[Dataset]-%20has%20experiment(i)%200..1>[Experiment],[Submission]-%20has%20experiment(i)%200..1>[Experiment],[Submission]++-%20has%20experiment%201..*>[Experiment],[Experiment]uses%20-.->[AttributeMixin],[Experiment]uses%20-.->[AccessionMixin],[Experiment]uses%20-.->[EgaAccessionMixin],[Investigation]^-[Experiment],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[Protocol],[Investigation],[File],[ExperimentProcess],[ExperimentProcess]<has%20experiment%20process%200..*-++[Experiment&#124;type:string%20%3F;biological_replicates:string%20%3F;technical_replicates:string%20%3F;experimental_replicates:string%20%3F;alias:string;title:string%20%3F;description:string;accession:string%20%3F;ega_accession:string%20%3F;id(i):string;xref(i):string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Protocol]<has%20protocol%201..*-++[Experiment],[File]<has%20file%200..*-++[Experiment],[Sample]<has%20sample%201..*-++[Experiment],[Study]<has%20study%201..1-++[Experiment],[Dataset]++-%20has%20experiment%201..*>[Experiment],[Dataset]-%20has%20experiment(i)%200..1>[Experiment],[Submission]-%20has%20experiment(i)%200..1>[Experiment],[Submission]++-%20has%20experiment%201..*>[Experiment],[Experiment]uses%20-.->[AttributeMixin],[Experiment]uses%20-.->[AccessionMixin],[Experiment]uses%20-.->[EgaAccessionMixin],[Investigation]^-[Experiment],[EgaAccessionMixin],[Dataset],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.

## Referenced by Class

 *  **[Dataset](Dataset.md)** *[dataset➞has experiment](dataset_has_experiment.md)*  <sub>1..\*</sub>  **[Experiment](Experiment.md)**
 *  **None** *[has experiment](has_experiment.md)*  <sub>0..1</sub>  **[Experiment](Experiment.md)**
 *  **[Submission](Submission.md)** *[submission➞has experiment](submission_has_experiment.md)*  <sub>1..\*</sub>  **[Experiment](Experiment.md)**

## Attributes


### Own

 * [experiment➞type](experiment_type.md)  <sub>0..1</sub>
     * Description: The type of Experiment.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [biological replicates](biological_replicates.md)  <sub>0..1</sub>
     * Description: A biological replicate is a replicate role that consists of independent biological replicates made from different individual biosamples.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [technical replicates](technical_replicates.md)  <sub>0..1</sub>
     * Description: A technical replicate is a replicate role where the same BioSample is use e.g. the same pool of RNA used to assess technical (as opposed to biological) variation within an experiment.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [experimental replicates](experimental_replicates.md)  <sub>0..1</sub>
     * Description: The replicate number of the assay, i.e. the numeric iteration for the assay that was repeated.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [experiment➞has study](experiment_has_study.md)  <sub>1..1</sub>
     * Description: The Study entity associated with this Experiment.
     * Range: [Study](Study.md)
     * in subsets: (essential,public)
 * [experiment➞has sample](experiment_has_sample.md)  <sub>1..\*</sub>
     * Description: The Sample entity associated with this Experiment.
     * Range: [Sample](Sample.md)
     * in subsets: (essential,restricted)
 * [experiment➞has file](experiment_has_file.md)  <sub>0..\*</sub>
     * Description: One or more Files entities that are generated as output of this Experiment.
     * Range: [File](File.md)
     * in subsets: (essential,restricted)
 * [experiment➞has protocol](experiment_has_protocol.md)  <sub>1..\*</sub>
     * Description: One or more Protocol entities associated with this Experiment.
     * Range: [Protocol](Protocol.md)
     * in subsets: (essential,restricted)
 * [experiment➞has experiment process](experiment_has_experiment_process.md)  <sub>0..\*</sub>
     * Description: One or more Experiment Processes entities associated with this Experiment.
     * Range: [ExperimentProcess](ExperimentProcess.md)
     * in subsets: (essential,restricted)
 * [experiment➞alias](experiment_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [experiment➞title](experiment_title.md)  <sub>0..1</sub>
     * Description: Name for the experiment (eg: GHGAE_PBMC_RNAseq).
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [experiment➞description](experiment_description.md)  <sub>1..1</sub>
     * Description: A detailed description of the Experiment.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)

### Inherited from investigation:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (optional,restricted)

### Mixed in from accession mixin:

 * [accession](accession.md)  <sub>0..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession](ega_accession.md)  <sub>0..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000994 |

