allocatemem(120*10^6);
{
exponet = 1000;

q = nextprime(random(2^exponet));
p = 2*q+1;
while(!isprime(p), q = nextprime(random(2^exponet)); p = 2*q+1);
a = random(2^exponet);
while(((Mod(a,p)^2) == 1 || (Mod(a,p)^q) == 1), 
a = random(2^exponet));

x = nextprime(random(q-1));
g = Mod(a,p);
y = Mod(g,p)^x;

Ka = [p, lift(g), lift(y)];
ka = [x, p];
write("Public", Ka);
write("Private", ka);
}
\q;
