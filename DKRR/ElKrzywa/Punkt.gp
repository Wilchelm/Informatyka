chi = 20;
M = 5363;
j = 1;
xm = lift(Mod(M*chi + j,p));
fx = x^3 + A*x + B;
ym = lift(Mod(fx,p)^ ((p+1)/4));
while(lift(Mod(fx,p)^( (p-1)/2  )) != 1, xm = M*chi + j; fx = x^3 + A*x + B; ym = lift(Mod(fx,p)^ ((p+1)/4) ); j = j + 1);
Pm = [Mod(xm,p), Mod(ym,p)];