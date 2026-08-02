import kglab
from rdflib_test import Graph
print("running rdflib")
g = Graph()
g.parse('https://example.com')
for s, p, o in g:
   print(s, p, o)


kg = kglab.KnowledgeGraph()

# Load RDF from a URL
kg.load_rdf("taylorswift_graph.rdf", format="xml")

# Measure the graph
measure = kglab.Measure()
measure.measure_graph(kg)

print("Edges:", measure.get_edge_count())
print("Nodes:", measure.get_node_count())

ttl = kg.save_rdf_text()
print(ttl)