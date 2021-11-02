# nasa-project
Wilkommen im Projekt!

Das ist eine kleine Bokeh Applikation, die Informationen über die Sonneneruptionen darstellt.
Ursprünglich war geplant, die Temperatur auf dem Mars zu visualisieren.
Die Api war aber nicht funktionierend und über die NASA Api Webseite 
sind wir auf die Sonneneruptionen gekommen.

Die erste Herausforderung war, die Daten zu verstehen und sich zu überlegen, 
wie man sie pflegen kann und welche Informationen man bekommt.

Ein Beispiel von der Webseite:

[{"flrID":"2016-01-01T23:00:00-FLR-001",
"instruments":[{"displayName":"GOES15: SEM/XRS 1.0-8.0"}],
"beginTime":"2016-01-01T23:00Z",
"peakTime":"2015-01-02T00:10Z",
"endTime":null,
"classType":"M2.3",
"sourceLocation":"S21W73",
"activeRegionNum":12473,
"linkedEvents":[{"activityID":"2016-01-01T23:12:00-CME-001"},{"activityID":"2016-01-02T02:48:00-SEP-001"},{"activityID":"2016-01-02T04:30:00-SEP-001"}],
"link":"https://kauai.ccmc.gsfc.nasa.gov/DONKI/view/FLR/9963/-1"}]

Paar Erklärungen (wikipedia):

ClassType:

"Flares werden logarithmisch nach ihrer Röntgenstrahlungsenergie in die Klassen A, B, C, M und X eingeteilt. Innerhalb einer Klasse wird die Intensität mit einem Wert zwischen 1 und 10 (1 eingeschlossen) festgelegt. Erreicht der Wert 10, so wird er der nächsten Klasse zugeteilt; in der Klasse X sind auch Werte größer als 10 möglich. Die Einteilung ergibt sich aus dem Fluss der Röntgenstrahlung, die von der Sonne ausgeht, und zwar im Bereich von 0,1 bis 0,8 nm (entspricht 1,55 bis 12,4 keV).
"

Von BeginTime bis EndTime versteht man die gesamte Zeit über die, die Sonneneruption erscheint.

Von BeginTime bis PeakTime versteht man die Zeit vom Beginn bis zur intensivsten Phase des Phenomenas. 

"sourceLocation" und "activeRegionNum" zeigen auf die Lokations auf der Sonne.

#####################################################################################
Mit Pandas und Bokeh entstand eine kleine Web App, die versucht die Daten darzustellen. 
Während der Entwicklung wurden genauer Bibliotheken wie: Pandas, Numpy, Seaborn, Bokeh, HoloViews angeschaut.

Zuletzt Pandas und Bokeh war unsere Wahl um die Daten darzustellen. 

Die erste Tabelle ("Welcome") zeigt eine Zusammenfassung von den Daten auf Class Type sortiert.
Die zwei nächste Histogramme stellen dar, wie die Dauerzeit für alle Klassen ausschaut.
Vorletzte Tab fasst kurz Boxplot für During Time um.
Der letzte Tab mit scatter plot beschreibt wie die Zeit für Monate ausschaut mit der Sortierung auf Klassen.

Vielen Dank für das Lesen :)
