# Referencing Ontologies, Controlled Vocabularies, and Thesauri

## Basics

**Controlled Vocabulary**: A Controlled Vocabulary is an organized selection of
words or phrases that are used to tag pieces of information.

**Thesaurus**: A Thesaurus is a form of controlled vocabulary that provides a 
dictionary of synonyms, near-synonyms, and other semantically related terms to
facilitate unambiguous interpretation of terms or concepts.

**Ontology**: An ontology is a formal specification of concepts, from a
particular domain of knowledge, that are arranged in a hierarchy, as a directed
acyclic graph, where concepts are defined in relation to other concepts in
the graph. 

In the biological and biomedical domain, knowledge is organized in
various forms. Some are human readable, some are machine readable,
while seldom few are both human and machine readable. Of the many forms of
knowledge representation, ontologies have been gaining popularity with
several domain specific ontologies being developed in the last two decades.
The most familiar one is the [Gene Ontology](http://geneontology.org/)
that describes functions of gene products.

**OBO Foundry**: The [Open Biological and Biomedical Ontology (OBO) Foundry](http://www.obofoundry.org/)
is a community for developing interoperable ontologies that are logically
well-formed and scientifically accurate. They do so by putting forth a set
of design principles that promotes open-use, collaborative development,
well defined scope, common syntax, and relations. All the well known
ontologies are catalogued in the OBO Foundry.

## Why reference external resources?

In the presence of well developed, curated, and maintained resources, it is
crucial that new projects and initiatives be aware of these resources before
developing new ones.

When developing a new data model or schema, there will always be a need
to be semantically precise. While one can achieve precision by being verbose
with their model, it is immensely beneficial to map elements in their model
to other controlled vocabularies, thesauri, and ontologies.

In the case of GHGA Metadata Schema following are a few reasons
why mapping to external semantic resources would be useful:

- To define our concepts (or classes) in relation to other concepts which are
well defined, richly annotated, and widely used
- To achieve semantic clarity and consistency where when we define a class
as equivalent to a term in an ontology, we are making a statement that the
class is identical in its meaning, not just by its lexical definition but also
by its semantic structure
- To be able to translate external heterogenous data onto our schema
by the way of mappings
- To be able to translate our data to external data models by the way of 
mappings

## How to reference an external concept or term

There are a few things to keep in mind before defining mappings in the GHGA
Metadata Schema.

**URI**: A Uniform Resource Identifier (URI) is a sequence of characters that can
be used to to identify an abstract or a physical resource. URIs can be used to
identify real world objects, concepts, or information resources. URIs are used
by web browsers and are also used to identify any resource described using
the Resource Description Framework (RDF). 

**IRI**: An Internationalized Resource Identifier (IRI) is an extension to a URI
where the sequence of characters are expanded to include international
characters.

**CURIE**: A Compact Uniform Resource Identifier (CURIE) is an abbreviated
representation of a URI/IRI. Such representations are common when describing
resources in RDF, which includes ontologies.

A CURIE is generated by first defining a mapping between the IRI and a 
short prefix. Such a mapping is called a prefix mapping.

For example, `www.example.com` can be mapped to `ex`. 

Systems that are aware of this prefix mapping can then contract IRIs that have
`www.example.com` in it.

For example, `www.example.com/foo` can be contracted to its CURIE
representation of `ex:foo`

**Defining prefix to IRI mappings**

Before we reference external resources, it is crucial that we define the IRI to
prefix mappings for those resources.

Lets say we want to map a class in our schema to the
[Experiment Factor Ontology](https://www.ebi.ac.uk/efo/).

First, we need to check if there exists a mapping from an IRI to the prefix `EFO`
in our default CURI maps (defined via `default_curi_maps` in the schema YAML).

If not, then we should define a mapping in the `prefixes` block. But what is
the base IRI for EFO?

Lets say we want to map a class to the term `EFO:0000311 cancer`, and
the actual IRI for this term is `http://www.ebi.ac.uk/efo/EFO_0000311`.

Here, the base IRI would be `http://www.ebi.ac.uk/efo/EFO_`, such that when
this IRI is contracted to the `EFO` prefix, we get `EFO:0000311`.

Most of the prefix to IRI mappings are already defined by other
open-source initiatives like:

- [Prefix Commons Registry](https://github.com/prefixcommons/biocontext/tree/master/registry)
- [Bioregistry](https://bioregistry.io/)

And these mappings exist in a JSON-LD file.

**Use the defined prefix**

Once the prefix mapping is defined, use the CURIE form of the concept
or term as reference in the GHGA Metadata Schema.
