
# Class: ResearchDataFile


A Research Data File is a File that contains raw data originating from an Experiment.

URI: [GHGA:ResearchDataFile](https://w3id.org/GHGA/ResearchDataFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Experiment]<experiment%201..*-%20[ResearchDataFile&#124;format:ResearchDataFileFormatEnum;technical_replicate:integer;sequencing_lane_id:string%20%3F;ega_accession:string%20%3F;name(i):string;included_in_submission(i):boolean;alias(i):string],[Analysis]-%20research_data_files%201..*>[ResearchDataFile],[Submission]++-%20research_data_files%201..*>[ResearchDataFile],[Analysis]-%20research_data_files(i)%200..*>[ResearchDataFile],[Submission]-%20research_data_files(i)%200..*>[ResearchDataFile],[File]^-[ResearchDataFile],[File],[Experiment],[Dataset],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Experiment]<experiment%201..*-%20[ResearchDataFile&#124;format:ResearchDataFileFormatEnum;technical_replicate:integer;sequencing_lane_id:string%20%3F;ega_accession:string%20%3F;name(i):string;included_in_submission(i):boolean;alias(i):string],[Analysis]-%20research_data_files%201..*>[ResearchDataFile],[Submission]++-%20research_data_files%201..*>[ResearchDataFile],[Analysis]-%20research_data_files(i)%200..*>[ResearchDataFile],[Submission]-%20research_data_files(i)%200..*>[ResearchDataFile],[File]^-[ResearchDataFile],[File],[Experiment],[Dataset],[Analysis])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Analysis](Analysis.md)** *[Analysis➞research_data_files](Analysis_research_data_files.md)*  <sub>1..\*</sub>  **[ResearchDataFile](ResearchDataFile.md)**
 *  **[Submission](Submission.md)** *[Submission➞research_data_files](Submission_research_data_files.md)*  <sub>1..\*</sub>  **[ResearchDataFile](ResearchDataFile.md)**
 *  **None** *[research_data_files](research_data_files.md)*  <sub>0..\*</sub>  **[ResearchDataFile](ResearchDataFile.md)**

## Attributes


### Own

 * [ResearchDataFile➞format](ResearchDataFile_format.md)  <sub>1..1</sub>
     * Description: The file format of the Research Data File (e.g., FASTQ, uBAM, FASTA).
     * Range: [ResearchDataFileFormatEnum](ResearchDataFileFormatEnum.md)
 * [ResearchDataFile➞technical_replicate](ResearchDataFile_technical_replicate.md)  <sub>1..1</sub>
     * Description: An integer to indicate the technical replicate of this File.
     * Range: [Integer](types/Integer.md)
 * [ResearchDataFile➞sequencing_lane_id](ResearchDataFile_sequencing_lane_id.md)  <sub>0..1</sub>
     * Description: The identifier of a sequencing lane.
     * Range: [String](types/String.md)
 * [ResearchDataFile➞ega_accession](ResearchDataFile_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession ID of an entity.
     * Range: [String](types/String.md)
 * [ResearchDataFile➞experiment](ResearchDataFile_experiment.md)  <sub>1..\*</sub>
     * Description: The alias of the Experiment that produced this Research Data File.
     * Range: [Experiment](Experiment.md)

### Inherited from File:

 * [File➞name](File_name.md)  <sub>1..1</sub>
     * Description: The given filename.
     * Range: [String](types/String.md)
 * [File➞dataset](File_dataset.md)  <sub>1..1</sub>
     * Description: The Dataset alias associated with this File.
     * Range: [Dataset](Dataset.md)
 * [File➞included_in_submission](File_included_in_submission.md)  <sub>1..1</sub>
     * Description: Whether a File is included in the Submission or not.
     * Range: [Boolean](types/Boolean.md)
