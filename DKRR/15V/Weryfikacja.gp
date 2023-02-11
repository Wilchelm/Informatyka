read("PublicKey.out");
read("Podpis.out");
if(   !((0<r || r<p)  & (0<s  || s<(p-1)  )) , print("NIE"));

t= lift( Mod(  lift(Mod(y,p)^r) *  lift(Mod(r,p)^s)   ,p ));
if( t = lift(Mod(q,p)^M)    ,print("TAK"));
\q;
