package ex4;

public class Zwierze {

	protected String gatunek;
	protected double cena;
	protected String nazwa;
	
	public String getGatunek() {
		return gatunek;
	}
	public void setGatunek(String gatunek) {
		this.gatunek = gatunek;
	}
	public double getCena() {
		return cena;
	}
	public void setCena(double cena) {
		this.cena = cena;
	}
	public String getNazwa() {
		return nazwa;
	}
	public void setNazwa(String nazwa) {
		this.nazwa = nazwa;
	}
	
	public Zwierze(String gatunek, double cena, String nazwa) {
		super();
		this.gatunek = gatunek;
		this.cena = cena;
		this.nazwa = nazwa;
	}

}
