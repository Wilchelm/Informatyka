
RetroC2 temporal classification challenge
=========================================

Guess the publication year of a Polish text.

This is the second (larger and improved) edition of the challenge, see
[http://gonito.net/challenge/retroc]() for the first edition.

Example
-------

For instance, you are expected to guess the publication year of this 500-word
text:

> Gazet, a tam o osobie zamformuie się. Uwiadomienie. Stosownie do
> dodatku gazety W. Xiestwa Poznańskiego Nru 74. Ig15. niźey podpisany
> odwoluiąc się, w którey wszelkie pełnomocnictwa komukolwiek priez
> niego dane, od daty teyźe gazety za nieważne mieć chce, dziś więc
> potwierdza to, kassuiac i umarzaiąc pełnomocnictw» Ur. Podgurskiemu
> przez siebie uczyni o n e, w P o z n a n i u dnia 3. Mala 1816 r.
> Psirohońshi. Odmienienie mieszkania. Donoszę Szanowney Publiczności,
> iż mieszkanie moie z Dominikjńskiey ulicy przeniosłem na Szeroką
> ulicę do JP. Fi asa pod Nr 114 na pierwszym piętrze, i handel zboża
> nadal prowadzić będę. Poznań dnia 6. Maia 1816. Meyer Marcuse. III
> 111---»-- Do przedania. Kamienica w rynku podNrcra 62, o trzech
> piętrach, wraz z zabudowaniami, w bardzo dobrym znayduiąca się
> stanie, do szynku i przyimowania gości urządzona, iest zwolney ręki
> do przedania. Dokładnieyszą wiadomość powziąść można u właściciela.
> Do przedania. Dom za Świętym Marcinem pod N rem 42. z browarnią,
> staynią, studnią i wielkićm podwórzem, niemniey kilkanaście szachtów
> kamieni, iest na dniu 24m Czerwca r. b. z wolney .ręki do
> sprzedania. Każdy ochotę mający kupna, o kondycyach sprzedaży
> dowiedzieć się mole tu w Voznaniu w rynku pod N rem 57. u S tanisław
> a PoweIskiego. Do przedania. Na mocy w Prześwietnym Sądzie Pokoiti
> Powiatu tuteyszego pomiędzy Szl. Henrykiem Eichbaum, właścicielem
> młyna papierni w MuchodzU 5 A 7 II nie, Powiatu Międzyrzeckiego, a
> Szl. Wilhelmem Ferdynandem Naukę, Kredy torem pryncypalnym z młyna
> wodnego w Muchodzinie, na dniu 29m miesiąca Marca roku bieżąesgo
> itawartey i w ley n.ierze do podpisanego uczynionego wniosku,
> zesunie młyn papiernia, wraz do tego należącemi gruntami, w wsi
> Muchodzinie w Powiecie Międzyrzeckim leżąca, według urzedowey na
> dniu I I Kwietnia roku bieżącego zdziałaney taxy, na summe. 2246
> Tal. 12 dgr, oszacowana, w drodze lieytacyi public-zney więcey
> daiącemu za gotowa Ziraz zjpłatę, i wypełnieniem kondycyi kupna,
> sprzedana; do którey to sprzedaży termin pierwszy do publikacyi
> kondycyi kupna 1 przedsunowczego przysądzenia, na żądanie
> Iineressentow, na dzieli 12. miesiąca Czerwca roku bieżącego
> w.kascelląryi Urzędnika podpisanego o godzinie iotey przed południem
> wyznaczonym zostaie.- Wzywa się więc ninśeyszem Publiczność kupna
> tego ochotę maiącą, oraz wszelcy Kredyiorowie e x q u o c u n q u e
> jur e d o młyna tego papierni twierdzić prawa sobie mogący, aby w
> terminie wzwyż wyrażonym osobiście lub przez prawnie umocowanych
> Pełnomocników stawilisię; pierwsi swe licyta, drudzy zaś swe realne
> pretensye do protokółu podali, a nay więcey licytuiącemu nie«
> ruchomości powyż wymienioney zprzyległościami przygotowawcze
> przysądzenie nastąpi. Kredytprowie zaś "Z swerni pretensyami do
> nieruchomości tey za prekludowanych, a to sub prejudicio perpetui
> silentii uważani zostaną. Zbiór obiaśnień i kondycyi kupna przeyrzeć
> każdy interessuiący może u podpisanego. Międzyrzecz dnia 20.
> Kwietnia i816\\ Ur ząd P isars t wa Aktowego Powiatu
> Międzyrzeckiego. M. GądkowskL Do przedania. Podaie się do publiczney
> wiadomości, iż podpisany Komornik Sądowy Powiatu Krobskiego,
> zatradowane inwentarze, to iest: konie, woły, krowy, owce i t. d. i
> porządki gospodarskie, Wmu Kamieńskiemu, Possessocpwi dóbr
> Sobiałkowskich, za kaucyą na zabezpieczenie inwentarzy gruntowych,
> do massy konkursowey JOO.XiazatSujftoivsftjcji należących, w wsi
> Sobiałkowie pod Rawiczem

(Yes, there might be a lot of OCR noise there!)

The perfect answer for this text is 1816.37021856342 (year with a
fraction representing a specific day, May, 15th, 1816 for this
example). You could as well return non-integer numbers, for instance
if you are sure that the text was published in 1977, but you have no
idea on which day, the optimal decision is to return 1977.5.

The metric is root mean squared error.

Directory structure
-------------------

* `README.md` — this file
* `config.txt` — GEval configuration file
* `train/` — directory with training data
* `train/train.tsv.xz` — train set (compressed with xz, not gzip!)
* `train/meta.tsv.xz` — metadata (do **not** use in training)
* `dev-0/` — directory with dev (test) data from the same sources as the train set
* `dev-0/in.tsv` — input text for the dev set
* `dev-0/expected.tsv` — expected data for the dev set (publication years)
* `dev-0/meta.tsv.xz` — metadata (do **not** use while testing)
* `dev-1/` — directory with dev (test) data from different source than the train set
* `dev-1/in.tsv` — input text for the dev set
* `dev-1/expected.tsv` — expected data for the dev set (publication years)
* `dev-1/meta.tsv.xz` — metadata (do **not** use while testing)
* `test-A` — directory with test data
* `test-A/in.tsv` — input text for the test set
* `test-A/expected.tsv` — expected data for the test set (hidden)
* `test-A/meta.tsv.xz` — hidden metadata

Structure of data sets
----------------------

Dev and tests test sets are balanced for years (or at least it was
attempted to balance them for years — for some years there was not enough material).

The `dev-0` dataset was created using the same sources as the train set, but
`dev-1` and `test-A` were generated using sources different from
`dev-0` (and different to each other), so `dev-0` is likely to be
easier than `dev-1`.

Metadata files are given for reference, do not use them for training.

Format of the train set
-----------------------

The format of the train set is different from test sets. There is more
information there and you are free to exploit it.

TAB-separated columns:

* beginning of the period in which a text is known to be published, given as a year
  with a possible fraction (note that various time granularities are given in this
  data set — daily, monthly, yearly, etc.),
* end of the period in which a text is known to be published,
* title normalised,
* symbol of the source (usually a Polish digital library).
* ~500-word-long text snippet.

Format of the test sets
-----------------------

The input file is just a list of ~500-word-long text snippets, each
given in a separate line.

The `expected.tsv` file is a list of publication years (with fractions).

Format of the output files
--------------------------

For each input line, publication year should be given (it is the same
as `expected.tsv` files). The name of the output files is `out.tsv`.
