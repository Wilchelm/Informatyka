<?php

require_once('funkcje_bazy.php');

function rejestruj($nazwa_uz, $email, $haslo) {
// zarejestrowanie nowej osoby w bazie danych
// zwraca true lub komunikat o błędzie

 // połączenie z bazą danych
  $lacz = lacz_bd();

  // sprawdzenie, czy nazwa użytkownika nie powtarza się
  $wynik = $lacz->query("select * from uzytkownik where nazwa_uz='".$nazwa_uz."'");
  if (!$wynik) {
     throw new Exception('Wykonanie zapytania nie powiodło się.');
  }

  if ($lacz->num_rows>0) {
     throw new Exception('Nazwa użytkownika zajęta proszę wrócić i wybrać inną.');
  }

  // jeżeli wszystko w porządku, umieszczenie w bazie danych
  $wynik = $lacz->query("insert into uzytkownik values
                       ('".$nazwa_uz."', sha1('".$haslo."'), '".$email."')");
  if (!$wynik) {
    throw new Exception('Rejestracja w bazie danych niemożliwa  proszę spróbować później.');
  }

  return true;
}

function loguj($nazwa_uz, $haslo) {
// sprawdzenie nazwy użytkownika i hasła w bazie danych
// jeżeli się zgadza, zwraca true
// jeżeli nie, wyrzuca wyjątek

  // połączenie z bazšą danych
  $lacz = lacz_bd();

  // sprawdzenie unikatowoci nazwy użytkownika
  $wynik = $lacz->query("select * from uzytkownik
                         where nazwa_uz='".$nazwa_uz."'
                         and haslo = sha1('".$haslo."')");
  if (!$wynik) {
     throw new Exception('Logowanie nie powiodło się.');
  }

  if ($wynik->num_rows>0) {
     return true;
  } else {
     throw new Exception('Logowanie nie powiodło się.');
  }
}

function sprawdz_prawid_uzyt() {
// sprawdzenie czy użytkownik jest zalogowany i powiadomienie go jeżeli nie
  if (isset($_SESSION['prawid_uzyt'])) {
      echo "Zalogowano jako ".$_SESSION['prawid_uzyt'].".<br />";
  } else {
     // nie jest zalogowany
     tworz_naglowek_html('Problem:');
     echo 'Brak zalogowania.<br />';
     tworz_HTML_URL('logowanie.php', 'Logowanie');
     tworz_stopke_html();
     exit;
  }
}

function zmien_haslo($nazwa_uz, $stare_haslo, $nowe_haslo) {
// zmiana hasła użytkownika ze stare_haslo na nowe_haslo
// zwraca true lub false

  // jeżeli stare hasło jest prawidłowe zmiana nowe_haslo i zwrócenie true
  // w przeciwnym wypadku wyrzucenie wyjštku
  loguj($nazwa_uz, $stare_haslo);
  $lacz = lacz_bd();
  $wynik = $lacz->query("update uzytkownik
                         set haslo = sha1('".$nowe_haslo."')
                         where nazwa_uz = '".$nazwa_uz."'");
  if (!$wynik) {
    throw new Exception('Zmiana hasła nie powiodła się.');
  } else {
    return true;  // zmiana udana
  }
}

function pobierz_losowe_slowo($dlugosc_min, $dlugosc_max) {
//pobranie losowego słowa ze słownika o okrelonej długoci zwrócenie go

  // generowanie losowego słowa
  $slowo = '';
  // tę cieżkę należy dostosować do ustawień własnego systemu
  $slownik = '/usr/dict/words';  // słownik ispell
  $wp = @fopen($slownik, 'r');
  if(!$wp) {
    return false;
  }
  $wielkosc = filesize($slownik);

  // przejócie do losowej pozycji w słowniku
  $losowa_pozycja = rand(0, $wielkosc);
  fseek($wp, $losowa_pozycja);

  // pobranie ze słownika następnego pełnego słowa o właściwej długości
  while ((strlen($slowo) < $dlugosc_min) || (strlen($slowo)>$dlugosc_max) || strstr($slowo, "'")) {
     if (feof($wp)) {
        fseek($wp, 0);        // jeżeli koniec pliku, przeskocz na początek
     }
     $slowo = fgets($wp, 80);  // przeskoczenie pierwszego słowa bo może być niepełne
     $slowo = fgets($wp, 80);  // potencjalne hasło
  }
  $slowo = trim($slowo); // obcięcie poczštkowego \n z funkcji fgets
  return $slowo;
}

function ustaw_haslo($nazwa_uz) {
// ustawienie hasła użytkownika na losową wartość
// zwraca nowe hasło lub false w przypadku niepowodzenia

  // pobranie losowego słowa ze słownika o długości pomiędzy 6 i 13 znaków
  $nowe_haslo = pobierz_losowe_slowo(6, 13);

  if($nowe_haslo == false) {
    throw new Exception('Wygenerowanie nowego hasła nie powiodło się.');
  }

  // dodanie liczby pomiędzy 0 i 999 w celu stworzenia lepszego hasła
  $losowa_liczba = rand(0, 999);
  $nowe_haslo .= $losowa_liczba;

  // ustawienie nowego hasła w bazie danych lub zwrócenie false
  $lacz = lacz_bd();
      return false;
  $wynik = $lacz->query("update uzytkownik
                         set haslo = sha1('".$nowe_haslo."')
                         where nazwa_uz = '".$nazwa_uz."'");
  if (!$wynik) {
    throw new Exception('Zmiana hasła nie powiodła się.');  // hasło nie zmienione
  } else {
    return $nowe_haslo;  // hasło zmienione pomylnie
  }
}

function powiadom_haslo($nazwa_uz, $haslo) {
// powiadomienie użytkownika o zmianie hasła

    $lacz = lacz_bd();
    $wynik = $lacz->query("select email from uzytkownik
                           where nazwa_uz='".$nazwa_uz."'");
    if (!$wynik) {
      throw new Exception('Nie znaleziono adresu e-mail');
    } else if ($wynik->num_rows == 0) {
      throw new Exception('Nie znaleziono adresu e-mail'); // nazwy użytkownika nie ma w bazie danych
    } else {
      $wiersz = $wynik->fetch_object();
      $email = $wiersz->email;
      $od = "From: obsluga@zakladkaphp \r\n";
      $wiad = "Hasło systemu ZakładkaPHP zostało zmienione na $haslo \r\n"
              ."Proszę zmienić je przy następnym logowaniu. \r\n";


      if (mail($email, 'Informacja o logowaniu ZakładkaPHP', $wiad, $od)) {
        return true;
      } else {
        throw new Exception('Wysłanie e-maila nie powiodło się');
      }
    }
}

?>
