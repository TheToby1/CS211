/*
 * Q1.cpp
 *
 *  Created on: 5 Aug 2015
 *      Author: toby
 *      You have been employed by Channel 4 to write a computer program that
 *      can help the presenters of Countdown.
 *      Contestants must make English words from nine randomly selected
 *      letters using as many of the letters as possible. Judges look up the words
 *      in the dictionary and then make some even better suggestions. You need
 *      to write a computer program to help them with this.
 *      Write a program which takes in a set of nine letters and then prints out
 *      some good solutions for those letters. You will need to load and use the
 *      file dictionary.txt which contains all of the words in the English
 *      language.
 *      Used Ubuntu's dictinoary as it contains more words, also set it up to take
 *      in more or less than 9 letters.
 */
#include <iostream>
#include <iterator>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

struct checkalpha {
	//check is a char is alpha or apostrophe
	bool operator()(char c) {
		if(std::isalpha(c)||c=='\''){
			return false;
		}
		else{
			return true;
		}
	}
};

struct comparelength {
    bool operator()(const std::string& first, const std::string& second){
        return first.size() < second.size();
    }
} comp;

int main(){
	bool nonalpha = true;
	std::string chars;

	//Takes in a string of only letters and or apostrophes
	while(nonalpha){
		std::cout << "Please input a string of letters." << std::endl;
		std::cin >> chars;
		nonalpha = std::find_if(chars.begin(), chars.end(), checkalpha()) != chars.end();
	}
	//Puts string to lower case
	std::transform(chars.begin(), chars.end(), chars.begin(), ::tolower);

	//counts characters
	std::map<char, int> charset;
	for (char& c : chars) {
		charset[c] += 1;
	}

	//Takes in all words the same size or smaller than chars and makes them lower case
	int pos = 0;
	std::ifstream is("british-english.txt");
	std::istream_iterator<std::string> start(is), end;
	std::vector<std::string> words(start, end);
	std::sort(words.begin(), words.end(), comp);
	for (auto it = words.begin(); it != words.end(); ++it){
		std::transform(it->begin(), it->end(), it->begin(), ::tolower);
		if(it->size()>chars.size()){
			pos = it-words.begin();
			break;
		}
	}
	if(pos>0) words.erase(words.begin()+pos, words.end());

	/*Checker algorithm
	compares the word x with the counter of letters given y
	if any part of y goes negative it breaks*/
	std::vector<std::string> good;
	int maxim = 1;
	for (auto it = words.end()-1; it != words.begin()-1; --it){
		int count = 0;
		std::map<char, int> tmp = charset;
		if (maxim>it->size()) break;
		for (auto ip = it->begin(); ip != it->end(); ++ip){
			if(tmp[*ip]>0){
				count++;
				tmp[*ip]--;
			}
			else{
				count = 0;
				break;
			}
		}
		if (count>=maxim){
			maxim = count;
			//remembers the longest words
			good.push_back(*it);
		}
	}

	std::cout << "The longest word has " << maxim << " letters" << std::endl;
	for (auto it = good.begin(); it != good.end(); ++it){
		std::cout << *it << std::endl;
	}
	return 0;
}
