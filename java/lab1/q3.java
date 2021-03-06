/*Write a Java program that takes in an int and prints out the next power of
2 (e.g. 5 -> 8, 4 -> 4, 17 -> 32, 1-> 1, 61 -> 64). Don’t use any loops.
Don’t use any arithmetic. Only use bit-shifting. */
import java.util.*;

public class q3 {
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.println("Please enter a number");
		int num = scan.nextInt();
		int count = 0;
		
		//For example if num=4, if 3&4==0 print 4
		if((num-- & num++) == 0){
			System.out.println(num);
		}
		else{
			count = powersoftwo(num);
			System.out.println(1<<count);
		}
		
		scan.close();
	}
	
	public static int powersoftwo(int num){
		int count = 1;
		if(num == 0) return 0;
		count += powersoftwo(num>>1);
		return count;
	}

}
