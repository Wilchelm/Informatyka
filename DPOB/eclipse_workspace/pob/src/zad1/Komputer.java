package zad1;

public class Komputer {

	private double CPU;

	private int RAM;

	private String producent;

	public double getCPU() {
		return CPU;
	}

	public void setCPU(double cPU) {
		CPU = cPU;
	}

	public int getRAM() {
		return RAM;
	}

	public void setRAM(int rAM) {
		RAM = rAM;
	}

	public String getProducent() {
		return producent;
	}

	public void setProducent(String producent) {
		this.producent = producent;
	}

	public Komputer(double cPU, int rAM, String producent) {
		super();
		CPU = cPU;
		RAM = rAM;
		this.producent = producent;
	}

}
