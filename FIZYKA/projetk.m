clear
g=9.81;
v0 = 10; %predkosc poczatkowa
h=90;
kat=90;
rad=kat*pi/180; %kąt
vx=v0*cos(rad);
vy=v0*sin(rad);
tmax=(vy+sqrt((2*g*h)+(vy*vy)))/g;
xmax=vx*tmax;
T=0:tmax/100:tmax;
X=vx*T;
Y=(h+(vy*T))-0.5*g*T.*T;
if xmax>0.001
a=xmax;
else
a=0.001
end
plot(X,Y)
axis([-a a])
