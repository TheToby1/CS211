#ifndef NODE_H
#define NODE_H

class node{
private:
	char data;
	
public:
	node * leftchild;
	node * rightchild;
	node(){
		data = NULL;
		leftchild = nullptr;
		rightchild = nullptr;
	}
	node(char data, node * leftchild, node * rightchild){
		this->data = data;
		this->leftchild = leftchild;
		this->rightchild = rightchild;
	}

	char getdata(){ return data; }
};

#endif