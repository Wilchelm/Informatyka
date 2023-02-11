
#define EPS 0.0000000001
#define STEP 1.0

/* This function adds two numbers. */
double very_smart_add(double a, double b)
{
	a += b;
	return a;
}

double the_middle_of2(double a, double b)
{
	double l = a, r = b;
	double check, m;
	while (1)
	{
		m = very_smart_add(l, r)/2;
		check = very_smart_add(m, m);
		if (check > very_smart_add(a, b) + EPS)
			r = m;
		else if (check < very_smart_add(a, b) - EPS)
			l = m;
		else
			return m;
	}
}
double the_middle_of(double a, double b)
{
	double r = 0;
	double s = a + b;
	double z = fmod(s,2);
	
	if(z==0.0) r=s/2;
	else r=(s+1.0)/2;

	return the_middle_of2(r - 1.0, s - (r - 1.0));
}

double square_root(double x)
{
	double l = 0, r = x;
	double check, m;
	while (1)
	{
		m = the_middle_of(l, r);
		check = m * m;
		if (check > x + EPS)
			r = m;
		else if (check < x - EPS)
			l = m;
		else
			return m;
	}
}
