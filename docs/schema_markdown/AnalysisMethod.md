
# Class: AnalysisMethod


An Analysis Method captures the workflow steps that were performed to analyze data obtained from an Experiment.

URI: [GHGA:AnalysisMethod](https://w3id.org/GHGA/AnalysisMethod)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[Analysis]-%20analysis_methods%201..*>[AnalysisMethod&#124;name:string;description:string;type:string;workflow_name:string;workflow_version:string%20%3F;workflow_repository:string;workflow_doi:string;workflow_tasks:string%20%3F;parameters:string%20%3F;software_versions:string%20%3F;ega_accession:string%20%3F;alias:string],[Submission]++-%20analysis_methods%201..*>[AnalysisMethod],[Analysis]-%20analysis_methods(i)%200..*>[AnalysisMethod],[Submission]-%20analysis_methods(i)%200..*>[AnalysisMethod],[AnalysisMethod]uses%20-.->[IdentifiedByAliasMixin],[Analysis])](https://yuml.me/diagram/nofunky;dir:TB/class/[Submission],[IdentifiedByAliasMixin],[Analysis]-%20analysis_methods%201..*>[AnalysisMethod&#124;name:string;description:string;type:string;workflow_name:string;workflow_version:string%20%3F;workflow_repository:string;workflow_doi:string;workflow_tasks:string%20%3F;parameters:string%20%3F;software_versions:string%20%3F;ega_accession:string%20%3F;alias:string],[Submission]++-%20analysis_methods%201..*>[AnalysisMethod],[Analysis]-%20analysis_methods(i)%200..*>[AnalysisMethod],[Submission]-%20analysis_methods(i)%200..*>[AnalysisMethod],[AnalysisMethod]uses%20-.->[IdentifiedByAliasMixin],[Analysis])

## Uses Mixin

 *  mixin: [IdentifiedByAliasMixin](IdentifiedByAliasMixin.md)

## Referenced by Class

 *  **[Analysis](Analysis.md)** *[Analysis➞analysis_methods](Analysis_analysis_methods.md)*  <sub>1..\*</sub>  **[AnalysisMethod](AnalysisMethod.md)**
 *  **[Submission](Submission.md)** *[Submission➞analysis_methods](Submission_analysis_methods.md)*  <sub>1..\*</sub>  **[AnalysisMethod](AnalysisMethod.md)**
 *  **None** *[analysis_method](analysis_method.md)*  <sub>0..1</sub>  **[AnalysisMethod](AnalysisMethod.md)**
 *  **None** *[analysis_methods](analysis_methods.md)*  <sub>0..\*</sub>  **[AnalysisMethod](AnalysisMethod.md)**

## Attributes


### Own

 * [AnalysisMethod➞name](AnalysisMethod_name.md)  <sub>1..1</sub>
     * Description: The name for an entity.
     * Range: [String](types/String.md)
 * [AnalysisMethod➞description](AnalysisMethod_description.md)  <sub>1..1</sub>
     * Description: Description of an entity.
     * Range: [String](types/String.md)
 * [AnalysisMethod➞type](AnalysisMethod_type.md)  <sub>1..1</sub>
     * Description: The type of an entity. Note: Not to be confused with rdf:type
     * Range: [String](types/String.md)
 * [AnalysisMethod➞workflow_name](AnalysisMethod_workflow_name.md)  <sub>1..1</sub>
     * Description: The workflow name
     * Range: [String](types/String.md)
 * [AnalysisMethod➞workflow_version](AnalysisMethod_workflow_version.md)  <sub>0..1</sub>
     * Description: The workflow version
     * Range: [String](types/String.md)
 * [AnalysisMethod➞workflow_repository](AnalysisMethod_workflow_repository.md)  <sub>1..1</sub>
     * Description: The workflow repository (e.g., the URL)
     * Range: [String](types/String.md)
 * [AnalysisMethod➞workflow_doi](AnalysisMethod_workflow_doi.md)  <sub>1..1</sub>
     * Description: A digital object identifier for the workflow. Can be a publication or the workflow commit that was used for the Analysis.
     * Range: [String](types/String.md)
 * [AnalysisMethod➞workflow_tasks](AnalysisMethod_workflow_tasks.md)  <sub>0..1</sub>
     * Description: Tasks performed by the workflow
     * Range: [String](types/String.md)
 * [AnalysisMethod➞parameters](AnalysisMethod_parameters.md)  <sub>0..1</sub>
     * Description: Non-default parameters and the corresponding value.
     * Range: [String](types/String.md)
 * [AnalysisMethod➞software_versions](AnalysisMethod_software_versions.md)  <sub>0..1</sub>
     * Description: Software used during the Analysis and the corresponding software version.
     * Range: [String](types/String.md)
 * [AnalysisMethod➞ega_accession](AnalysisMethod_ega_accession.md)  <sub>0..1</sub>
     * Description: The EGA accession of the EGA 'Protocol' entity.
     * Range: [String](types/String.md)

### Mixed in from IdentifiedByAliasMixin:

 * [IdentifiedByAliasMixin➞alias](IdentifiedByAliasMixin_alias.md)  <sub>1..1</sub>
     * Description: The alias for an entity at the time of submission.
     * Range: [String](types/String.md)
