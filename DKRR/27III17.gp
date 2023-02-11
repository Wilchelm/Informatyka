allocatemem(120*10^6);
p=random(2^1000);
x=random(p-1);
y=random(p-1);
a=random(p-1);
b=lift(Mod(y^2-(x^3+a*x),p));

while(Mod(4*x^3+27*b^2,p)==0){
x=random(p-1);
y=random(p-1);
a=random(p-1);
b=lift(Mod(y^2-(x^3+a*x),p));
}

P=[x,y];
A=a;
B=b;
print("y=", y^2=x^3+A*x+B);
\q;
