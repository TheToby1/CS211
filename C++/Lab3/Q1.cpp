/*
 * Q1.cpp
 *
 *  Created on: 5 Aug 2015
 *      Author: toby
 *      Write a program which takes in a line from the user (using Scanner)
 *      and then outputs
 *      i) The sentence in ASCII
 *      ii) Each letter in the sentence and its frequency
 */
#include <iostream>
#include <string>
#include <map>
#include <bitset>

int main(){
	std::string x;
	std::cout << "Please enter your sentence: ";
	std::cin >> x;

	//Counts all characters
	int count = 0;
	std::map<char, int> y;
	for (char& c : x) {
		count++;
		y[c] += 1;
		//prints ascii
		std::bitset<7> b(c);
		std::cout << b.to_string() << " ";
		if(count%8==0){//new line every 8 characters for presentations sake
			std::cout << std::endl;
		}
	}
	std::cout << std::endl;

	//iterates over the map
	for (auto it = y.cbegin(); it != y.cend(); ++it){
		std::cout << it->first << " " << it->second << "\n";
	}
	std::cout << "ASCII would use " << count*7 << " bits." << std::endl;
}


