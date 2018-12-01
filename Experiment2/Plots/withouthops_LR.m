K11=[20 20 21 21 21 20 17 14 12 10]


K12=[11 10 8 9 7 6 12 14 15 17]


K13=[5 6 8 9 12 15 12 13 14 13]


K14=[12 12 11 9 8 7 7 7 7 8]


K21=[14 14 14 13 13 13 13 13 12 12]


K22=[14 13 12 12 9 7 6 6 7 8]


K23=[11 12 11 10 16 17 17 17 14 13]


K24=[9 9 11 13 10 11 12 12 15 15]


K31=[16 16 17 18 14 15 15 15 15 15]


K32=[17 17 16 14 16 11 12 11 11 11]


K33=[15 15 15 16 18 22 21 22 22 22]


X = [];
for i=1:10
    X(i) = i
end

subplot(3,1,1)
scatter(X,K11,'filled')
hold on
scatter(X,K12,'filled')
hold on
scatter (X,K13,'filled')
hold on
scatter (X,K14,'filled')
subplot(3,1,2)
scatter(X,K21,'filled')
hold on
scatter(X,K22,'filled')
hold on
scatter (X,K23,'filled')
hold on
scatter (X,K24,'filled')
subplot(3,1,3)
scatter(X,K31,'filled')
hold on
scatter(X,K32,'filled')
hold on
scatter (X,K33,'filled')

