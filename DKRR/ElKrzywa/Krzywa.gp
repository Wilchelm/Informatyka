{

p = random(2^50);
while ( ! (isprime(p) && 3 == lift(Mod(p,4)) ), p = random(2^50));
 

random();
A = random(p);
B = random(p);
E = ellinit([A,B],p);
lift(Mod(E.disc,p));
 
while ( ! ( lift(Mod(E.disc,p)) != 0 && isprime(p + 1 - ellap(E,p))), A = random(p); B = random(p); E = ellinit([A,B],p););
ordE = p + 1 - ellap(E,p);
 

x = random(p);
f = lift(Mod(x^3 + A*x + B,p));
if(lift(Mod(f,p)^( (p-1)/2  )) == 1 , y = lift(Mod(f,p)^ ((p+1)/4) ); print("OK")); 
P = [Mod(x,p), Mod(y,p)];
 
xa = random(ordE);   \\ ellisoncurve(E,[x,y])
Qa = ellpow(E,P,xa);
}