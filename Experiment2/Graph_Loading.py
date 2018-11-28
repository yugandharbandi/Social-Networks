import networkx as nx 
import matplotlib.pyplot as plt


Max_Hop = 5
Max_credit = 2**(Max_Hop+1)


def Caluculte_avg_distance_mobile(M1,M2,M3,M4):
	for i in range(0,len(M1)):
		sum1 = 0
		sum2 = 0
		sum3 = 0
		sum4 = 0
		for j in range(0,len(M1)):
			if(i!=j):
				p = len(nx.shortest_path(G,M1[i],M1[j]))
				if p<=Max_Hop:
					sum1 = sum1 + Max_credit*(1-(0.5**p))
		for j in range(0,len(M2)):
			p = len(nx.shortest_path(G,M1[i],M2[j]))
			if p <=Max_Hop:
				sum2 = sum2 + Max_credit*(1-(0.5**p))
		for j in range(0,len(M3)):
			p = len(nx.shortest_path(G,M1[i],M3[j]))
			if p<=Max_Hop:
				sum3 = sum3 + Max_credit*(1-(0.5**p))
		for j in range(0,len(M4)):
			p = len(nx.shortest_path(G,M1[i],M4[j]))
			if p<=Max_Hop:
				sum4 = sum4 + Max_credit*(1-(0.5**p))
		print (sum1/(len(M1)-1) , sum2/len(M2) , sum3/len(M3) , sum4/len(M4))
	print ("\n")


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



M1 = []
M2 = []
M3 = []
M4 = []
S1 = []
S2 = []
S3 = []
S4 = []
C1 = []
C2 = []
C3 = []
mobile=nx.get_node_attributes(G,'mobile')
shoes=nx.get_node_attributes(G,'shoes')
car=nx.get_node_attributes(G,'car')
for i in mobile:
	if (mobile[i] == 1):
		M1.append(i)
	elif (mobile[i] == 2):
		M2.append(i)
	elif (mobile[i] == 3):
		M3.append(i)
	elif (mobile[i] == 4):
		M4.append(i)


for i in shoes:
	if (shoes[i] == 1):
		S1.append(i)
	elif (shoes[i] == 2):
		S2.append(i)
	elif (shoes[i] == 3):
		S3.append(i)
	elif (shoes[i] == 4):
		S4.append(i)

for i in car:
	if (car[i] == 1):
		C1.append(i)
	elif (car[i] == 2):
		C2.append(i)
	elif(car[i] == 3):
		C3.append(i)

"""
Caluculte_avg_distance_mobile(M1,M2,M3,M4)
Caluculte_avg_distance_mobile(M2,M1,M3,M4)
Caluculte_avg_distance_mobile(M3,M1,M3,M4)
Caluculte_avg_distance_mobile(M4,M1,M3,M4)

Caluculte_avg_distance_mobile(S1,S2,S3,S4)
Caluculte_avg_distance_mobile(S2,S1,S3,S4)
Caluculte_avg_distance_mobile(S3,S1,S3,S4)
Caluculte_avg_distance_mobile(S4,S1,S3,S4)
"""


color_map = []
for node in G:
    if node in C1:
        color_map.append('blue')
    elif node in C2:
    	color_map.append('red')
    elif node in C3:
    	color_map.append('orange')
    else:
    	color_map.append('black')   



nx.draw(G,node_color = color_map,with_labels = True)
plt.show()


