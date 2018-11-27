import networkx as nx 
import matplotlib.pyplot as plt


G = nx.Graph()

nodes = []
count = 0
with open("Data_for_SocialNetworks.txt", 'r') as fobj:
    for line in fobj:
        numbers = [int(num) for num in line.split()]
        for i in range(1,len(numbers)):
        	G.add_edge(numbers[0],numbers[i])
 


nx.draw(G,with_labels = True)
plt.show()