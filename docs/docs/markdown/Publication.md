
# Class: publication


The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.

URI: [GHGA:Publication](https://w3id.org/GHGA/Publication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[PublicationMixin],[Dataset]++-%20has%20publication%200..*>[Publication&#124;title:string;abstract:string%20%3F;author:string;year:integer;journal:string;xref:string%20*;id(i):string;alias(i):string;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[Study]-%20has%20publication(i)%200..1>[Publication],[Submission]-%20has%20publication(i)%200..1>[Publication],[PublicationMixin]-%20has%20publication(i)%200..1>[Publication],[PublicationMixin]-%20has%20publication%201..1>[Publication],[Study]++-%20has%20publication%200..*>[Publication],[Submission]++-%20has%20publication%200..*>[Publication],[InformationContentEntity]^-[Publication],[InformationContentEntity],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[PublicationMixin],[Dataset]++-%20has%20publication%200..*>[Publication&#124;title:string;abstract:string%20%3F;author:string;year:integer;journal:string;xref:string%20*;id(i):string;alias(i):string;creation_date(i):string;update_date(i):string;schema_type(i):string;schema_version(i):string],[Study]-%20has%20publication(i)%200..1>[Publication],[Submission]-%20has%20publication(i)%200..1>[Publication],[PublicationMixin]-%20has%20publication(i)%200..1>[Publication],[PublicationMixin]-%20has%20publication%201..1>[Publication],[Study]++-%20has%20publication%200..*>[Publication],[Submission]++-%20has%20publication%200..*>[Publication],[InformationContentEntity]^-[Publication],[InformationContentEntity],[Dataset])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Referenced by Class

 *  **[Dataset](Dataset.md)** *[dataset➞has publication](dataset_has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **None** *[has publication](has_publication.md)*  <sub>0..1</sub>  **[Publication](Publication.md)**
 *  **[PublicationMixin](PublicationMixin.md)** *[publication mixin➞has publication](publication_mixin_has_publication.md)*  <sub>1..1</sub>  **[Publication](Publication.md)**
 *  **[Study](Study.md)** *[study➞has publication](study_has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **[Submission](Submission.md)** *[submission➞has publication](submission_has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [publication➞title](publication_title.md)  <sub>1..1</sub>
     * Description: The title for the Publication.
     * Range: [String](types/String.md)
 * [publication➞abstract](publication_abstract.md)  <sub>0..1</sub>
     * Description: The study abstract that describes the goals. Can also hold abstract from a publication related to this study.
     * Range: [String](types/String.md)
 * [publication➞author](publication_author.md)  <sub>1..1</sub>
     * Description: The individual who is responsible for the content of a document version.
     * Range: [String](types/String.md)
 * [publication➞year](publication_year.md)  <sub>1..1</sub>
     * Description: Year in which the paper was published.
     * Range: [Integer](types/Integer.md)
 * [publication➞journal](publication_journal.md)  <sub>1..1</sub>
     * Description: Name of the journal.
     * Range: [String](types/String.md)
 * [publication➞xref](publication_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Publication.
     * Range: [String](types/String.md)

### Inherited from information content entity:

 * [named thing➞id](named_thing_id.md)  <sub>1..1</sub>
     * Description: The internal unique identifier for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞alias](named_thing_alias.md)  <sub>1..1</sub>
     * Description: The alias (alternate identifier) for an entity.
     * Range: [String](types/String.md)
     * in subsets: (restricted)
 * [named thing➞creation date](named_thing_creation_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>1..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)
