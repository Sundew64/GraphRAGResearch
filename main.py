import kglab

# Create a KnowledgeGraph object
kg = kglab.KnowledgeGraph()

# Load RDF from a URL
kg.load_rdf("https://storage.googleapis.com/kglab-tutorial/foaf.rdf", format="xml")

# Measure the graph
measure = kglab.Measure()
measure.measure_graph(kg)

print("Edges:", measure.get_edge_count())
print("Nodes:", measure.get_node_count())

# Serialize as Turtle/TTL
ttl = kg.save_rdf_text()
print(ttl)