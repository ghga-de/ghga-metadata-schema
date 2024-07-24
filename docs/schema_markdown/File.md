
# Class: File


A file is an object that contains information generated from a process, either an Experiment or an Analysis.

URI: [GHGA:File](https://w3id.org/GHGA/File)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ResearchDataFile],[ProcessDataFile],[IndividualSupportingFile],[IdentifiedByAliasMixin],[Dataset]<dataset%201..1-%20[File&#124;name:string;size:integer;checksum:string;checksum_type:string;included_in_submission:boolean;alias:string],[File]uses%20-.->[IdentifiedByAliasMixin],[File]^-[ResearchDataFile],[File]^-[ProcessDataFile],[File]^-[IndividualSupportingFile],[File]^-[ExperimentMethodSupportingFile],[File]^-[AnalysisMethodSupportingFile],[ExperimentMethodSupportingFile],[Dataset],[AnalysisMethodSupportingFile])](https://yuml.me/diagram/nofunky;dir:TB/class/[ResearchDataFile],[ProcessDataFile],[IndividualSupportingFile],[IdentifiedByAliasMixin],[Dataset]<dataset%201..1-%20[File&#124;name:string;size:integer;checksum:string;checksum_type:string;included_in_submission:boolean;alias:string],[File]uses%20-.->[IdentifiedByAliasMixin],[File]^-[ResearchDataFile],[File]^-[ProcessDataFile],[File]^-[IndividualSupportingFile],[File]^-[ExperimentMethodSupportingFile],[File]^-[AnalysisMethodSupportingFile],[ExperimentMethodSupportingFile],[Dataset],[AnalysisMethodSupportingFile])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Children

 * [AnalysisMethodSupportingFile](AnalysisMethodSupportingFile.md) - An Analysis Method Supporting File is a File that contains additional information relevant for the Analysis Method, such as (unstructured) protocols or task descriptions.
 * [ExperimentMethodSupportingFile](ExperimentMethodSupportingFile.md) - An Experiment Method Supporting File is a File that contains additional information relevant for the Experiment Method, such as (unstructured) protocols.
 * [IndividualSupportingFile](IndividualSupportingFile.md) - An Individual Supporting File is a File that contains additional information relevant for the Individual, such as ped-files, phenopackets or imaging data.
 * [ProcessDataFile](ProcessDataFile.md) - A Process Data File is a File that contains data produced by an Analysis or workflow.
 * [ResearchDataFile](ResearchDataFile.md) - A Research Data File is a File that contains raw data originating from an Experiment.

## Referenced by Class


## Attributes


### Own

 * [File➞name](File_name.md)  <sub>1..1</sub>
     * Description: The given filename.
     * Range: [String](types/String.md)
 * [File➞size](File_size.md)  <sub>1..1</sub>
     * Description: The size of the File in bytes.
     * Range: [Integer](types/Integer.md)
 * [File➞checksum](File_checksum.md)  <sub>1..1</sub>
     * Description: The checksum of the File.
     * Range: [String](types/String.md)
 * [File➞checksum_type](File_checksum_type.md)  <sub>1..1</sub>
     * Description: The type of algorithm used to generate the checksum of the File.
     * Range: [String](types/String.md)
 * [File➞dataset](File_dataset.md)  <sub>1..1</sub>
     * Description: The Dataset alias associated with this File.
     * Range: [Dataset](Dataset.md)
 * [File➞included_in_submission](File_included_in_submission.md)  <sub>1..1</sub>
     * Description: Whether a File is included in the Submission or not.
     * Range: [Boolean](types/Boolean.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
