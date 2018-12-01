import networkx as nx 
import matplotlib.pyplot as plt


Max_Hop = 2
Max_credit = 2**(Max_Hop+1)


def Caluculte_avg_distance_mobile(K1,K2,K3,K4):
	Options_Ascending = [0,0,0,0]

	for k in range(0,4):
		if (k==0):	
			M1 = K1
			M2 = K2
			M3 = K3
			M4 = K4
		elif(k==1):
			M1 = K2
			M2 = K1
			M3 = K3
			M4 = K4
		elif(k==2):
			M1 = K3
			M2 = K1
			M3 = K2
			M4 = K4
		elif(k==3):
			M1 = K4
			M2 = K1
			M3 = K3
			M4 = K2
		for i in range(0,len(M1)):
			sum1 = 0
			sum2 = 0
			sum3 = 0
			sum4 = 0
			for j in range(0,len(M1)):
				if(i!=j):
					p = len(nx.shortest_path(G,M1[i],M1[j]))
					if(p<=Max_Hop):
						sum1 = sum1 + p
			for j in range(0,len(M2)):
				p = len(nx.shortest_path(G,M1[i],M2[j]))
				if(p<=Max_Hop):
					sum2 = sum2 + p
			for j in range(0,len(M3)):
				p = len(nx.shortest_path(G,M1[i],M3[j]))
				if(p<=Max_Hop):
					sum3 = sum3 + p
			for j in range(0,len(M4)):
				p = len(nx.shortest_path(G,M1[i],M4[j]))
				if(p<=Max_Hop):
					sum4 = sum4 + p
			L = [sum1/(len(M1)-1) , sum2/len(M2) , sum3/len(M3) , sum4/len(M4)]
			value = sum1/(len(M1)-1)
			for s in range(0,4):
				m = min(L)
				if(m == value):
					Options_Ascending[s] = Options_Ascending[s] + 1
					break
				else:
					L[L.index(m)] = 100000

	return Options_Ascending




def Caluculte_avg_distance_cars(K1,K2,K3):
	Options_Ascending = [0,0,0]

	for k in range(0,3):
		if (k==0):	
			M1 = K1
			M2 = K2
			M3 = K3
		elif(k==1):
			M1 = K2
			M2 = K1
			M3 = K3
		elif(k==2):
			M1 = K3
			M2 = K1
			M3 = K2
		for i in range(0,len(M1)):
			sum1 = 0
			sum2 = 0
			sum3 = 0
			sum4 = 0
			for j in range(0,len(M1)):
				if(i!=j):
					p = len(nx.shortest_path(G,M1[i],M1[j]))
					if(p<=Max_Hop):
						sum1 = sum1 + p
			for j in range(0,len(M2)):
				p = len(nx.shortest_path(G,M1[i],M2[j]))
				if(p<=Max_Hop):
					sum2 = sum2 + p
			for j in range(0,len(M3)):
				p = len(nx.shortest_path(G,M1[i],M3[j]))
				if(p<=Max_Hop):
					sum3 = sum3 + p
			L = [sum1/(len(M1)-1) , sum2/len(M2) , sum3/len(M3)]
			value = sum1/(len(M1)-1)
			for s in range(0,3):
				m = min(L)
				if(m == value):
					Options_Ascending[s] = Options_Ascending[s] + 1
					break
				else:
					L[L.index(m)] = 100000

	return Options_Ascending




def Caluculte_LinearReduction_mobile(K1,K2,K3,K4,d):
	Options_Ascending = [0,0,0,0]

	for k in range(0,4):
		if (k==0):	
			M1 = K1
			M2 = K2
			M3 = K3
			M4 = K4
		elif(k==1):
			M1 = K2
			M2 = K1
			M3 = K3
			M4 = K4
		elif(k==2):
			M1 = K3
			M2 = K1
			M3 = K2
			M4 = K4
		elif(k==3):
			M1 = K4
			M2 = K1
			M3 = K3
			M4 = K2
		for i in range(0,len(M1)):
			sum1 = 0
			sum2 = 0
			sum3 = 0
			sum4 = 0
			for j in range(0,len(M1)):
				if(i!=j):
					p = len(nx.shortest_path(G,M1[i],M1[j]))
					if(p<=Max_Hop):
						sum1 = sum1 + p+(p*(p-1)*d)/2
			for j in range(0,len(M2)):
				p = len(nx.shortest_path(G,M1[i],M2[j]))
				if(p<=Max_Hop):
					sum2 = sum2 + p+(p*(p-1)*d)/2
			for j in range(0,len(M3)):
				p = len(nx.shortest_path(G,M1[i],M3[j]))
				if(p<=Max_Hop):
					sum3 = sum3 + p+(p*(p-1)*d)/2
			for j in range(0,len(M4)):
				p = len(nx.shortest_path(G,M1[i],M4[j]))
				if(p<=Max_Hop):
					sum4 = sum4 + p +(p*(p-1)*d)/2
			L = [sum1/(len(M1)-1) , sum2/len(M2) , sum3/len(M3) , sum4/len(M4)]
			value = sum1/(len(M1)-1)
			for s in range(0,4):
				m = min(L)
				if(m == value):
					Options_Ascending[s] = Options_Ascending[s] + 1
					break
				else:
					L[L.index(m)] = 100000

	return Options_Ascending




def Caluculte_LinearReduction_cars(K1,K2,K3,d):
	Options_Ascending = [0,0,0]

	for k in range(0,3):
		if (k==0):	
			M1 = K1
			M2 = K2
			M3 = K3
		elif(k==1):
			M1 = K2
			M2 = K1
			M3 = K3
		elif(k==2):
			M1 = K3
			M2 = K1
			M3 = K2
		for i in range(0,len(M1)):
			sum1 = 0
			sum2 = 0
			sum3 = 0
			sum4 = 0
			for j in range(0,len(M1)):
				if(i!=j):
					p = len(nx.shortest_path(G,M1[i],M1[j]))
					if(p<=Max_Hop):
						sum1 = sum1 + p +(p*(p-1)*d)/2
			for j in range(0,len(M2)):
				p = len(nx.shortest_path(G,M1[i],M2[j]))
				if(p<=Max_Hop):
					sum2 = sum2 + p +(p*(p-1)*d)/2
			for j in range(0,len(M3)):
				p = len(nx.shortest_path(G,M1[i],M3[j]))
				if(p<=Max_Hop):
					sum3 = sum3 + p +(p*(p-1)*d)/2
			L = [sum1/(len(M1)-1) , sum2/len(M2) , sum3/len(M3)]
			value = sum1/(len(M1)-1)
			for s in range(0,3):
				m = min(L)
				if(m == value):
					Options_Ascending[s] = Options_Ascending[s] + 1
					break
				else:
					L[L.index(m)] = 100000

	return Options_Ascending


def Caluculte_FactorReduction_mobile(K1,K2,K3,K4,d):
	Options_Ascending = [0,0,0,0]

	for k in range(0,4):
		if (k==0):	
			M1 = K1
			M2 = K2
			M3 = K3
			M4 = K4
		elif(k==1):
			M1 = K2
			M2 = K1
			M3 = K3
			M4 = K4
		elif(k==2):
			M1 = K3
			M2 = K1
			M3 = K2
			M4 = K4
		elif(k==3):
			M1 = K4
			M2 = K1
			M3 = K3
			M4 = K2
		for i in range(0,len(M1)):
			sum1 = 0
			sum2 = 0
			sum3 = 0
			sum4 = 0
			for j in range(0,len(M1)):
				if(i!=j):
					p = len(nx.shortest_path(G,M1[i],M1[j]))
					if(p<=Max_Hop):
						sum1 = sum1 + p*1000 + d*(d**(p-1) - 1)/(d-1)
			for j in range(0,len(M2)):
				p = len(nx.shortest_path(G,M1[i],M2[j]))
				if(p<=Max_Hop):
					sum2 = sum2 + p*1000 + d*(d**(p-1) - 1)/(d-1)
			for j in range(0,len(M3)):
				p = len(nx.shortest_path(G,M1[i],M3[j]))
				if(p<=Max_Hop):
					sum3 = sum3 + p*1000 + d*(d**(p-1) - 1)/(d-1)
			for j in range(0,len(M4)):
				p = len(nx.shortest_path(G,M1[i],M4[j]))
				if(p<=Max_Hop):
					sum4 = sum4 + p*1000 + d*(d**(p-1) - 1)/(d-1)
			L = [sum1/(len(M1)-1) , sum2/len(M2) , sum3/len(M3) , sum4/len(M4)]
			value = sum1/(len(M1)-1)
			for s in range(0,4):
				m = min(L)
				if(m == value):
					Options_Ascending[s] = Options_Ascending[s] + 1
					break
				else:
					L[L.index(m)] = 100000

	return Options_Ascending




def Caluculte_FactorReduction_cars(K1,K2,K3,d):
	Options_Ascending = [0,0,0]

	for k in range(0,3):
		if (k==0):	
			M1 = K1
			M2 = K2
			M3 = K3
		elif(k==1):
			M1 = K2
			M2 = K1
			M3 = K3
		elif(k==2):
			M1 = K3
			M2 = K1
			M3 = K2
		for i in range(0,len(M1)):
			sum1 = 0
			sum2 = 0
			sum3 = 0
			sum4 = 0
			for j in range(0,len(M1)):
				if(i!=j):
					p = len(nx.shortest_path(G,M1[i],M1[j]))
					if(p<=Max_Hop):
						sum1 = sum1 + p*1000 + d*(d**(p-1) - 1)/(d-1)
			for j in range(0,len(M2)):
				p = len(nx.shortest_path(G,M1[i],M2[j]))
				if(p<=Max_Hop):
					sum2 = sum2 + p*1000 + d*(d**(p-1) - 1)/(d-1)
			for j in range(0,len(M3)):
				p = len(nx.shortest_path(G,M1[i],M3[j]))
				if(p<=Max_Hop):
					sum3 = sum3 + p*1000 + d*(d**(p-1) - 1)/(d-1)
			L = [sum1/(len(M1)-1) , sum2/len(M2) , sum3/len(M3)]
			value = sum1/(len(M1)-1)
			for s in range(0,3):
				m = min(L)
				if(m == value):
					Options_Ascending[s] = Options_Ascending[s] + 1
					break
				else:
					L[L.index(m)] = 100000

	return Options_Ascending




def Likeliness_mobile(M1,M2,M3,M4,G):
	Likecount_for_mobile = [0,0,0,0]
	for k in range(0,4):
		if(k == 0):
			M1 = M1
		elif (k==1):
			M1 = M2
		elif (k ==2):
			M1 = M3
		elif (k==3):
			M1 = M4
		else:
			break
		for i in range(0,len(M1)):
			L = [-1,0,0,0,0]
			for j in G.neighbors(M1[i]):
				if(G.node[j]['mobile'] == 1):
					L[1] = L[1]+1
				elif (G.node[j]['mobile'] == 2):
					L[2] = L[2]+1
				elif (G.node[j]['mobile'] == 3):
					L[3] = L[3]+1
				elif (G.node[j]['mobile'] == 4):
					L[4] = L[4]+1
			for s in range(0,4):
				m = max(L)
				if(L.index(m) == G.node[M1[i]]['mobile']):
					Likecount_for_mobile[s] = Likecount_for_mobile[s]+1
					break;
				else:
					L[L.index(m)] = -2

	return Likecount_for_mobile
			

def Likeliness_shoes(M1,M2,M3,M4,G):
	Likecount_for_shoes  = [0,0,0,0]
	for k in range(0,4):
		if(k == 0):
			M1 = M1
		elif (k==1):
			M1 = M2
		elif (k ==2):
			M1 = M3
		elif (k==3):
			M1 = M4
		else:
			break
		for i in range(0,len(M1)):
			L = [-1,0,0,0,0]
			for j in G.neighbors(M1[i]):
				if(G.node[j]['shoes'] == 1):
					L[1] = L[1]+1
				elif (G.node[j]['shoes'] == 2):
					L[2] = L[2]+1
				elif (G.node[j]['shoes'] == 3):
					L[3] = L[3]+1
				elif (G.node[j]['shoes'] == 4):
					L[4] = L[4]+1
			for s in range(0,4):
				m = max(L)
				if(L.index(m) == G.node[M1[i]]['shoes']):
					Likecount_for_shoes[s] = Likecount_for_shoes[s]+1
					break;
				else:
					L[L.index(m)] = -2
	return Likecount_for_shoes


def Likeliness_cars(M1,M2,M3,G):
	Likecount_for_cars = [0,0,0]
	for k in range(0,4):
		if(k == 0):
			M1 = M1
		elif (k==1):
			M1 = M2
		elif (k ==2):
			M1 = M3
		else:
			break
		for i in range(0,len(M1)):
			L = [-1,0,0,0,0]
			for j in G.neighbors(M1[i]):
				if(G.node[j]['car'] == 1):
					L[1] = L[1]+1
				elif (G.node[j]['car'] == 2):
					L[2] = L[2]+1
				elif (G.node[j]['car'] == 3):
					L[3] = L[3]+1
			for s in range(0,3):
				m = max(L)
				if(L.index(m) == G.node[M1[i]]['car']):
					Likecount_for_cars[s] = Likecount_for_cars[s]+1
					break;
				else:
					L[L.index(m)] = -2
	return Likecount_for_cars





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

""" Do I like what majority of my friends Like """
"""
Likecount_for_mobile = 0
Likecount_for_shoes = 0
Likecount_for_cars = 0
Likecount_for_mobile = Likeliness_mobile(M1,M2,M3,M4,G)
Likecount_for_shoes = Likeliness_shoes(S1,S2,S3,S4,G)
Likecount_for_cars = Likeliness_cars(C1,C2,C3,G)
print("Like Count ",Likecount_for_mobile,Likecount_for_shoes,Likecount_for_cars)
Total_responses = len(M1)+len(M2)+len(M3)+len(M4)
"""
#print("Unlike Count ",Total_responses-Likecount_for_mobile,Total_responses-Likecount_for_shoes,Total_responses-Likecount_for_cars)






print ("Simple Averaging")
Options_Ascending1=Caluculte_avg_distance_mobile(M1,M2,M3,M4)
print (Options_Ascending1)
Options_Ascending2=Caluculte_avg_distance_mobile(S1,S2,S3,S4)
print (Options_Ascending2)
Options_Ascending3=Caluculte_avg_distance_cars(C1,C2,C3)
print (Options_Ascending3)
print (Options_Ascending1, Options_Ascending2, Options_Ascending3)




"""
K11 = []
K12 = []
K13 = []
K14 = []
K21 = []
K22 = []
K23 = []
K24 = []
K31 = []
K32 = []
K33 = []

"""

"""
print ("Linear Reduction")

d = 0
for i in range(0,100):
	d = d+0.1
	A = Caluculte_LinearReduction_mobile(M1,M2,M3,M4,d)
	B =	Caluculte_LinearReduction_mobile(S1,S2,S3,S4,d)
	C = Caluculte_LinearReduction_cars(C1,C2,C3,d)
	K11.append(A[0])
	K12.append(A[1])
	K13.append(A[2])
	K14.append(A[3])
	K21.append(B[0])
	K22.append(B[1])
	K23.append(B[2])
	K24.append(B[3])
	K31.append(C[0])
	K32.append(C[1])
	K33.append(C[2])



print (*K11)
print ("\n")
print (*K12)
print ("\n")
print (*K13)
print ("\n")
print (*K14)
print ("\n")
print (*K21)
print ("\n")
print (*K22)
print ("\n")
print (*K23)
print ("\n")
print (*K24)
print ("\n")
print (*K31)
print ("\n")
print (*K32)
print ("\n")
print (*K33)
"""

"""
print ("Factor Reduction")

d = 1
for i in range(0,10):
	d = d+1
	A = Caluculte_FactorReduction_mobile(M1,M2,M3,M4,d)
	B =	Caluculte_FactorReduction_mobile(S1,S2,S3,S4,d)
	C = Caluculte_FactorReduction_cars(C1,C2,C3,d)
	K11.append(A[0])
	K12.append(A[1])
	K13.append(A[2])
	K14.append(A[3])
	K21.append(B[0])
	K22.append(B[1])
	K23.append(B[2])
	K24.append(B[3])
	K31.append(C[0])
	K32.append(C[1])
	K33.append(C[2])



print (*K11)
print ("\n")
print (*K12)
print ("\n")
print (*K13)
print ("\n")
print (*K14)
print ("\n")
print (*K21)
print ("\n")
print (*K22)
print ("\n")
print (*K23)
print ("\n")
print (*K24)
print ("\n")
print (*K31)
print ("\n")
print (*K32)
print ("\n")
print (*K33)
"""
"""
print ("Factor Reduction")
d = 1
for i in range(0,10):
	d = d+1
	print (Caluculte_FactorReduction_mobile(M1,M2,M3,M4,d), Caluculte_FactorReduction_mobile(S1,S2,S3,S4,d),Caluculte_FactorReduction_cars(C1,C2,C3,d))
"""


"""
Caluculte_avg_distance_mobile(S1,S2,S3,S4)
Caluculte_avg_distance_mobile(S2,S1,S3,S4)
Caluculte_avg_distance_mobile(S3,S1,S3,S4)
Caluculte_avg_distance_mobile(S4,S1,S3,S4)
"""

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
"""

"""
nx.draw(G,node_color = color_map,with_labels = True)
plt.show()
"""

