% RUCH HARMONICZNY -- ciało na sprężynie

clear    % czyścimy co się da

%graphics_toolkit("fltk")   % opcjonalna opcja graficzna, czasem niezbędna, czasem przeszkadzająca
%setenv GNUTERM aqua    % jak wyżej


% Parametry:

tmax = 10;    % maksymalny czas

h = 0.005;    % krok czasowy

nt = tmax/h   % końcowy czas

MOD = 1;      % co ile króków ma być wyświetlany wykres

k = 10;       % stała sprężystości
m = 1;        % masa
K = k/m;           

x0 = 1;       % odchylenie początkowe w metrach
v0 = 0;       % prędkość początkowa

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

x = x0;       % położenie chwilowe
v = v0;       % prędkość chwilowa

eng = 1;      % znormalizowana energia chwilowa

t = 0;        % wektor wartości argumentów czasu
X = x;        % wektor położeń
V = v;        % wektor prędkości
E = eng;      % wektor energii

ampl_x = max(abs([x0 v0/sqrt(K)]));    % amplituda dla x
ampl_v = max(abs([v0 x0*sqrt(K)]));    % amplituda dla v


T = 0:h:tmax;      % zbiór argumentów czasu

% analityczne rozwiązanie dla położenia i prędkości,
% jako wektory względem T,
% argumentem jest numer kroku czasowego:

rozw_x = x0 * cos(sqrt(K) * T);              
rozw_v = - sqrt(K) * x0 * sin(sqrt(K) * T);

%rozw_x = x0 * cos(sqrt(K) * T) + (v0 * sin(sqrt(K) * T))/sqrt(K);              
%rozw_v = v0 * cos(sqrt(K) * T) - sqrt(K) * x0 * sin(sqrt(K) * T);              

energia = ones(1,size(T,2));  % energia = 1 dla każdego t 


% znormalizowane błędy
error_x = abs(x - rozw_x(1))/ampl_x;
error_v = abs(v - rozw_v(1))/ampl_v;

% zakres osi dla wykresów
AXIS = [0 tmax -2*ampl_x 2*ampl_x];
AXIS2 = [0 tmax -2*ampl_v 2*ampl_v];
AXIS3 = [0 tmax];
AXIS4 = [0 tmax];

  figure(1)  
  plot(T,rozw_x,'m',t,X,'b.')
  axis(AXIS)
  grid on
  title('POLOZENIE')
  xlabel('T')
  ylabel('X')
  legend('rozw. dokladne', 'rozw. numeryczne')
  
  %figure(2)
  %plot(T,rozw_v,'m',t,V,'r.')
  %axis(AXIS2)
  %grid on
  %title('PREDKOSC')
  %xlabel('T')
  %ylabel('V')
  %legend('rozw. dokladne', 'rozw. numeryczne')
  
  %figure(3)
  %plot(T,energia,'m',t,E,'b.')
  %axis(AXIS3)
  %grid on
  %title('ENERGIA')
  %xlabel('T')
  %ylabel('E')
  %legend('energia = 1', 'energia numeryczna')

  %figure(4)
  %plot(t,error_x,'b.',t,error_v,'r.')
  %axis(AXIS4)
  %grid on
  %title('BLEDY')
  %xlabel('T')
  %ylabel('errors')
  %legend('blad dla x', 'blad dla v')


%drawnow
pause()


for n = 1:nt         % pętla czasowa (krokowa)


% znajdujemy za pomocą odpowiedniego schematu nowe chwilowe położenie i nową chwilową prędkość


% SCHEMAT EULERA:
 x_new = x + h * v;
 v_new = v - h * K * x;


% lekko zmodyfikowany SCHEMAT EULERA:
% x_new = x + h * v;
% v_new = v - h * K * x_new;


% ALTERNATYWNY SCHEMAT
% x_new = (4*h*v + 4*x - h^2*K*x)/(4 + h^2*K);
% v_new = (4*v - h^2*K*v - 4*h*K*x)/(4 + h^2*K);

x = x_new;
v = v_new;


eng = (m*v^2 + k*x^2)/(m*v0^2 + k*x0^2);    % energia


% uzupełniamy o nowe wartości odpowiednie wektory:

t = [t n*h];
X = [X x];
V = [V v];
E = [E eng];

error_x = [error_x abs(x - rozw_x(n+1))/ampl_x];
error_v = [error_v abs(v - rozw_v(n+1))/ampl_v];


  if mod(n,MOD) == 0            % rysujemy pod warunkiem, że n jest wielokrotnością MOD 

  %figure(1)
  %plot(T,rozw_x,'m',t,X,'b.')
  %axis(AXIS)
  %grid on
  %title('POLOZENIE')
  %xlabel('T')
  %ylabel('X')
  %legend('rozw. dokladne', 'rozw. numeryczne')

  %figure(2)
  %plot(T,rozw_v,'m',t,V,'r.')
  %axis(AXIS2)
  %grid on
  %title('PREDKOSC')
  %xlabel('T')
  %ylabel('V')
  %legend('rozw. dokladne', 'rozw. numeryczne')
  
  %figure(3)
  %plot(T,energia,'m',t,E,'b.')
  %axis(AXIS3)
  %grid on
  %title('ENERGIA')
  %xlabel('T')
  %ylabel('E')
  %legend('energia = 1', 'energia numeryczna')

  %figure(4)
  %plot(t,error_x,'b.',t,error_v,'r.')
  %axis(AXIS4)
  %grid on
  %title('BLEDY')
  %xlabel('T')
  %ylabel('errors')
  %legend('blad dla x', 'blad dla v')

%  drawnow

  end

end

disp(" "), disp("krok czasowy : "), disp(h);
disp(" "), disp("czas maksymalny : "), disp(tmax);
disp(" "), disp("ilosc krokow : "), disp(nt);
disp(" "), disp("Max error_x : "), disp(max(error_x));
disp(" "), disp("Max error_v : "), disp(max(error_v)), disp(" ");
pause()


