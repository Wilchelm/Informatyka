allocatemem(120*10^6);
{
p=read("Public");

message = random(p);
k = nextprime(random(p-1));

c1 = Mod(g,p)^k;
s = Mod(y,p)^k;
c2 = Mod(message*s,p);
print("Bob says: message = ", message);

C = [lift(c1),lift(c2)];
write("Cipher", C);
}
\q;
