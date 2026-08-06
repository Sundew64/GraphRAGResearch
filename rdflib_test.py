from rdflib import Graph
from rdflib import Namespace
from rdflib import URIRef
from spacy_test import triples_list

g = Graph()
ENTITY = Namespace("http://taylorswiftkg.org/entity/")
REL = Namespace("http://taylorswiftkg.org/relation/")

for subject, predicate, obj in triples_list:
    g.add((
        URIRef(ENTITY + subject.replace(" ", "_")),
        URIRef(REL + predicate.replace(" ", "_")),
        URIRef(ENTITY + obj.replace(" ", "_"))
    ))

g.serialize("taylorswift_graph.5.rdf", format="xml")