import networkx as nx
import matplotlib.pyplot as plt 
import random
import math

G = nx.read_edgelist("facebook_combined.txt",nodetype=int)
L = G.edges()
N = len(G.nodes())
K = 95;
flag = math.ceil((K*len(L))/100)
p = 0;
G1 = nx.Graph()
random.shuffle(L)
for i in L:
	G1.add_edge(i[0],i[1])
  p = p+1
  if p == flag:
  	break
  	

flag1 = 0;

while(flag1 != 100):
	a = random.randint(0,N-1)
	while(1):
		b = random.randint(0,N-1)
		if(b != a):
			break
			
	while(1):
		c = random.randint(0,N-1)
		if(c!=a and c!=b ):
			break
			
	if(nx.has_path(G,a,b) and nx.has_path(G,a,c)):
		s = nx.shortest_path_length(G,a,b)
		t = nx.shortest_path_length(G,a,c)
		if(nx.has_path(G1,a,b) and nx.has_path(G1,a,c)):
			p = nx.shortest_path_length(G1,a,b)
			q = nx.shortest_path_length(G1,a,c)
			flag1 = flag1 + 1
			if(s<t):
				if(p<q):
					count = count + 1
			else:
				if(p>=q):
					count = count + 1
	

print (count/100)

