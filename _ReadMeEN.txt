# ############### #
# TabelleComperre #
# ############### #

The principle of operation:
The script compares 2 tables of symbols imported to an Excel, and then creates the result file "Result.txt",
in which it prints out all the rows that differ from the rows in the master table.
If there are no differences in the resulting file, the text "No changes" will appear.
The script takes into account a change in the position of the signals, it will show only those that have changed or have been added (to the table we are comparing).
It will not show the signals that are missing. This can be detected by swapping the tables in the sheets.


Manual:
We export from 2 projects of symbol tables (I used SDF format,
but it doesn't matter) and then we import them into the prepared Excel.

In "To_Compare" tab we import table from current backup.
Select A1 cell, go to "Data" tab, select "From text file/CSV",
select our table, drop down the "Load" context menu and select "Load to",
Import in the form of a table and select "Existing sheet" and cell A1.
Similarly, to the Template sheet, we import a master table - e.g. from the current backup where we made the changes.


Close the excel and run the executable file "TC.exe". - nothing spectacular will happen, no chases or explosions, no running dinosaurs
on the desktop. After a certain time (depending on the size of the tables), the result file "Result.txt" will appear (in the same folder).
Searching 2 tables of 18000 rows each took about 1 minute and 40 seconds.

NOTES:
For proper operation it is required that:
	- "TC.exe" and "TabelleComperre.xlsx" are in the same folder.
	- Tables in sheets start in the same cells.

I placed the source code in the Source folder.

Translated with www.DeepL.com/Translator (free version)