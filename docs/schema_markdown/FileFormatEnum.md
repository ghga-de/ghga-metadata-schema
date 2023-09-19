
# Enum: FileFormatEnum


Enum to capture file types.

URI: [GHGA:FileFormatEnum](https://w3id.org/GHGA/FileFormatEnum)


## Other properties

|  |  |  |
| --- | --- | --- |

## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| AGP | AGP is a tabular format for a sequence assembly (a contig, a scaffold/supercontig, or a chromosome). | format_3693 |  |
| BAI | BAM indexing format | format:3327 |  |
| BAM | BAM format, the binary, BGZF-formatted compressed version of SAM format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s).  May contain base-call and alignment qualities and other data. | format:2572 |  |
| BCF | BCF, the binary version of Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation). | format:3020 |  |
| BED | Browser Extensible Data (BED) format of sequence annotation track, typically to be displayed in a genome browser. BED detail format includes 2 additional columns (http://genome.ucsc.edu/FAQ/FAQformat#format1.7) and BED 15 includes 3 additional columns for experiment scores (http://genomewiki.ucsc.edu/index.php/Microarray_track). | format:3003 |  |
| CRAM | Reference-based compression of alignment format. | format:3462 |  |
| CSV | Tabular data represented as comma-separated values in a text file. | format:3752 |  |
| FASTA | FASTA format including NCBI-style IDs. | format:1929 |  |
| FASTQ | FASTQ short read format ignoring quality scores. | format:1930 |  |
| GFF | GFF feature format (of indeterminate version). | format:2305 |  |
| HDF5 | HDF5 is a data model, library, and file format for storing and managing data, based on Hierarchical Data Format (HDF).  An HDF5 file appears to the user as a directed graph. The nodes of this graph are the higher-level HDF5 objects that are exposed by the HDF5 APIs: Groups, Datasets, Named datatypes. Currently supported by the Python MDTraj package. HDF5 is the new version, according to the HDF group, a completely different technology (https://support.hdfgroup.org/products/hdf4/ compared to HDF. | format:3590 |  |
| JSON | JavaScript Object Notation format; a lightweight, text-based format to represent tree-structured data using key-value pairs. | format:3464 |  |
| PED | The PED file describes individuals and genetic data and is used by the Plink package. | format:3286 |  |
| SAM | Sequence Alignment/Map (SAM) format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data. The format supports short and long reads (up to 128Mbp) produced by different sequencing platforms and is used to hold mapped data within the GATK and across the Broad Institute, the Sanger Centre, and throughout the 1000 Genomes project. | format:2573 |  |
| SFF | Standard flowgram format (SFF) is a binary file format used to encode results of pyrosequencing from the 454 Life Sciences platform for high-throughput sequencing. | format:3284 |  |
| SRF | Sequence Read Format (SRF) of sequence trace data. Supports submission to the NCBI Short Read Archive. | format:3017 |  |
| TABIX | TAB-delimited genome position file index format. | format:3616 |  |
| TSV | Tabular data represented as tab-separated values in a text file. | format:3475 |  |
| TXT | Textual format. Data in text format can be compressed into binary format, or can be a value of an XML element or attribute. Markup formats are not considered textual (or more precisely, not plain-textual). | format:2330 |  |
| VCF | Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation). | format:3016 |  |
| WIG | Wiggle format (WIG) of a sequence annotation track that consists of a value for each sequence position. Typically to be displayed in a genome browser. | format:3005 |  |
| OTHER | A file format not captured by the controlled vocabulary. |  |  |

