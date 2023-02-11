package pob.ex3;

public class Throw {

	public static void main(String[] args){
		// TODO Auto-generated method stub
		System.out.println("Start");
		SomeClass sc = new SomeClass();
		try {
			System.out.println(sc.sayHello());
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("Koniec");

	}

}
