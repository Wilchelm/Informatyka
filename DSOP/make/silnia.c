unsigned long int silnia(int n){
	if(n==1) return 1;
	return n*silnia(n-1);
}
