
# Enum: DataUseModifierEnum


Permitted values for data use modifier

URI: [GHGA:DataUseModifierEnum](https://w3id.org/GHGA/DataUseModifierEnum)


## Other properties

|  |  |  |
| --- | --- | --- |

## Permissible Values

| Text | Description | Meaning | Other Information |
| :--- | :---: | :---: | ---: |
| clinical care use | This data use modifier indicates that use is allowed for clinical use and care.  Clinical Care is defined as Health care or services provided at home, in a healthcare facility or hospital. Data may be used for clinical decision making. | DUO:0000043 |  |
| RETURN_TO_DATABASE_OR_RESOURCE | This data use modifier indicates that the requestor must return derived/enriched data to the database/resource. | DUO:0000029 |  |
| INSTITUTION_SPECIFIC_RESTRICTION | This data use modifier indicates that use is limited to use within an approved institution. | DUO:0000028 |  |
| PROJECT_SPECIFIC_RESTRICTION | This data use modifier indicates that use is limited to use within an approved project. | DUO:0000027 |  |
| USER_SPECIFIC_RESTRICTION | This data use modifier indicates that use is limited to use by approved users. | DUO:0000026 |  |
| TIME_LIMIT_ON_USE | This data use modifier indicates that use is approved for a specific number of months. This should be coupled with an integer value indicating the number of months. | DUO:0000025 |  |
| PUBLICATION_MORATORIUM | This data use modifier indicates that requestor agrees not to publish results of studies until a specific date. This should be coupled with a date specified as ISO8601. | DUO:0000024 |  |
| GEOGRAPHICAL_RESTRICTION | This data use modifier indicates that use is limited to within a specific geographic region. This should be coupled with an ontology term describing the geographical location the restriction applies to. | DUO:0000022 |  |
| ETHICS_APPROVAL_REQUIRED | This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval. | DUO:0000021 |  |
| COLLABORATION_REQUIRED | This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s). This could be coupled with a string describing the primary study investigator(s). | DUO:0000020 |  |
| PUBLICATION_REQUIRED | This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community. | DUO:0000019 |  |
| NOT_FOR_PROFIT_NON_COMMERCIAL_USE_ONLY | This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use. | DUO:0000018 |  |
| NON_COMMERCIAL_USE_ONLY | This data use modifier indicates that use of the data is limited to not-for-profit use. This indicates that data can be used by commercial organisations for research purposes, but not commercial purposes. | DUO:0000046 |  |
| NOT_FOR_PROFIT_ORGANISATION_USE_ONLY | This data use modifier indicates that use of the data is limited to not-for-profit organizations. | DUO:0000045 |  |
| GENETIC_STUDIES_ONLY | This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively). | DUO:0000016 |  |
| NO_GENERAL_METHODS_RESEARCH | This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms). | DUO:0000015 |  |
| RESEARCH_SPECIFIC_RESTRICTIONS | This data use modifier indicates that use is limited to studies of a certain research type. | DUO:0000012 |  |
| POPULATION_ORIGINS_OR_ANCESTRY_RESEARCH_PROHIBITED | This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited. | DUO:00000044 |  |

