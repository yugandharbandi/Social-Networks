#include<bits/stdc++.h>
#include<iostream>
using namespace std;
unsigned seed1 = std::chrono::system_clock::now().time_since_epoch().count();
default_random_engine gen(seed1); //gen(time(NULL));
uniform_int_distribution<int> dist(0,100000);
uniform_int_distribution<int> dist1(0,1000);


int main(){ 


	srand(time(0)); 
	for(int i=1;i<=10;i++){
		for(int j=1;j<=10;j++){
			for(int k=1;k<=50;k++){
			   string file;
			   file = "Category_"+to_string(i)+"_Brand_"+to_string(j)+"_Product_"+to_string(k);
			   ofstream myfile(file);
			   if(myfile.is_open()){
			   		int number = dist1(gen);
	  				
			   		for(int s=0;s<number;s++){
			   			myfile<<dist(gen)<<endl;
			   		}
			   }
			}
		}
	}
	
	
	/*
	ofstream myfile ("Brands.txt");
  
  if (myfile.is_open())
  {
  	for(int i=1;i<=5;i++){
  	myfile<<"Brand"<<i<<endl;
  	}
    myfile.close();
  }
  */
  

  return 0;
}