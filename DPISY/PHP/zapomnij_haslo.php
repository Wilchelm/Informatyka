<?php
require_once("funkcje_zakladki.php");
tworz_naglowek_html("Ustawianie hasła");
// utworzenie krótkiej nazwy zmiennej
$nazwa_uz = $_POST['nazwa_uz'];

try {
	$haslo=ustaw_haslo($nazwa_uz);
	powiadom_haslo($nazwa_uz, $haslo);
	echo 'Nowe hasło zostało przesłane na adres poczty elektronicznej.<br />';
}
catch (Exception $e) {
	echo 'Hasło nie mogło zostać ustawione. Proszę spróbować pożniej.';
}
tworz_HTML_URL('logowanie.php', 'Logowanie');
tworz_stopke_html();
?>
