
# Enum: ProcessDataFileFormatEnum


Enum to capture Process Data File formats.

URI: [GHGA:ProcessDataFileFormatEnum](https://w3id.org/GHGA/ProcessDataFileFormatEnum)


## Other properties

|  |  |  |
| --- | --- | --- |

## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| BAI | BAM indexing format. |  |  |
| BAM | BAM format, the binary, BGZF-formatted compressed version of SAM format for alignment of nucleotide sequences (e.g., sequencing reads) to (a) reference sequence(s).  May contain base-call and alignment qualities and other data. |  |  |
| BCF | BCF, the binary version of Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation). |  |  |
| BED | Browser Extensible Data (BED) format of sequence annotation track, typically to be displayed in a genome browser. BED detail format includes 2 additional columns (http://genome.ucsc.edu/FAQ/FAQformat#format1.7) and BED 15 includes 3 additional columns for experiment scores (http://genomewiki.ucsc.edu/index.php/Microarray_track). |  |  |
| CRAM | Reference-based compression of alignment format. |  |  |
| GFF | GFF feature format (of indeterminate version). |  |  |
| HDF5 | HDF5 is a data model, library, and file format for storing and managing data, based on Hierarchical Data Format (HDF).  An HDF5 file appears to the user as a directed graph. The nodes of this graph are the higher-level HDF5 objects that are exposed by the HDF5 APIs: Groups, Datasets, Named datatypes. Currently supported by the Python MDTraj package. HDF5 is the new version, according to the HDF group, a completely different technology (https://support.hdfgroup.org/products/hdf4/ compared to HDF. |  |  |
| SAM | Sequence Alignment/Map (SAM) format for alignment of nucleotide sequences (e.g., sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data. The format supports short and long reads (up to 128Mbp) produced by different sequencing platforms and is used to hold mapped data within the GATK and across the Broad Institute, the Sanger Centre, and throughout the 1000 Genomes project. |  |  |
| SF | Salmon quantification file. |  |  |
| VCF | Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation). |  |  |
| WIG | Wiggle format (WIG) of a sequence annotation track that consists of a value for each sequence position. Typically to be displayed in a genome browser. |  |  |
| OTHER | A file format not captured by the controlled vocabulary. |  |  |

