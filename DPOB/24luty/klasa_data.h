#ifndef KLASA_DATA_H
#define KLASA_DATA_H

using namespace std;

class Data
{
    private:
	int day;
	int month;
	int year;

    public:
    Data()
    {
        time_t czas = 0;
        time( & czas );
        printf( "Czas lokalny: %s", ctime( & czas ) );
    }



	void set(int d, int m, int y)
	{
		day = d;
		month = m;
		year = y;
	}
	void print()
	{
		cout<< day << "."<< month<< "."<< year<< endl;
	}

    Data(int d, int m, int y)
    {
        day = d;
        month = m;
        year = y;
    }

};

#endif
