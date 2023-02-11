allocatemem(120*10^6);
{
read("Public");
read("Private");
read("Cipher");

s = Mod(c1,p)^x;
message = c2*Mod(lift(s),p)^(-1);

print("Alice says: message = ", lift(message));
}
\q;
