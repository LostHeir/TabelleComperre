# ############### #
# TabelleComperre #
# ############### #

Zasada działania:
Skrypt porównuje 2 tabele symboli zaimportowane do excela, po czym tworzy plik wynikowy "Result.txt",
w którym wypisuje wszystkie wiersze, które różnią się od wierszy tabeli wzorcowej.
W przypadku braku różnic w pilku wynikowym pojawi się napis "No changes".
Skrypt uwzględnia zmianę położenia sygnałów, pokaże tylko te sygnały, które się zmieniły albo zostały dodane (do tabeli, którą porównujemy).
Nie pokaże natomiast sygnałów, których brakuje. Można to wykryć zamieniając miejscami tabele w arkuszach.


Instrukcja:
Eksportujemy z 2 interesujących nas projektów tebele symboli (ja używałem formatu SDF,
ale to nie ma znaczenia), po czym importujemy je do przygotowanego Excela.

W zakładce "To_Compare" importujemy tabelę z aktualnego backup'u na linii.
Wybieramy komórkę A1, przechodzimy do zakładki "Dane", wybieramy opcję"Z pliku tekstowego/CSV",
wybieramy naszą tabelę, rozwijamy menu kontekstowe "Załaduj" i wybieramy "Załaduj do",
importujemy w formię tabeli i wybieramy opcję "Istenijący arkusz" oraz komórkę A1.

Analogicznie, do arkusza Tempate importujemy tabelę wzorcową - np. z aktualnego backup'u, na którym wprowadziliśmy zmiany.

Zamykamy excela i uruchamiamy plik wykonawczy "TC.exe" - nie stanie się nic spektakularnego, nie będzie fajerwerków, ani biegających
na pulpicie dinozaurów. Po określonym czasie (zależnym od wielkości tabel), pojawi się plik wynikowy "Result.txt" (w tym samym folderze).
Przeszukanie 2 tabel po 18000 wierszy, zajmowało około 1 min i 40 s.

UWAGI:
Do poprawnego działania wymagane jest aby:
	- "TC.exe" i "TabelleComperre.xlsx" były w tym samym katalogu.
	- Tabele w arkuszach zaczynały się w tych samych komórkach.

W folderze Source umieściłem kod źródłowy.




