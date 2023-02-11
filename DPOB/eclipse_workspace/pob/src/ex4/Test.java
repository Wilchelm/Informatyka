package ex4;

import java.util.ArrayList;
import java.util.List;

public class Test {

	public static void main(String[] args) {
		Zwierze z = new Zwierze("pies",120.0, "dog niemiecki");
		ZwierzeLadowe z1 = new ZwierzeLadowe("kot perski", 50.0 , "kot", 30.0);
		
		List <Zwierze> zwierzeta = new ArrayList<>();
		zwierzeta.add(z1);
		
		List<PrzedmiotDoKupienia> doKupienia = new ArrayList<>();
		doKupienia.get(0).przedlozGwarancje();
	}

}
