<?php
session_start();
require_once('funkcje_zakladki.php');
tworz_naglowek_html('Zmiana hasła');
// utworzenie krótkich nazw zmiennych
$stare_haslo = $_POST['stare_haslo'];
$nowe_haslo = $_POST['nowe_haslo'];
$nowe_haslo2 = $_POST['nowe_haslo2'];
try {
	sprawdz_prawid_uzyt();
	if (!wypelniony($_POST)) {
		throw new Exception('Formularz nie został wypełniony całkowicie. Proszę spróbować ponownie');
	}
	if ($nowe_haslo != $nowe_haslo2) {
		throw new Exception('Wprowadzone hasła nie są identyczne. Hasło zostało zmienione.');
	}

	if ((strlen($nowe_haslo) > 16) || (strlen($nowe_haslo) < 6)) {
										throw new Exception('Nowe hasło musi mieć długość co najmniej 6 i maksymalnie 16 znaków. Proszę spróbować ponownie.');
}
// próba uaktualnienia
zmien_haslo($_SESSION[ 'prawid_uzyt'], $stare_haslo, $nowe_haslo);
echo 'Hasło zmienione.';
}
catch (Exception $e) {
echo $e->getMessage();
}
wyswietl_menu_uzyt();
tworz_naglowek_html();
?>
