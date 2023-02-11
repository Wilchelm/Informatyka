<?php
session_start();
require_once('funkcje_zakladki.php');
//create short variable names
$usun_mnie = $_POST['usun_mnie'];
$prawid_uzyt = $_SESSION['prawid_uzyt'];

tworz_naglowek_html('Usuwanie zakładek');
sprawdz_prawid_uzyt();

if (!wypelniony ($_POST)) {
		echo '<p>Nie wybrane zostały żadne zakładki do usunięcia.<br/> Proszę spróbować ponownie.</p>';
wyswietl_menu_uzyt();
tworz_stopke_html();
exit;
}else {
	if (count($usun_mnie) > 0) {
		foreach($usun_mnie as $url) {
			if (usun_zak($prawid_uzyt, $url)) {
					echo 'Usunięto '.htmlspecialchars($url).'.<br />';
			}else {
					echo 'Nie udało się usunięcie'.htmlspecialchars($url).'.<br /> ' ;
			}
		}
} else {
	echo 'Nie wybrano żadnych zakładek do usunięcia';
}
}
//odczytanie zakładek użytkownika
if ($tablica_url = pobierz_urle_uzyt($prawid_uzyt)) {
		wyswietl_urle_uzyt($tablica_url);
}
wyswietl_menu_uzyt();
tworz_stopke_html();
?>
