from rdflib import Graph
print("running rdflib")
g = Graph()
g.parse('https://example.com')
for s, p, o in g:
   print(s, p, o)