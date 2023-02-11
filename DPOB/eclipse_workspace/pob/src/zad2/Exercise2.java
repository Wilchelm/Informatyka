package zad2;


public class Exercise2 {

	public static void main(String[] args) { 
	
		long numer = 123456789;

		String s = String.valueOf(numer);
		StringBuilder sb = new StringBuilder(s);
		String result = sb.reverse().toString(); 
		
		System.out.println(result);
	
		
	}
}
