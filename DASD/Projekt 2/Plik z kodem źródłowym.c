#include <stdio.h>
#include <math.h>

void main()
{


int z;
scanf ("%d", &z);

for (int i=0; i<z; i++) {
  float a,b,c;
  scanf ("%f %f %f", &a, &b, &c);
  
  if (a==0 && b==0 && c==0) {printf("R\n");}
  else {
    if (a==0 && b==0) {printf("0\n");}
    else {
      if (a==0) { 
        float liniowa=(0-c)/b;
        if (floor(liniowa)==liniowa) {
          int traj;
          traj=liniowa;
          printf("1 %d\n", traj);
        }
        else {printf("1 %f\n", liniowa);}
      }
      else {
        float delta,pierw,x,x1,x2;
  
        delta=b*b-(4*a*c);
        pierw=sqrt(delta);
        
        if (delta<0) {
          printf("0\n");
        }
  
        if (delta==0) {
          x=-b/(2*a);
          if (floor(x)==x) {
            int traj;
            traj=floor(x);
            printf("1 %d\n", traj);
          }
          else {printf("1 %f\n", x);}
        }
  
        if (delta>0) {
          x1=((-b)-pierw)/(2*a);
          x2=((-b)+pierw)/(2*a);
          int traj1=0,traj2=0;
          if (floor(x1)==x1 && floor(x2)==x2) {
            traj1=floor(x1);
            traj2=floor(x2);
            
            if (traj1<=traj2) {printf("2 %d %d\n", traj1, traj2);}
            if (traj1>traj2) {printf("2 %d %d\n", traj2, traj1);}
          }
          
          if (floor(x1)==x1 && floor(x2)!=x2) {
            traj1=floor(x1);
            
            if (traj1<=x2) {printf("2 %d %f\n", traj1, x2);}
            if (traj1>x2) {printf("2 %f %d\n", x2, traj1);}
          }
          
          if (floor(x1)!=x1 && floor(x2)==x2) {
            traj2=floor(x2);
            
            if (x1<=traj2) {printf("2 %f %d\n", x1, traj2);}
            if (x1>traj2) {printf("2 %d %f\n", traj2, x1);}
          }
          if (floor(x1)!=x1 && floor(x2)!=x2) {
            if (x1<=x2) {printf("2 %f %f\n", x1, x2);}
            if (x1>x2) {printf("2 %f %f\n", x2, x1);}
          }
        }
      }
    }
  }
}
}
