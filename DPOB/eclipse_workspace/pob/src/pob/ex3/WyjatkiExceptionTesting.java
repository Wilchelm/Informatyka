package pob.ex3;

import java.util.Scanner;

public class WyjatkiExceptionTesting {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Scanner scanner = new Scanner(System.in);
			
			int i=-1;
			try {
				i = scanner.nextInt();
				System.out.println("koniec wprowadzania");
			} catch (Exception e) {
				System.out.println("zla liczba");
			} finally {
				System.out.println("finally");
			}
			
			System.out.println(i);
			
			scanner.close();
			
			System.out.println("Koniec");
	}

}
