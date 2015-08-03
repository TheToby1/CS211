#ifndef Tree_H
#define Tree_H

#include "node.h"

class tree{
private:
	int frequency;
	
public:
	node * root;
	tree(){
		root = nullptr;
		frequency = 0;
	}
	tree(node * root, int frequency){
		this->root = root;
		this->frequency = frequency;
	}

	int getfreq(){ return frequency; }
	//node getroot(){ return * root; }
};

#endif