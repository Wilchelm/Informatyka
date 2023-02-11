#ifndef PRACOWNIK_H
#define PRACOWNIK_H

class Pracownik : public Osoba
{
	private:
		int pensja;
	public:
		float wydatekOsobowy();
		void ustalPensje (double p)
		{
			pensja = p;
		}
		int podajPensje ()
		{
			return pensja;
		}
		int podajPremie()
		{
			return 0.2*pensja;
		}
};

#endif