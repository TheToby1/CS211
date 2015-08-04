/*
 * Q1.cpp
 *
 *  Created on: 2 Aug 2015
 *      Author: toby
 */

#include <iostream>
#include <algorithm>
/*Write a Java program that uses a Monte Carlo algorithm to calculate the
probability that next week's lottery draw won't have any consecutive
pairs of numbers (eg 8 and 9 or 22 and 23). Six numbers are drawn
from 1 to 45.*/
int main(){
	//generates array of numbers 1->45
	int ilotto[45]={0};
	for(int i = 1; i<45;i++){
		ilotto[i-1]=i;
		//std::cout << ilotto[i-1] << std::endl;
	}

	//number of times for monte carlo
	double times = 1000000;
	int temp[6] = {};
	double count = 0;
	//loop shuffles ilotto array and takes top 6, checking for pairs
	for(int i =0;i<times;i++){
		std::random_shuffle ( std::begin(ilotto), std::end(ilotto) );
		for(int j = 0;j<6;j++){
			temp[j] = ilotto[j];
			//std::cout << temp[j] << std::endl;
		}
		std::sort(std::begin(temp), std::end(temp));
		for(int j = 0;j<5;j++){
			if(temp[j] == temp[j+1]-1){
				count++;
				j=6;
			}
		}
	}
	//calcs probability
	std::cout << (times-count)/times << std::endl;

	return 0;
}
