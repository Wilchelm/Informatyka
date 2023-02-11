allocatemem(120*10^6);
{
exponet = 1000;

q = nextprime(random(2^exponet));
p = 2*q+1;
while(!isprime(p), q = nextprime(random(2^exponet)); p = 2*q+1);

x = random(p-1);

y= lift(Mod(q,p)^x);


write("PublicKey.out","p=",p);
write("PublicKey.out","q=",q);
write("PublicKey.out","y=",y);
print("y=",y);
print("p=",p);
print("q=",q);


write("PrivateKey.out","x=",x);
write("PrivateKey.out","p=",p);
write("PrivateKey.out","q=",q);
print("x=",x);
print("p=",p);
print("q=",q);
}
\q;
