package zad2;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Delfiny {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		List<String> lista = new ArrayList<>();
		
		Scanner scanner = new Scanner(System.in);
	    int ilosc = scanner.nextInt();
	    
	    for(int i=0; i<ilosc; i++) {
	    	
	    	String imie = scanner.nextLine();
	    	lista.add(imie); 	
	    }		
	
	    for(int i=0; i<ilosc; i++) {
	    	
	    	System.out.println(lista.get(i));
	    }	
	    	
		scanner.close();
	}
}
