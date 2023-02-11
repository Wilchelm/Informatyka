allocatemem(120*10^6);
{
p=1;
while(!isprime(p), p=random(2^50));
print("p=",p);
A=random(p);
B=random(p);

E=ellinit([0,0,0,A,B]);
print("delta mod p = ",Mod(E.disc,pl));

x=random(p);
f=Mod(x^3+A*x+B,p);
while(f^((p-1)/2)!=1,x=random(p);f=Mod(x^3+A*x+B,p));

print("is square mod p = ", f^((p-1)/2));
print("f=",f);
y=sqrt(f);
print("y=",y^2);
P=[Mod(x,p),y];
print("P=[x,y]=",P);

a=random(p);
print("a=",a);
Q=ellpow(E,P,a);
print("[a]Q=",Q);

R=elladd(E,P,Q);
print("P+Q=",R);

N=p+1-ellap(E,p);
print("#E=",N);
}
\q;
