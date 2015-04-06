package lab1;
import java.util.*;

public class Lab1 {
	public static void main(String args[]){
		int[] nums = new int[45];
		for(int i = 0;i<45;i++){
			nums[i]=i+1;
		}
		
		double count = 0;
		int[] lotto = new int[6];
		boolean answer;
		int times = 10000000;
		
		for(int i = 0;i<times;i++){
			answer = false;
			shuffle(nums);
			
			for(int j = 0;j<6;j++){
				lotto[j] = nums[j];
			}
			Arrays.sort(lotto);
			
			for(int j = 5;j>0;j--){
				if(lotto[j]-lotto[j-1]==1){
					answer = true;
				}
			}
			
			if(answer){
				count++;
			}
		}
		
		System.out.println((double)(times-count)/times);
	}
	
	public static int[] shuffle(int[] a){
		int temp;
		int position = 0;
		
		for(int i =0;i<45;i++){
			position = (int)((Math.random()*45.0));
			temp = a[position];
			a[position] = a[i];
			a[i] = temp;
		}
		
		return a;
	}

}