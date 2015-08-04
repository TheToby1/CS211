/*
 * Q2.cpp
 *
 *  Created on: 4 Aug 2015
 *      Author: toby
 */
/*Write a program that takes in an int and prints out the next power of
2 (e.g. 5 -> 8, 4 -> 4, 17 -> 32, 1 -> 1, 61 -> 64). Don’t use any loops.
Don’t use any arithmetic. Only use bit-shifting. */
#include <iostream>
int ans=1;
//decrease x by 1
int decrement(int x){
	if((x&1)==1){
		return x >> 1 << 1;
	}
	else{
		return decrement(x >> 1) << 1|1;
	}
}
//count bits in binary equivalent and make ans equal to that
void count(int x){
	if(x==1){
		ans = ans << 1;
	}
	else{
		ans = ans << 1;
		count(x>>1);
	}
}
//return x if already power of two, otherwise return ans
int pow2(int x){
	if ((x&decrement(x))==0){
		return x;
	}
	else{
		count(x);
		return ans;
	}
}
int main(){
	int x;
	std::cout << "Please enter a number:";
	std::cin >> x;
	std::cout << pow2(x) << std::endl;
	return 0;
}

