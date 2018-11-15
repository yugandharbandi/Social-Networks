import networkx as nx
import matplotlib.pyplot as plt 
import random

N = 1000
p = 0.06

G = nx.erdos_renyi_graph(N,p)
L = G.edges()
G1 = nx.Graph()
for i in range(0,N):
	G1.add_node(i)
	
K = [0,1]
for i in L:
	if(random.choice(K)):
		G1.add_edge(i[0],i[1])
count = 0;

for i in range(100):
	a = random.randint(0,N-1)
	while(1):
		b = random.randint(0,N-1)
		if(b != a):
			break
			
	while(1):
		c = random.randint(0,N-1)
		if(c!=a and c!=b ):
			break
	
	s = nx.shortest_path_length(G,a,b)
	t = nx.shortest_path_length(G,a,c)
	if(nx.has_path(G1,a,b) and nx.has_path(G1,a,c)):
		p = nx.shortest_path_length(G1,a,b)
		q = nx.shortest_path_length(G1,a,c)
		if(s<t):
			if(p<q):
				count = count + 1
		else:
			if(p>=q):
				count = count + 1
	
	#print (a,b,c)

print (count/100)

"""	
print (G.number_of_edges())
print (G1.number_of_edges())
nx.draw(G,with_labels=True,edge_color='b')
plt.show()


"""
