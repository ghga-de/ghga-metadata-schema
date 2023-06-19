
# Class: Publication


The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.

URI: [GHGA:Publication](https://w3id.org/GHGA/Publication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Study]<study%201..1-%20[Publication&#124;title:string%20%3F;abstract:string%20%3F;author:string%20%3F;year:integer%20%3F;journal:string%20%3F;doi:string;xref:string%20*],[Submission]++-%20publications%201..*>[Publication],[Submission]++-%20publications(i)%200..*>[Publication])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Study]<study%201..1-%20[Publication&#124;title:string%20%3F;abstract:string%20%3F;author:string%20%3F;year:integer%20%3F;journal:string%20%3F;doi:string;xref:string%20*],[Submission]++-%20publications%201..*>[Publication],[Submission]++-%20publications(i)%200..*>[Publication])

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞publications](Submission_publications.md)*  <sub>1..\*</sub>  **[Publication](Publication.md)**
 *  **None** *[publications](publications.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [Publication➞title](Publication_title.md)  <sub>0..1</sub>
     * Description: The title for the Publication.
     * Range: [String](types/String.md)
 * [Publication➞abstract](Publication_abstract.md)  <sub>0..1</sub>
     * Description: The study abstract that describes the goals. Can also hold abstract from a publication related to this study.
     * Range: [String](types/String.md)
 * [Publication➞author](Publication_author.md)  <sub>0..1</sub>
     * Description: The individual who is responsible for the content of a document version.
     * Range: [String](types/String.md)
 * [Publication➞year](Publication_year.md)  <sub>0..1</sub>
     * Description: Year in which the paper was published.
     * Range: [Integer](types/Integer.md)
 * [Publication➞journal](Publication_journal.md)  <sub>0..1</sub>
     * Description: Name of the journal.
     * Range: [String](types/String.md)
 * [Publication➞doi](Publication_doi.md)  <sub>1..1</sub>
     * Description: DOI identifier of the Publication.
     * Range: [String](types/String.md)
 * [Publication➞study](Publication_study.md)  <sub>1..1</sub>
     * Description: The Study entity associated with this Publication.
     * Range: [Study](Study.md)
 * [Publication➞xref](Publication_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Publication.
     * Range: [String](types/String.md)
