allocatemem(120*10^6);
p=random(2^1000);
while(!isprime(p),p=random(2^1000));
q=random(p);
while(!isprime(q),q=random(p));
n=p*q;
y=(p-1)*(q-1);
e=random(y);
while(gcd(e,y)!=1,e=random(y));

d=bezout(e,y)[1];

write("publickey.txt","e=",e);
write("publickey.txt","n=",n);

write("privatekey.txt","d=",d);
write("privatekey.txt","n=",n);
\q;
