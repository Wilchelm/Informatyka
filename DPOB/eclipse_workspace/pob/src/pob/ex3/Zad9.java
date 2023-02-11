package pob.ex3;

import java.util.Scanner;

public class Zad9 {

	public static void main(String[] args) {
		System.out.println("Podaj liczbe");
		Scanner scanner=new Scanner(System.in);
		String liczba = scanner.nextLine();
		int foo = Integer.parseInt(liczba);
		
		
		try {
			int i = foo*foo;
			System.out.println(i);
		} catch (Exception e) {
			System.out.println("to nie liczba");
		}
		
		System.out.println("Koniec");
		
		scanner.close();
		
	}

}