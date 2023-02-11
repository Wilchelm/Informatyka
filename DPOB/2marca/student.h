#ifndef STUDENT_H
#define STUDENT_H

class Student : public Osoba
{
	private:
		int stypendium;
	public:
		int podajStypendium()
		{
			return stypendium;
		}
		
		void ustalStypendium(double st)
		{
			stypendium = st;
		}
		float wydatekOsobowy();
};

#endif