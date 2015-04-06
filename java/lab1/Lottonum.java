package lab1;

public class Lottonum {
	
	private int num;
	
	public Lottonum(){
		num = 0;
		
	}
	
	public void draw(){
		//num = (int)(Math.ceil(Math.random()*6.0));
		num = (int)((Math.random()*45.0)+1);
	}
	
	public int getValue(){
		return num;
	}

}