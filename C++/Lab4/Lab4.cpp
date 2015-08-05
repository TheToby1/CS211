/*
 * Lab4.cpp
 *
 *  Created on: 30 July 2015
 *      Author: toby
 * The task is to complete the Huffman algorithm so that it takes in a sentence and
 * outputs Huffman codes.
 * Bonus marks for creating a compressor/de-compressor.
 * Python version working. C++ version cannot get serializer working.
 */
#include "node.h"
#include "tree.h"
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <queue>
#include <bitset>
#include <sstream>
using namespace std;

//All huffman codes stored in global variable j
map<char, string> j;

//Comparator for sorting the priority queue
class comparefreq{
public:
	bool operator() (tree &t1, tree &t2) const{
		return t1.getfreq() > t2.getfreq();
	}
};

//File input
string fileinput(const string place){
	ifstream fin;
	fin.open(place.c_str());
	//takes the file in as a string
	string x((std::istreambuf_iterator<char>(fin)), (std::istreambuf_iterator<char>()));
	fin.close();
	return x;
}

//Steps through tree to find huffman codes
int stepper(node current, string answer){
	if (current.getdata() != '\0'){
		cout << current.getdata() << ": " << answer << endl;
		j[current.getdata()] = answer;
		return 0;
	}
	//cout << "left" << endl;
	stepper(*current.leftchild, answer+"1");

	//cout << "up" << endl;
	//cout << "right" << endl;
	stepper(*current.rightchild, answer+"0");
	//cout << "up" << endl;
	return 0;
}

int main(){
	string x = fileinput("test.txt");
	//printf("%s", x.c_str());

	//Counts all characters
	map<char, int> y;
	for (char& c : x) {
		y[c] += 1;
	}

	priority_queue<tree, vector<tree>, comparefreq> prq;
	//Prints a 2d map and makes a priority queue of trees
	for (auto it = y.cbegin(); it != y.cend(); ++it){
		std::cout << it->first << " " << it->second << "\n";
		node * temp = new node(it->first, nullptr, nullptr);
		prq.push(tree(temp, it->second));
	}
	
	//joins the lowest frequency trees together until only one tree is left
	while(prq.size()>1){
		tree temp1 = prq.top();
		node * temp3 = temp1.root;
		prq.pop();
		tree temp2 = prq.top();
		node * temp4 = temp2.root;
		prq.pop();
		prq.push(tree(new node('\0', temp3, temp4), temp1.getfreq()+temp2.getfreq()));
	}

	//takes tree from priority queue and emptys queue
	tree huff = prq.top();
	prq = priority_queue <tree, vector<tree>, comparefreq>();
	node current = *huff.root;
	string answer = "";
	//gives stepper the root
	stepper(current, answer);
	//prints all charcters with their huffman code
	for (auto it = j.cbegin(); it != j.cend(); ++it){
		std::cout << it->first << " " << it->second << "\n";
	}
	//steps through original string adding its huffman to the answer
	for (char& c : x) {
		answer += j[c];
	}
	//printf("%s", answer.c_str());
	//adds trailing 0's for when de-compressing
	while (answer.length() % 8 != 0){
		answer += "0";
	}

	// write the binary value to file
	stringstream sstream(answer);
	string output;
	while (sstream.good())
	{
		bitset<8> bits;
		sstream >> bits;
		char c = char(bits.to_ulong());
		output += c;
	}
	ofstream myfile;
	myfile.open("comp.bin", ios::binary);
	myfile << output;
	return 0;
}
