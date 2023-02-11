<?php
require_once('funkcje_bazy.php');

function pobierz_urle_uzyt($nazwa_uz) {
  // pobranie z bazy danych wszystkich URL-i danego użytkownika
  $lacz = lacz_bd();
  $wynik = $lacz->query("select URL_zak
                         from zakladka
                         where nazwa_uz = '".$nazwa_uz."'");
  if (!$wynik) {
    return false;
  }

  // tworzenie tablicy URL-i
  $tablica_url = array();
  for ($licznik = 0; $rzad = $wynik->fetch_row(); ++$licznik) {
    $tablica_url[$licznik] = $rzad[0];
  }
  return $tablica_url;
}

function dodaj_zak($nowy_url) {
  // dodawanie nowych zakładek do bazy danych

  echo "Próba dodania ".htmlspecialchars($nowy_url)."<br />";
  $prawid_uzyt = $_SESSION['prawid_uzyt'];

  $lacz = lacz_bd();

  // sprawdzenie, czy zakładka już istnieje
  $wynik = $lacz->query("select * from zakladka
                         where nazwa_uz='$prawid_uzyt'
                         and URL_zak='".$nowy_url."'");
  if ($wynik && ($wynik->num_rows>0)) {
    throw new Exception('Zakładka już istnieje.');
  }

  // umieszczenie nowej zakladki
  if (!$lacz->query("insert into zakladka values
                     ('".$prawid_uzyt."', '".$nowy_url."')")) {
    throw new Exception('Wstawienie nowej zakładki nie powiodło się');
  }

  return true;
}

function usun_zak($uzytkownik, $url) {
  // usunięcie jednego URL-a z bazy danych
  $lacz = lacz_bd();
   // usunięcie zakładki
  if (!$lacz->query("delete from zakladka
                     where nazwa_uz='".$uzytkownik."' and URL_zak='".$url."'")) {
    throw new Exception('Usunięcie zakładki nie powiodło się.');
  }
  return true;
}

function rekomenduj_urle($prawid_uzyt, $popularnosc = 1) {
  // tworzenie półinteligentnych rekomendacji
  // Jeżeli posiadajš URL-e wspólne z innymi użytkownikami, mogš im się
  // spodobać inne URL-e, które lubiš inni
  $lacz = lacz_bd();

  // znalezienie innych pasujšcych użytkowników
  // z podobnymi URL-ami
  // jako prosty sposób wyłšczania prywatnych stron użytkowników oraz
  // zwiększania szansy rekomendacji wartociowego URL
  // podany jest minimalny poziom popularnoci
  // jeżeli $popularnosc=1, wtedy więcej niż jedna osoba musi posiadać
  // dany URL przed jego rekomendacjš

  $zapytanie = "select URL_zak
                from zakladka
                where nazwa_uz in
                                 (select distinct(z2.nazwa_uz)
                                  from zakladka z1, zakladka z2
                                  where z1.nazwa_uz='".$prawid_uzyt."'
                                  and z1.nazwa_uz!=z2.nazwa_uz)
                and URL_zak not in
                                 (select URL_zak
                                  from zakladka
                                  where nazwa_uz='".$prawid_uzyt."')
                group by URL_zak
                having count(URL_zak)>".$popularnosc;

  if (!($wynik = $lacz->query($zapytanie))) {
     throw new Exception('Nie znaleziono żadnych rekomendowanych zakładek.');
  }
  if ($wynik->num_rows==0) {
     throw new Exception('Nie znaleziono żadnych rekomendowanych zakładek.');
  }

  $urle = array();
  // stworzenie tablicy odpowiednich URL-i
  for ($licznik=0; $rzad = $wynik->fetch_object(); $licznik++) {
     $urle[$licznik] = $rzad->URL_zak;
  }

  return $urle;
}
?>
