<?php
// utworzenie krótkich nazw zmiennych
$email=$_POST['email'];
$nazwa_uz=$_POST['nazwa_uz'];
$haslo=$_POST['haslo'];
$haslo2=$_POST['haslo2'];

// rozpoczecie sesji. która może okazać się konieczna później
//w tym miejscu musi ona zostać przekazana przed nagłówkami
session_start();

//dołączenie plików funkcji tej aplikacji
require_once( 'funkcje_zakladki.php');
try {
	// sprawdzenia wypełnienia formularzy
	if (!wypelniony($_POST)) {
		throw new Exception('Formularz wypełniony nieprawidłowo - proszę wrócić i spróbować ponownie.');
	}
	// nieprawidłowy adres poczty elektronicznej
	if (!prawidlowy_email($email)) {
		throw new Exception('Nieprawidłowy adres poczty elektronicznej - wrócić i spróbować ponownie.');
	}				
	//różne hasła
	if ($haslo != $haslo2) {
		throw new Exception('Niepasujące do siebie hasła - proszę wrócić i spróbować ponownie.');
	}
	
	// sprawdzenie długości nazwy użytkownika
	if (strlen($nazwa_uz)>16) {
		throw new Exception('Nazwa uzytkownika nie może mieć więcej niż 16 znaków - proszę wrócić i spróbować ponownie.');
	}	
	//sprawdzenie długości hasła
	// nazwę użytkownika można skrócić, lecz zbyt
	// hasła skrócić nie można
	if ((strlen($haslo) < 6) || (strlen($haslo > 16))) {
		throw new Exception('Hasło musi mieć co najmniej 6 i maksymalnie 16 znaków - proszę wrócić i spróbować ponownie.');
	}
	// próba zarejestrowania
	rejestruj($nazwa_uz, $email , $haslo);
	// rejestracja zmiennej sesji
	$_SESSION['prawid_uzyt'] = $nazwa_uz;
	// stworzenie łącza do strony członkowskiej
	tworz_naglowek_html( 'Rejestracja pomyślna' );
	echo 'Rejestracja zakończyła się sukcesem. Proszę udać się na stronę członkowską, aby skonfigurować zakładki.';
 	tworz_HTML_URL ('czlonek.php' , 'Strona członkowska') ;
 	
 	//koniec strony
 	tworz_stopke_html();
}
catch (Exception $e) {
tworz_naglowek_html ('Problem; ');
echo $e->getMessage();
tworz_stopke_html();
exit;
}
?>
