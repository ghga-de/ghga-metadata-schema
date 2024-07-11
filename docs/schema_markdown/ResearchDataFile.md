
# Class: ResearchDataFile


A Research Data File is a File that contains raw data originating from an Experiment.

URI: [GHGA:ResearchDataFile](https://w3id.org/GHGA/ResearchDataFile)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Analysis]<analysis%200..*-%20[ResearchDataFile&#124;format:ResearchDataFileFormatEnum;technical_replicate:string;sequencing_lane_id:string%20%3F;is_pseudofile:PseudofileEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Experiment]<experiment%201..*-%20[ResearchDataFile],[Submission]++-%20research_data_files%201..*>[ResearchDataFile],[Submission]-%20research_data_files(i)%200..*>[ResearchDataFile],[File]^-[ResearchDataFile],[File],[Experiment],[Dataset],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Analysis]<analysis%200..*-%20[ResearchDataFile&#124;format:ResearchDataFileFormatEnum;technical_replicate:string;sequencing_lane_id:string%20%3F;is_pseudofile:PseudofileEnum;name(i):string;size(i):integer;checksum(i):string;checksum_type(i):string;alias(i):string],[Experiment]<experiment%201..*-%20[ResearchDataFile],[Submission]++-%20research_data_files%201..*>[ResearchDataFile],[Submission]-%20research_data_files(i)%200..*>[ResearchDataFile],[File]^-[ResearchDataFile],[File],[Experiment],[Dataset],[Analysis])

## Parents

 *  is_a: [File](File.md) - A file is an object that contains information generated from a process, either an Experiment or an Analysis.

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞research_data_files](Submission_research_data_files.md)*  <sub>1..\*</sub>  **[ResearchDataFile](ResearchDataFile.md)**
 *  **None** *[research_data_file](research_data_file.md)*  <sub>0..1</sub>  **[ResearchDataFile](ResearchDataFile.md)**
 *  **None** *[research_data_files](research_data_files.md)*  <sub>0..\*</sub>  **[ResearchDataFile](ResearchDataFile.md)**

## Attributes


### Own

 * [ResearchDataFile➞format](ResearchDataFile_format.md)  <sub>1..1</sub>
     * Description: The file format of the Research Data File (e.g., FASTQ, uBAM, FASTA)
     * Range: [ResearchDataFileFormatEnum](ResearchDataFileFormatEnum.md)
 * [ResearchDataFile➞technical_replicate](ResearchDataFile_technical_replicate.md)  <sub>1..1</sub>
     * Description: An integer to indicate the technical replicate of this File.
     * Range: [String](types/String.md)
 * [ResearchDataFile➞sequencing_lane_id](ResearchDataFile_sequencing_lane_id.md)  <sub>0..1</sub>
     * Description: The identifier of a sequencing lane.
     * Range: [String](types/String.md)
 * [ResearchDataFile➞is_pseudofile](ResearchDataFile_is_pseudofile.md)  <sub>1..1</sub>
     * Description: Whether the Research Data File is a pseudofile or not.
     * Range: [PseudofileEnum](PseudofileEnum.md)
 * [ResearchDataFile➞experiment](ResearchDataFile_experiment.md)  <sub>1..\*</sub>
     * Description: The alias of the Experiment that produced this Research Data File.
     * Range: [Experiment](Experiment.md)
 * [ResearchDataFile➞analysis](ResearchDataFile_analysis.md)  <sub>0..\*</sub>
     * Description: The alias of one or more Analyses that used this Research Data File to generate Process Data Files.
     * Range: [Analysis](Analysis.md)

### Inherited from File:

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
