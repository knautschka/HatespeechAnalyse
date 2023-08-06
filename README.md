# HatespeechAnalyse
Python-Skripte, um beispielsweise Tweets oder auch andere textliche Inhalte mit Hilfe der Perspective-API auf Hatespeech analysieren zu können.

Um die Skripte auszuführen, werden rudimentäre Python-Kenntnisse vorausgesetzt. Ihr soltet Python 3 und die entsprechenden genutzten Bibliotheken auf eurem System installiert haben.
Je nachdem, was ihr mit den Skripten machen möchtet, müssen diese angepasst werden. Wenn ihr das nicht möchtet und die Skripte möglichst so benutzen möchtet wie sie sind, folgt dieser Anleitung:

1. Besorgt euch Tweet-Daten. Diese könnt ihr euch beispielsweise von archive.org herunterladen. Wenn ihr ganze Datensätze haben wollt, solltet ihr das am besten per Terminal machen, weil die Datensätze über 60 GB groß sind.
2. Ihr solltet jetzt .tar-Dateien für jeden Tag eines Monats haben, in der Struktur twitter-stream-YYYYMMDD. Um die Skripte auszuführen spielt es keine Rolle, ob ihr nur einen Tag oder alle Tage eines Monats heruntergeladen habt.
3. Entpackt die .tar-Dateien der einzelnen Monate nun.
4. Ihr habt jetzt einzelne Ordner der Tage, die sehr viele komprimierte JSON-Dateien enthalten (json.gz). Diese NICHT entpacken, da das Skript diese temporär selbst entpackt.
5. Um nun die Tweets zu analysieren, müsst ihr das Skript "perspectiveapi_ready.py" bearbeiten. Ihr müsst an die entsprechende Stelle euren API-Key von Perspective einfügen. Vorsicht: Teilt euren API-Key mit niemandem.
6. Wenn ihr die Variable "num_files_to_read" anpasst, steuert ihr, wie viele Tweet-Dateien zur Analyse verwendetet werden. Diese werden immer zufällig ausgewählt. Standardmäßig werden zufällig 5 Tweet-Dateien ausgewählt.
7. Kopiert das Skript in den Ordner, in dem ihr die entpackten Ordner abgelegt habt. Wenn ihr das Skript über die Konsole startet, werden die Tweets zur Perspective-API geschickt und die Ergebnisse werden in einer Datei "analyzed_tweets.json" im selben Ordner abgespeichert.
--> Achtung! Bei mehrmaligem Ausführen wird die Datei ohne jede weitere Überprüfung einfach überschrieben. Wenn ihr Ergebnisse speichern wollt, kopiert euch die Datei nach Ausführung woandershin.
--> Dauer der Ausführung: Das Skript geht davon aus, dass ihr die Basis-Version der Perspective-API habt. Bisher ist damit gestattet, dass man 60 Anfragen pro Minute (also in unserem Fall 60 Tweets) abschicken kann. Um auf Nummer Sicher zu gehen, schickt das Skript nur 30 Anfragen pro Minute ab, da Perspective bei Übersteigen des Limits sonst die komplette Anfrage abbricht. Bedenkt also, dass es einige Zeit dauern wird, wenn ihr viele Tweets untersuchen wollt.
8. Schaut euch die generierte "analyzed_tweets.json" an. Es kann passieren, dass das Skript das JSON-Format nicht richtig umsetzt. Ab und zu ist am Ende der JSON-Datei ein Komma ganz am Ende der Datei anstatt einer eckigen Klammer zu ("]"). Dies am besten manuell checken und anpassen, damit die Datei richtig eingelesen werden kann.
9. Kopiert die neue JSON-Datei in einen neuen Ordner zusammen mit der Datei "tweet_hauefigkeitsverteilung.py". An dieser Datei müsst ihr nichts ändern. Ihr erhaltet hier Diagramme und eine Zusammenfassung darüber, welche Hatespeech-Verteilung in eurer Stichprobe vorliegt.
10. Wenn ihr nur eine Stichprobe untersuchen wolltet, dann seid ihr hier fertig. Wenn ihr eure Stichprobe mit einer zweiten vergleichen wollt, zum Beispiel mit eurer aus einem anderen Monat, führt die Schritte 1-9 noch mal mit dem anderen Monat genauso durch. Vorsicht: Achtet darauf, dass ihr eure generierten Dateien dabei nicht überschreibt. Und macht dann ab Schritt 11 weiter.
11. Nehmt jeweils die generierten "zusammenfassung.txt"-Dateien, die durch das "tweet_hauefigkeitsverteilung.py"-Skript generiert wurden. Benennt diese um. Im Skript "statistische_signfikanz.py" wird davon ausgegangen, dass Stichproben aus dem Jahr 2021 und 2022 untersucht wurden, daher wird davon ausgegangen, dass ihr eure Dateien "zusammenfassung_2021.txt" und zusammenfassung_2022.txt" nennt. Wenn ihr andere Monate bzw. Jahre untersucht, achtet darauf, dass ihr die entsprechenden Stellen im Skript umbenennt. Macht dies nur, wenn ihr wisst, was ihr macht. Dazu müssen Stellen im gesamten Skript umgeschrieben werden und es darf nichts vergessen werden, sonst erhaltet ihr Ergebnisse, die nicht akkurat sind.
12. Wenn ihr dies alles gemacht habt, kopiert ihr die beiden Text-Dateien und das Python-Skript "statistische_signfikanz.py" in einen neuen Ordner. Führt dann das Python-Skript aus und ihr erhaltet Diagramme, die das Hatespeech-Vorkommen beider Stichproben vergleichen sowie einen p-Werte, mit denen ihr die statistische Signifikanz festlegen könnt.

Fertig!
