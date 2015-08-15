/*
 * Q1.cpp
 *
 *  Created on: 15 Aug 2015
 *      Author: toby
 *      Write a program that takes encoded.txt as input and outputs the
 *      European language that it is in.Come up with some metric for quantifying
 *      how good the fit is. Encoded is in UTF-8 which I cannot get
 *      working in C++ as <codecvt> is not found.
 */

#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

//compares the two vectors by there largest numbers and prints difference
void compa(std::vector<double> & a,std::vector<double> & z){
	double total = 0;
	if(a.size()>z.size()){
		for(int i = 0; i < z.size();i++){
			total+=abs(a[i]-z[i]);
		}
	}
	else{
		for(int i = 0; i < a.size();i++){
			total+=abs(a[i]-z[i]);
		}
	}
	std::cout << total << std::endl;
}

//Takes the language files into a vector
void language(std::vector<double> & z, std::string place, std::vector<double> & a){
	std::ifstream fin;
	fin.open(place.c_str());

	char key;
	double value;

	while (fin >> key >> value) z.push_back(value);
	fin.close();

	std::sort(z.begin(),z.end(), std::greater<double>());
	compa(a,z);
	z.clear();
}

int main(){
	std::ifstream fin;
	fin.open("encoded.txt");
	std::string x((std::istreambuf_iterator<char>(fin)), (std::istreambuf_iterator<char>()));
	fin.close();

	//counts the chars in the encoded file
	int count = 0;
	std::map<char, double> y;
	for (char& c : x) {
		if(c>31){
			y[c] += 1;
			count++;
		}
	}
	//puts counts into vecor of percentages
	std::vector<double> a;
	for(auto it = y.begin(); it!=y.end();it++){
		 a.push_back((it->second/count)*100);
	}
	//sorts with biggest first
	std::sort(a.begin(),a.end(), std::greater<double>());

	std::vector<double> z;

	//takes in all languages
	std::cout << "French: ";
	language(z, "french.txt", a);

	std::cout << "German: ";
	language(z, "german.txt", a);

	std::cout << "Finnish: ";
	language(z, "finnish.txt", a);

	std::cout << "English: ";
	language(z, "english.txt", a);

	std::cout << "Danish: ";
	language(z, "danish.txt", a);
}
