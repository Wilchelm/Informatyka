package test;

import java.util.Scanner;

public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Podaj imie:");

		Scanner scanner = new Scanner(System.in);
		String imie = scanner.nextLine();
				System.out.println("To twoje imie:"+imie+"?");	
				
		
		scanner.close();
	}
}
