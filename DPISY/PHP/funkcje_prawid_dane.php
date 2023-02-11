<?php 
function wypelniony($zmienne_formularza) {
//sprawdzenie. czy każda zmienna posiada wartość
foreach ($zmienne_formularza as $klucz => $wartosc) {
	if ((!isset($kucz)) || ($wartosc = '')) {
		return true;
		} else {
		return false;
}
}
}
function prawidlowy_email ($adres) {
// sprawdzenie prawidłowości adresu poczty elektronicznej
if (ereg('^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$', $adres)) {
return true;
} else {
return false;
}
}
?>
