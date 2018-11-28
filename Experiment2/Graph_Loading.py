import networkx as nx 
import matplotlib.pyplot as plt


G = nx.Graph()

nodes = []
count = 0
L = []
previous = 0
with open("Data_for_SocialNetworks.txt", 'r') as fobj:
    for line in fobj:
    	numbers = [int(num) for num in line.split()]
    	if(count%2 == 0):
    		previous = numbers[0]
    		L.append(numbers[0])
    		for i in range(1,len(numbers)):
    			G.add_edge(numbers[0],numbers[i])
    	else:
    		G.node[previous]['mobile'] = numbers[0]
    		G.node[previous]['shoes'] = numbers[1]
    		G.node[previous]['car'] = numbers[2]
    	count=count+1

nodes = G.nodes()
for i in nodes:
	if(i not in L):
		G.node[i]['mobile'] = 0
		G.node[i]['shoes'] = 0
		G.node[i]['car'] = 0


mobile=nx.get_node_attributes(G,'mobile')
print(mobile)


nx.draw(G,with_labels = True)
plt.show()


