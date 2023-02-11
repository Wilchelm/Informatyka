function main()
{
  var EPS = 0.0000000001; // dok³adnoœæ porównania z zerem
  var a,b,c,delta,x1,x2,t;

  a = parseFloat(document.frmbincode.wsp_a.value);
  b = parseFloat(document.frmbincode.wsp_b.value);
  c = parseFloat(document.frmbincode.wsp_c.value);
  if(isNaN(a) || isNaN(b) || isNaN(c))
    t = "<font color=red><b>Nieprawid³owe wspó³czynniki!</b></font>";
  else if(Math.abs(a) < EPS)
    t = "<font color=red><b>To nie jest rownanie kwadratowe</b></font>";
  else
  {
    delta = b * b - 4 * a * c;
    if(Math.abs(delta) < EPS) delta = 0;
    if(delta < 0)
      t = "<font color=red><b>Brak pierwiastków równania</b></font>";
    else
    {
      x1 = (-b + Math.sqrt(delta)) / 2 / a;
      x2 = (-b - Math.sqrt(delta)) / 2 / a;
      t = "x<sub>1</sub> = " + x1 + "<BR>x<sub>2</sub> = " + x2;
    }
  }
  document.getElementById("out").innerHTML = t;
}
