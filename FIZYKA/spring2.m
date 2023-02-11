% RUCH HARMONICZNY -- ciało na sprężynie

% schemat alteratywny 
% dla przypadku niejawnego równania

clear  % czyścimy co się da
 
graphics_toolkit("fltk")   % opcjonalna opcja graficzna, czasem niezbędna, czasem przeszkadzająca
%setenv GNUTERM aqua    % jak wyżej  


% Parametry:

tmax = 10;     % maksymalny czas

global h = 0.005;      % krok czasowy

nt = tmax/h        % końcowy czas

MOD = 25;        % co ile króków ma być wyświetlany wykres

k = 10;     % stała sprężystości
m = 1;     % masa
global K = k/m;    

global x0 = 1;   % odchylenie początkowe w metrach
global v0 = 0;     % prędkość początkowa

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

global x = x0;     % położenie chwilowe
global v = v0;     % prędkość chwilowa

eng = 1;   % znormalizowana energia chwilowa

t = 0;   % wektor wartości argumentów czasu
X = x;   % wektor położeń
V = v;   % wektor prędkości
E = eng;   % wektor energii

ampl_x = max(abs([x0 v0/sqrt(K)]));     % amplituda dla x
ampl_v = max(abs([v0 x0*sqrt(K)]));    % amplituda dla v


T = 0:h:tmax;      % zbiór argumentów czasu, dowolny krok

% analityczne rozwiązanie dla położenia i predkości
% jako funkcja względem czasu chwilowego,
% argumnetem jest czas: 

function wynik = rozw_x(t)
global K x0 v0;

  wynik = x0 * cos(sqrt(K) * t);

%  wynik = x0 * cos(sqrt(K) * t) + (v0 * sin(sqrt(K) * t))/sqrt(K);
end 

function wynik = rozw_v(t)
global K x0 v0;

  wynik = - sqrt(K) * x0 * sin(sqrt(K) * t);  

%  wynik = v0 * cos(sqrt(K) * t) - sqrt(K) * x0 * sin(sqrt(K) * t);  
end 


energia = ones(1,size(T,2));  % energia = 1 dla każdego t 


% znormalizowane błędy
error_x = abs(x - rozw_x(0))/ampl_x;
error_v = abs(v - rozw_v(0))/ampl_v;

% zakres osi dla wykresów
AXIS = [0 tmax -2*ampl_x 2*ampl_x];
AXIS2 = [0 tmax -2*ampl_v 2*ampl_v];
AXIS3 = [0 tmax];
AXIS4 = [0 tmax];


  figure(1)
  plot(T,rozw_x(T),'m',t,X,'b.')
  axis(AXIS)
  grid on
  title('POLOZENIE')
  xlabel('T')
  ylabel('X')
  legend('rozw. dokladne', 'rozw. numeryczne')

  figure(2)
  plot(T,rozw_v(T),'m',t,V,'r.')
  axis(AXIS2)
  grid on
  title('PREDKOSC')
  xlabel('T')
  ylabel('Y')
  legend('rozw. dokladne', 'rozw. numeryczne')
  
  figure(3)
  plot(T,energia,'m',t,E,'b.')
  axis(AXIS3)
  grid on
  title('ENERGIA')
  xlabel('T')
  ylabel('E')
  legend('energia = 1', 'energia numeryczna')

  figure(4)
  plot(t,error_x,'b.',t,error_v,'r.')
  axis(AXIS4)
  grid on
  title('BLEDY')
  xlabel('T')
  ylabel('errors')
  legend('blad dla x', 'blad dla v')


%drawnow
pause()



% FUNKCJA dla zmodyfikowanego schematu: 

function wynik = Fun(X)
global K x v h

u = [x v];

p =  (X + u)/2;
      
KK = [p(2) -K*p(1)];

wynik = X - u - h * KK;

endfunction



% Pętla

for n = 1:nt  % pętla czasowa (krokowa)


% znajdujemy za pomocą odpowiedniego schematu nowe chwilowe położenie i nową chwilową prędkość


% schemat
solution = fsolve(@Fun,[x v]);

x = solution(1);
v = solution(2);

eng = (m*v^2 + k*x^2)/(m*v0^2 + k*x0^2);    % energia


% uzupełniamy o nowe wartości odpowiednie wektory:

t = [t n*h];
X = [X x];
V = [V v];
E = [E eng];

error_x = [error_x abs(x - rozw_x(n*h))/ampl_x];
error_v = [error_v abs(v - rozw_v(n*h))/ampl_v];


  if mod(n,MOD) == 0    % rysujemy pod warunkiem, że n jest wielokrotnością MOD

  figure(1)
  plot(T,rozw_x(T),'m',t,X,'b.')
  axis(AXIS)
  grid on
  title('POLOZENIE')
  xlabel('T')
  ylabel('X')
  legend('rozw. dokladne', 'rozw. numeryczne')

  figure(2)
  plot(T,rozw_v(T),'m',t,V,'r.')
  axis(AXIS2)
  grid on
  title('PREDKOSC')
  xlabel('T')
  ylabel('Y')
  legend('rozw. dokladne', 'rozw. numeryczne')
  
  figure(3)
  plot(T,energia,'m',t,E,'b.')
  axis(AXIS3)
  grid on
  title('ENERGIA')
  xlabel('T')
  ylabel('E')
  legend('energia = 1', 'energia numeryczna')

  figure(4)
  plot(t,error_x,'b.',t,error_v,'r.')
  axis(AXIS4)
  grid on
  title('BLEDY')
  xlabel('T')
  ylabel('errors')
  legend('blad dla x', 'blad dla v')

%  drawnow

  end

end

disp(" "), disp("krok czasowy : "), disp(h);
disp(" "), disp("czas maksymalny : "), disp(tmax);
disp(" "), disp("ilosc krokow : "), disp(nt);
disp(" "), disp("Max error_x : "), disp(max(error_x));
disp(" "), disp("Max error_v : "), disp(max(error_v)), disp(" ");
pause()
