
# Class: Publication


A Publication represents an article that is published. The minimum expectation is that the publication has a valid DOI.

URI: [GHGA:Publication](https://w3id.org/GHGA/Publication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Study]<study%201..1-%20[Publication&#124;title:string%20%3F;abstract:string%20%3F;author:string%20%3F;year:integer%20%3F;journal:string%20%3F;doi:string;xref:string%20*;alias:string],[Submission]++-%20publications%201..*>[Publication],[Submission]-%20publications(i)%200..*>[Publication],[Publication]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Study]<study%201..1-%20[Publication&#124;title:string%20%3F;abstract:string%20%3F;author:string%20%3F;year:integer%20%3F;journal:string%20%3F;doi:string;xref:string%20*;alias:string],[Submission]++-%20publications%201..*>[Publication],[Submission]-%20publications(i)%200..*>[Publication],[Publication]uses%20-.->[IdentifiedByAliasMixin],[IdentifiedByAliasMixin])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Submission](Submission.md)** *[Submission➞publications](Submission_publications.md)*  <sub>1..\*</sub>  **[Publication](Publication.md)**
 *  **None** *[publications](publications.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [Publication➞study](Publication_study.md)  <sub>1..1</sub>
     * Description: The Study entity associated with this Publication.
     * Range: [Study](Study.md)
 * [Publication➞title](Publication_title.md)  <sub>0..1</sub>
     * Description: The title for this Publication.
     * Range: [String](types/String.md)
 * [Publication➞abstract](Publication_abstract.md)  <sub>0..1</sub>
     * Description: The study abstract that describes the goals. Can also hold abstract from a publication related to this Study
     * Range: [String](types/String.md)
 * [Publication➞author](Publication_author.md)  <sub>0..1</sub>
     * Description: Author(s) of this Publication.
     * Range: [String](types/String.md)
 * [Publication➞year](Publication_year.md)  <sub>0..1</sub>
     * Description: The year in which the paper was published.
     * Range: [Integer](types/Integer.md)
 * [Publication➞journal](Publication_journal.md)  <sub>0..1</sub>
     * Description: The name of the journal.
     * Range: [String](types/String.md)
 * [Publication➞doi](Publication_doi.md)  <sub>1..1</sub>
     * Description: DOI identifier of a publication.
     * Range: [String](types/String.md)
 * [Publication➞xref](Publication_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Publication.
     * Range: [String](types/String.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
