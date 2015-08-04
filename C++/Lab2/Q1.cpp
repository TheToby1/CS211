/*
 * Q1.cpp

 *
 *  Created on: 4 Aug 2015
 *      Author: toby
 *  Grab a stick. Break it in two. Now randomly break another piece in two. Carry out
 *  this process a total of n times.
 *  Write a program that takes n as input and outputs the probability that a triangle can
 *  be formed out of any three of the resulting pieces.
 *  This solution takes a stick breaks it, takes a random stick breaks it etc etc
 *  Gets an answer of roughy 19-20% for 2 breaks
 */
#include <iostream>
#include <random>
#include <set>
#include <algorithm>

int trianglechecker(std::vector<double> & newsticks, int breaks){
	//checks to see if it makes a triangle
	for (auto it = newsticks.cbegin(); it != newsticks.cend()-2; it++){
		if ((*(it)+*(it+1))>(*(it+2)))return 1;
	}
	return 0;
}

int main(){
	const int times = 1000000;
	int count = 0;
	const int breaks = 2;
	double stick1 = 1.0;
	std::random_device rd;
	std::mt19937 mt(rd());

	for(int i =0;i<times;i++){
		std::set<double> breakset;
		//picks n number of random points to break at and puts them in a set.
		while(breakset.size()<breaks){
			std::uniform_real_distribution<double> dist(0,1);
			double stick2 = 0;
			while(stick2==0){
				stick2 = dist(mt);
			}
			breakset.insert(stick2);
		}
		std::vector<double> newsticks;
		double count1 = 0;
		//breaks the stick at set points into an array.
		for (auto it = breakset.cbegin(); it != breakset.cend(); it++){
			newsticks.push_back((*it) - count1);
			count1=(*it);
		}
		newsticks.push_back(1-count1);

		std::sort(newsticks.begin(), newsticks.end());
		count+=trianglechecker(newsticks, breaks);
	}
	std::cout << "With " << breaks << " breaks the chance of making a triangle is " << (count/(double)times)*100 << "%" << std::endl;
}
