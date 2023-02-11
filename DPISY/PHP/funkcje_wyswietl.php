<?php

function tworz_naglowek_html($tytul) {
  // wyświetlenie nagłówka HTML
?>
  <html>
  <head>
    <title><?php echo $tytul;?></title>
    <style>
      body { font-family: Arial, Helvetica, sans-serif; font-size: 13px }
      li, td { font-family: Arial, Helvetica, sans-serif; font-size: 13px }
      hr { color: #3333cc; width=300; text-align=left}
      a { color: #000000 }
    </style>
  </head>
  <body>
  <img src="zakladka.gif" alt="Logo ZakładkaPHP" border="0"
       align="left" valign="bottom" height = "55" width = "57" />
  <h1>&nbsp;ZakładkaPHP</h1>
  <hr />
<?php
  if($tytul) {
    tworz_tytul_html($tytul);
  }
}

function tworz_stopke_html() {
  // wyświetlenie stopki HTML
?>
  </body>
  </html>
<?php
}

function tworz_tytul_html($tytul) {
  // wyświetlenie tytułu
?>
  <h2><?php echo $tytul;?></h2>
<?php
}

function tworz_HTML_URL($url, $nazwa) {
  // wyświetlenie URL-a jako łšcza i nowa linia
?>
  <br /><a href="<?php echo $url;?>"><?php echo $nazwa;?></a><br />
<?php
}

function wyswietl_informacje_witryny() {
  // wyświetlenie informacji marketingowych
?>
  <ul>
  <li>Przechowuj swoje zakładki online!
  <li>Zobacz, czego używajš inni!
  <li>Podziel się swoimi ulubionymi stronami z innymi!
  </ul>
<?php
}

function wyswietl_form_log() {
?>
  <p><a href="formularz_rejestracji.php">Jeszcze nie członek?</a></p>
  <form method="post" action="czlonek.php">
  <table bgcolor="#cccccc">
   <tr>
     <td colspan="2">Logowanie członków:</td>
   <tr>
     <td>Nazwa użytkownika:</td>
     <td><input type="text" name="nazwa_uz"/></td></tr>
   <tr>
     <td>Hasło:</td>
     <td><input type="password" name="haslo"/></td></tr>
   <tr>
     <td colspan="2" align=center>
     <input type="submit" value="Logowanie"/></td></tr>
   <tr>
     <td colspan="2"><a href="zapomnij_formularz.php">Zapomniane hasło?</a></td>
   </tr>
 </table></form>
<?php
}

function wyswietl_form_rej() {
?>
 <form method="post" action="nowa_rejestracja.php">
 <table bgcolor="#cccccc">
   <tr>
     <td>Adres poczty elektronicznej:</td>
     <td><input type="text" name="email" size="30" maxlength="100"></td></tr>
   <tr>
     <td>Preferowana nazwa użytkownika <br />(maksymalnie 16 znaków):</td>
     <td valign="top"><input type="text" name="nazwa_uz"
                     size="16" maxlength="16"/></td></tr>
   <tr>
     <td>Hasło <br />(pomiędzy 6 i 16 znaków):</td>
     <td valign="top"><input type="password" name="haslo"
                     size="16" maxlength="16"/></td></tr>
   <tr>
     <td>Potwierdź hasło:</td>
     <td><input type="password" name="haslo2" size="16" maxlength="16"/></td></tr>
   <tr>
     <td colspan="2" align="center">
     <input type="submit" value="Rejestracja"></td></tr>
 </table></form>
<?php

}

function wyswietl_urle_uzyt($tablica_url) {
  //wyswietlenie URL-i użytkownika

  // ustawienie zmiennej globalnej, aby możliwe było sprawdzanie strony
  global $tabela_zak;
  $tabela_zak = true;
?>
  <br />
  <form name="tabela_zak" action="usun_zak.php" method="post">
  <table width="300" cellpadding="2" cellspacing="0">
  <?php
  $kolor = "#cccccc";
  echo "<tr bgcolor=\"".$kolor."\"><td><strong>Zakładka</strong></td>";
  echo "<td><strong>Usuń?</strong></td></tr>";
  if ((is_array($tablica_url)) && (count($tablica_url) > 0)) {
    foreach ($tablica_url as $url) {
      if ($kolor == "#cccccc") {
        $kolor = "#ffffff";
      } else {
        $kolor = "#cccccc";
      }
      // należy pamiętać o wywołaniu htmlspecialchars() przy wyświetlaniu danych użytkownika
      echo "<tr bgcolor=\"".$kolor."\"><td><a href=\"".$url."\">".htmlspecialchars($url)."</a></td>
            <td><input type=\"checkbox\" name=\"usun_mnie[]\"
             value=\"".$url."\"/></td>
            </tr>";
      }
  } else {
    echo "<tr><td>Brak zapisanych zakładek</td></tr>";
  }
?>
  </table>
  </form>
<?php
}

function wyswietl_menu_uzyt() {
  // wyświetlenie menu opcji na stronie
?>
<hr />
<a href="czlonek.php">Home</a> &nbsp;|&nbsp;
<a href="dodaj_zak_formularz.php">Dodaj zakładkę</a> &nbsp;|&nbsp;
<?php
  // opcja usuń jedynie w wypadku wyświetlenia tabeli zakładek
  global $tabela_zak;
  if($tabela_zak == true) {
    echo "<a href=\"#\" onClick=\"tabela_zak.submit();\">Usuń zakładki</a>&nbsp;|&nbsp;";
  } else {
    echo "<span style=\"color: #cccccc\">Usuń zakładki</span>&nbsp;|&nbsp;";
  }
?>
<a href="zmiana_hasla_formularz.php">Zmiana hasła</a>
<br />
<a href="rekomendacja.php">Zarekomenduj URL-e</a> &nbsp;|&nbsp;
<a href="wylog.php">Wylogowanie</a>
<hr />

<?php
}

function wyswietl_dodaj_zak_form() {
  // wyświetlenie formularza do dodania nowych zakładek
?>
<form name="tabela_zak" action="dodaj_zak.php" method="post">
<table width="250" cellpadding="2" cellspacing="0" bgcolor="#cccccc">
<tr><td>Nowa zakładka:</td>
<td><input type="text" name="nowy_url"  value="http://"
                        size="30" maxlength="255"></td></tr>
<tr><td colspan="2" align="center"><input type="submit" value="Dodaj zakładkę"></td></tr>
</table>
</form>
<?php
}

function wyswietl_haslo_form() {
  // wyświetlenie formularza zmiany hasła
?>
   <br />
   <form action="zmiana_hasla.php" method="post">
   <table width="250" cellpadding="2" cellspacing="0" bgcolor="#cccccc">
   <tr><td>Poprzednie hasło:</td>
       <td><input type="password" name="stare_haslo" size="16" maxlength="16"/></td>
   </tr>
   <tr><td>Nowe hasło:</td>
       <td><input type="password" name="nowe_haslo" size="16" maxlength="16"/></td>
   </tr>
   <tr><td>Powtorzenie nowego hasła:</td>
       <td><input type="password" name="nowe_haslo2" size="16" maxlength="16"/></td>
   </tr>
   <tr><td colspan="2" align="center"><input type="submit" value="Zmiana hasła"/>
   </td></tr>
   </table>
   <br />
<?php
};

function wyswietl_zapomnij_form() {
  // wyświetlenie formularza HTML do ustawiania nowych haseł
?>
   <br />
   <form action="zapomnij_haslo.php" method="post">
   <table width="250" cellpadding="2" cellspacing="0" bgcolor="#cccccc">
   <tr><td>Nazwa użytkownika</td>
       <td><input type="text" name="nazwa_uz" size="16" maxlength="16"/></td>
   </tr>
   <tr><td colspan="2" align="center"><input type="submit" value="Zmiana hasła"/>
   </td></tr>
   </table>
   <br />
<?php
}

function wyswietl_rekomend_urle($tablica_url) {
  // wyniki podobne do wyswietl_urle_uzyt
  // zamiast wyświetlać URL-e użytkownika, wywietla rekomendacje
?>
  <br />
  <table width="300" cellpadding="2" cellspacing="0">
<?php
  $kolor = "#cccccc";
  echo "<tr bgcolor=\"".$kolor."\"><td><strong>Rekomendacje</strong></td></tr>";
  if ((is_array($tablica_url) && count($tablica_url)>0)) {
    foreach ($tablica_url as $url) {
      if ($kolor == "#cccccc") {
        $kolor = "#ffffff";
      } else {
        $kolor = "#cccccc";
      }
      echo "<tr bgcolor=\"".$kolor."\">
            <td><a href=\"".$url."\">".htmlspecialchars($url)."</a></td></tr>";
    }
  } else {
    echo "<tr><td>Aktualnie brak rekomendacji.</td></tr>";
  }
?>
  </table>
<?php
}

?>