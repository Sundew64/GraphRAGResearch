import kglab

kg = kglab.KnowledgeGraph()

kg.load_rdf("taylorswift_graph.rdf", format="xml")

measure = kglab.Measure()
measure.measure_graph(kg)

print("Nodes:", measure.get_node_count())
print("Edges:", measure.get_edge_count())

print(kg.save_rdf_text())

#for node in kg.rdf_graph.subjects():
 #   print(node)

for s, p, o in kg.rdf_graph:
    print(s, p, o)

#print(dir(kg))