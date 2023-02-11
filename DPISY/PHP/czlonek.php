<?php
session_start();
// dołączenie plików funkCji tej aplikacji
require_once('funkcje_zakladki.php');
// utworzenie krótkich nazw zmiennych
$nazwa_uz = $_POST['nazwa_uz'];
$haslo = $_POST['haslo'];
if ($nazwa_uz && $haslo) {
// właśnie na stąpiła próba logowania
	try {
		loguj($nazwa_uz, $haslo);
		// jeżeli użytkownik znajduje się w bazie danych rejestracja identyfikatora
		$_SESSION['prawid_uzyt'] = $nazwa_uz;
}
catch (Exception $e) {
	// niepomyślne logowanie
	tworz_naglowek_html('Problem:');
	echo 'Zalogowanie niemożliwe. Należy być zalogowanym. aby oglądać tę stronę.';
	tworz_HTML_URL('logowanie.php', 'Logowanie');
	tworz_stopke_html();
	exit;
	}
}

tworz_naglowek_html('Strona główna');
sprawdz_prawid_uzyt();
// odczytanie zakładek użytkownika
if ($tablica_url = pobierz_urle_uzyt($_SESSION['prawid_uzyt'])) {
wyswietl_urle_uzyt($tablica_url);
}
// tworzenie menu opcji
wyswietl_menu_uzyt();
tworz_stopke_html();
?>