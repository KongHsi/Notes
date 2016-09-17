Graph-tool notes:

creat a graph:
g = Graph(directed = True) #default is true

v1 = g.add_vertex()
v2 = g.add_vertex()
vtuple = g.add_vertex(10) #tuple is a sequence of objects ("1","hi","this")
vlist = list(vtuple)

g.vertex_index[v] #returns v's index



e = g.add_edge(v1,v2) #v1 -> v2
e.source() 
e.target()

#draw the edge out
graph_draw(g,vertex_text = g.vertex_index , vertex_font_size = 18, output_size=(200,200)，output = "two-nodes.png")

print(v1.out_degree()) #in_degree()

g.remove_edge(e)
g.remove_vertex(v2)

v = g.vertex(8) # where 8 is the index, v is the vertex descriptor 
e = g.edge(2,3) # edge descriptor
g.edge_index[e] #returns e's index

for v in g.vertices():
	print(v)
for e in g.edges():
	print (e)
	
v.out_edges()
v.in_edges()
v.out_neighbours()
v.in_neighbours()

# Example for property map:
'''
from itertools import izip
from numpy.random import randint

g = Graph()
g.add_vertex(100)
# insert some random links
for s,t in izip(randint(0, 100, 100), randint(0, 100, 100)):
    g.add_edge(g.vertex(s), g.vertex(t))

vprop_double = g.new_vertex_property("double")            # Double-precision floating point
vprop_double[g.vertex(10)] = 3.1416

vprop_vint = g.new_vertex_property("vector<int>")         # Vector of ints
vprop_vint[g.vertex(40)] = [1, 3, 42, 54]

eprop_dict = g.new_edge_property("object")                # Arbitrary python object.
eprop_dict[g.edges().next()] = {"foo": "bar", "gnu": 42}  # In this case, a dict.

gprop_bool = g.new_graph_property("bool")                  # Boolean
gprop_bool[g] = True

'''

# from itertools import izip  :    izip(3,3) -> (p[0])


#Internal property maps: vp,ep,gp
eprop = g.new_edge_property("string")
>>> g.edge_properties["some name"] = eprop
>>> g.list_properties()
some name      (edge)    (type: string)

#or 

>>> vprop = g.new_vertex_property("double")
>>> g.vp.foo = vprop                        # equivalent to g.vertex_properties["foo"] = vprop
>>> v = g.vertex(0)
>>> g.vp.foo[v] = 3.14
>>> print(g.vp.foo[v])
3.14





