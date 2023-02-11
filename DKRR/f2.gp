allocatemem(120*10^6);
{
p=random(10^300);
while(!isprime(p),p=random(10^300));
print("p=",p);
}
\q;
