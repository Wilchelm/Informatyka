package ex4;

public class Akcesoria implements PrzedmiotDoKupienia {
	
	private String nazwa;
	
	private double cena;
	
	private int dlugoscGwarancji;

	public String getNazwa() {
		return nazwa;
	}

	public void setNazwa(String nazwa) {
		this.nazwa = nazwa;
	}

	public double getCena() {
		return cena;
	}

	public void setCena(double cena) {
		this.cena = cena;
	}

	public int getDlugoscGwarancji() {
		return dlugoscGwarancji;
	}

	public void setDlugoscGwarancji(int dlugoscGwarancji) {
		this.dlugoscGwarancji = dlugoscGwarancji;
	}

	public Akcesoria(String nazwa, double cena, int dlugoscGwarancji) {
		super();
		this.nazwa = nazwa;
		this.cena = cena;
		this.dlugoscGwarancji = dlugoscGwarancji;
	}

	@Override
	public double podajCene() {
		
		return cena;
	}

	@Override
	public int podajDlugoscGwarancji() {
		
		return dlugoscGwarancji;
	}

	@Override
	public void przedlozGwarancje() {
		dlugoscGwarancji++;
		
	}
	
	

}
