<?php
session_start();
// dołączenie plików fun kcj i tej aplikacji
require_once('funkcje_zakladki.php');
$stary_uzyt = $_SESSION['prawid_uzyt'];
// przechowanie do sprawdzenia. czy logowanie
unset( $_SESSION['prawid_uzyt']);
$wynik_niszcz = session_destroy();


// początek wyświetlania html
tworz_naglowek_html('Wylogowanie' );
if (!empty($stary_uzyt)) {
	if ($wynik_niszcz) {
		// jeżeli użytkownik zalogowany i nie wylogowany
		echo 'Wylogowano.<br /> ' ;
		tworz_HTML_URL( 'logowanie.php', ' Logowanie');
	} else {
		// użytkownik za logowany i wylogowanie niemożliwe
		echo 'Wylogowanie niemożliwe, < br />';
	}
} else {
	// jeżeli brak zalogowania, lecz w jakiś sposób uzyskany dostęp do strony
	echo 'Użytkownik niezalogowany, tak więc brak wylogowania,<br />';
	tworz_HTML_URL('logowanie,php', 'Logowanie' );
}

tworz_stopke_html();

?>