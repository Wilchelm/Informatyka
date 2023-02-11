<?php
session_start();
require_once('funkcje_zakladki.php');
// utworzenie krótkiej nazwy zmiennej
$nowy_url = $_POST['nowy_url'];
tworz_naglowek_html('Dodawanie zakładek');
try {
	sprawdz_prawid_uzyt();
	if (!wypelniony($_POST)) {
	throw new Exception ('Formularz wypełniowny niewłaściwie. Proszę spróbować ponownie');
}
// sprawdzenie formatu URL-a
if (strstr($nowy_url, 'http://') === false) {
       $nowy_url = 'http://'.$nowy_url;
  }
// sprawdzenie prawidłowości URL-a
if (!(@fopen($nowy_url, 'r'))) {
		throw new Exception('URL nieprawidłowy.');
}
//próba dodania zakładki
dodaj_zak($nowy_url);
echo 'Zakładka dodana.';
// pobranie zakładek zapisanych przez użytkownika
if ($tablica_urli = pobierz_urle_uzyt($_SESSION['prawid_uzyt'])) {
			wyswietl_urle_uzyt($tablica_urli);
}
}
catch (Exception $e) {
		echo $e->getMessage();
}
wyswietl_menu_uzyt();
tworz_stopke_html();
?>
