package lab1;
import java.util.*;

public class q3 {
	public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		System.out.println("Please enter a number");
		int num = scan.nextInt();
		int count = 0;
		boolean answer = false;
		
		if((num-- & num++) == 0) answer = true;
		
		if(answer){
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
