
# Class: experiment


An experiment is an investigation that consists of a coordinated set of actions and observations designed to generate data with the goal of verifying, falsifying, or establishing the validity of a hypothesis.

URI: [https://w3id.org/GHGA-Submission-Metadata-Schema/Experiment](https://w3id.org/GHGA-Submission-Metadata-Schema/Experiment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[Protocol],[Investigation],[File],[Protocol]<has%20protocol%201..*-++[Experiment&#124;type:string%20%3F;biological_replicates:string%20%3F;technical_replicates:string%20%3F;title:string%20%3F;description:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[File]<has%20file%201..*-++[Experiment],[Sample]<has%20sample%201..*-++[Experiment],[Study]<has%20study%201..1-++[Experiment],[Submission]-%20has%20experiment(i)%200..1>[Experiment],[Submission]++-%20has%20experiment%200..*>[Experiment],[Experiment]uses%20-.->[AttributeMixin],[Experiment]uses%20-.->[AccessionMixin],[Experiment]uses%20-.->[EgaAccessionMixin],[Investigation]^-[Experiment],[EgaAccessionMixin],[AttributeMixin],[Attribute],[AccessionMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Sample],[Protocol],[Investigation],[File],[Protocol]<has%20protocol%201..*-++[Experiment&#124;type:string%20%3F;biological_replicates:string%20%3F;technical_replicates:string%20%3F;title:string%20%3F;description:string;accession:string;ega_accession:string;id(i):string;alias(i):string;xref(i):string%20*],[File]<has%20file%201..*-++[Experiment],[Sample]<has%20sample%201..*-++[Experiment],[Study]<has%20study%201..1-++[Experiment],[Submission]-%20has%20experiment(i)%200..1>[Experiment],[Submission]++-%20has%20experiment%200..*>[Experiment],[Experiment]uses%20-.->[AttributeMixin],[Experiment]uses%20-.->[AccessionMixin],[Experiment]uses%20-.->[EgaAccessionMixin],[Investigation]^-[Experiment],[EgaAccessionMixin],[AttributeMixin],[Attribute],[AccessionMixin])

## Parents

 *  is_a: [Investigation](Investigation.md) - Investigation is the process of carrying out a plan or procedure so as to discover fact or information about the object of study.

## Uses Mixin

 *  mixin: [AttributeMixin](AttributeMixin.md) - Mixin for entities that can have one or more attributes.
 *  mixin: [AccessionMixin](AccessionMixin.md) - Mixin for entities that can be assigned a GHGA accession.
 *  mixin: [EgaAccessionMixin](EgaAccessionMixin.md) - Mixin for entities that can be assigned an EGA accession, in addition to GHGA accession.

## Referenced by Class

 *  **None** *[has experiment](has_experiment.md)*  <sub>0..1</sub>  **[Experiment](Experiment.md)**
 *  **[Submission](Submission.md)** *[submission➞has experiment](submission_has_experiment.md)*  <sub>0..\*</sub>  **[Experiment](Experiment.md)**

## Attributes


### Own

 * [experiment➞type](experiment_type.md)  <sub>0..1</sub>
     * Description: The type of Experiment.
     * Range: [String](types/String.md)
 * [experiment➞biological replicates](experiment_biological_replicates.md)  <sub>0..1</sub>
     * Description: A biological replicate is a replicate role that consists of independent biological replicates made from different individual biosamples.
     * Range: [String](types/String.md)
 * [experiment➞technical replicates](experiment_technical_replicates.md)  <sub>0..1</sub>
     * Description: A technical replicate is a replicate role where the same BioSample is use e.g. the same pool of RNA used to assess technical (as opposed to biological) variation within an experiment.
     * Range: [String](types/String.md)
 * [experiment➞has study](experiment_has_study.md)  <sub>1..1</sub>
     * Description: The Study entity associated with this Experiment.
     * Range: [Study](Study.md)
 * [experiment➞has sample](experiment_has_sample.md)  <sub>1..\*</sub>
     * Description: The Sample entity associated with this Experiment.
     * Range: [Sample](Sample.md)
     * in subsets: (restricted)
 * [experiment➞has file](experiment_has_file.md)  <sub>1..\*</sub>
     * Description: One or more Files entities that are generated as output of this Experiment.
     * Range: [File](File.md)
     * in subsets: (restricted)
 * [experiment➞has protocol](experiment_has_protocol.md)  <sub>1..\*</sub>
     * Description: One or more Protocol entities associated with this Experiment.
     * Range: [Protocol](Protocol.md)
     * in subsets: (restricted)
 * [experiment➞title](experiment_title.md)  <sub>0..1</sub>
     * Description: Name for the experiment (eg: GHGAE_PBMC_RNAseq).
     * Range: [String](types/String.md)
 * [experiment➞description](experiment_description.md)  <sub>1..1</sub>
     * Description: A detailed description of the Experiment.
     * Range: [String](types/String.md)

### Inherited from investigation:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞xref](named_thing_xref.md)  <sub>0..\*</sub>
     * Description: Holds one or more database cross references for an entity.
     * Range: [String](types/String.md)

### Mixed in from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: Key/value pairs corresponding to an entity.
     * Range: [Attribute](Attribute.md)
     * in subsets: (restricted)

### Mixed in from accession mixin:

 * [accession mixin➞accession](accession_mixin_accession.md)  <sub>1..1</sub>
     * Description: A unique GHGA identifier assigned to an entity for the sole purpose of referring to that entity in a global scope.
     * Range: [String](types/String.md)

### Mixed in from ega accession mixin:

 * [ega accession mixin➞ega accession](ega_accession_mixin_ega_accession.md)  <sub>1..1</sub>
     * Description: A unique European Genome-Phenome Archive (EGA) identifier assigned to an entity for the sole purpose of referring to that entity within the EGA federated network.
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | SIO:000994 |

