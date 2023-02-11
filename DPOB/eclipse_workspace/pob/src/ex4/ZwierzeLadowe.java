package ex4;

public class ZwierzeLadowe extends Zwierze implements PrzedmiotDoKupienia{
	
	private double szybkoscBiegania;


	public double getSzybkoscBiegania() {
		return szybkoscBiegania;
	}

	public ZwierzeLadowe(String gatunek, double cena, String nazwa,
			double szybkoscBiegania) {
		super(gatunek, cena, nazwa);
		this.szybkoscBiegania = szybkoscBiegania;
	}

	@Override
	public double podajCene() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int podajDlugoscGwarancji() {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public void przedlozGwarancje() {
		// TODO Auto-generated method stub
		
	}

	

}
