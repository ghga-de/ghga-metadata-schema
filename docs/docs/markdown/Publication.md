
# Class: publication


The Publication entity represents a publication. While a publication can be any article that is published, the minimum expectation is that the publication has a valid DOI.

URI: [GHGA:Publication](https://w3id.org/GHGA/Publication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Dataset]++-%20has%20publication%200..*>[Publication&#124;title:string%20%3F;abstract:string%20%3F;author:string%20%3F;year:string%20%3F;journal:string%20%3F;id:string;alias:string;xref:string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Submission]-%20has%20publication(i)%200..1>[Publication],[PublicationMixin]-%20has%20publication%200..1>[Publication],[Study]++-%20has%20publication%200..*>[Publication],[Submission]++-%20has%20publication%200..*>[Publication],[InformationContentEntity]^-[Publication],[PublicationMixin],[InformationContentEntity],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[Study],[Dataset]++-%20has%20publication%200..*>[Publication&#124;title:string%20%3F;abstract:string%20%3F;author:string%20%3F;year:string%20%3F;journal:string%20%3F;id:string;alias:string;xref:string%20*;creation_date(i):string%20%3F;update_date(i):string%20%3F;schema_type(i):string%20%3F;schema_version(i):string%20%3F],[Submission]-%20has%20publication(i)%200..1>[Publication],[PublicationMixin]-%20has%20publication%200..1>[Publication],[Study]++-%20has%20publication%200..*>[Publication],[Submission]++-%20has%20publication%200..*>[Publication],[InformationContentEntity]^-[Publication],[PublicationMixin],[InformationContentEntity],[Dataset])

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - A generically dependent continuant that is about some thing.

## Referenced by Class

 *  **[Dataset](Dataset.md)** *[dataset➞has publication](dataset_has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **None** *[has publication](has_publication.md)*  <sub>0..1</sub>  **[Publication](Publication.md)**
 *  **[Study](Study.md)** *[study➞has publication](study_has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **[Submission](Submission.md)** *[submission➞has publication](submission_has_publication.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [publication➞title](publication_title.md)  <sub>0..1</sub>
     * Description: The title for the Publication.
     * Range: [String](types/String.md)
     * in subsets: (essential,public)
 * [publication➞abstract](publication_abstract.md)  <sub>0..1</sub>
     * Description: The study abstract that describes the goals. Can also hold abstract from a publication related to this study.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)
 * [author](author.md)  <sub>0..1</sub>
     * Description: The individual who is responsible for the content of a document version.
     * Range: [String](types/String.md)
 * [year](year.md)  <sub>0..1</sub>
     * Description: Year in which the paper was published.
     * Range: [String](types/String.md)
 * [journal](journal.md)  <sub>0..1</sub>
     * Description: Name of the journal.
     * Range: [String](types/String.md)
 * [publication➞id](publication_id.md)  <sub>1..1</sub>
     * Description: An identifier that uniquely represents an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [publication➞alias](publication_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity.
     * Range: [String](types/String.md)
     * in subsets: (essential,restricted)
 * [publication➞xref](publication_xref.md)  <sub>0..\*</sub>
     * Description: One or more cross-references for this Publication.
     * Range: [String](types/String.md)
     * in subsets: (optional,public)

### Inherited from information content entity:

 * [named thing➞creation date](named_thing_creation_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was created.
     * Range: [String](types/String.md)
 * [named thing➞update date](named_thing_update_date.md)  <sub>0..1</sub>
     * Description: Timestamp (in ISO 8601 format) when the entity was updated.
     * Range: [String](types/String.md)
