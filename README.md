# Topic Modeling der historischen Fachzeitschrift ›Francia‹ 1973–2022

Das Projekt »Topic Modeling der historischen Fachzeitschrift ›Francia‹ 1973–2022« untersucht,
welche Trends und Inhalte sich in der Fachzeitschrift des Deutschen Historischen
Instituts in den 49 Jahrgängen seit ihrer Gründung durch ein Topic Modeling
beobachten lassen.

Dieses Repositorium enthält die für die Studie genutzten Python-Scripte und Jupyter-Notebooks.
Es teilt sich in drei Unterordner: 
## 1. Struktur
### 1.1 metadata
Der Ordner *metadata* enthält ein Jupyter-Notebook, das zur Erstellung der
Visualisierungen der Metadaten der Zeitschrift verwendet wurde. Die Information wurden mittels 
eines Webparsers von der Webseite der [Zeitschrift bei der Universität Heidelberg](https://journals.ub.uni-heidelberg.de/index.php/fr/)
gezogen. Einige Fehler, die wir dabei in den Metadaten gefunden haben, wurden bereits an den Universitätsverlag weitergegeben.
Zudem haben wir die Namen der Autorinnen und Autoren der Francia extrahiert und Analysen über die Geschlechterverteilung
durchgeführt. Diese finden sich ebenfalls im Jupyter-Notebook. Der Datenbestand, auf den es sich bezieht, findet
sich zusammen mit dem dazugehörigen Datenreport auf [Zenodo](https://doi.org/10.5281/zenodo.7962977).

### 1.2 scripts
Im Unterordner *scripts* finden sich die - auch in den Jupyter-Notebooks - verwendeten Scripte.
Sie sind zum Teil spezifisch für die Auswertung von mallet-topic-modelling hier anhand der Zeitschrift »Francia« geschrieben.
Eine etwas allgemeinere Version für die Auswertung von mallet-Ergebnissen bei Topic Modeling findet sich im GitHub repository
[*Analysing_Mallet_Results*](https://github.com/Leano1998/Analysing_Mallet_Results). In der zugehörigen [README.md](https://github.com/Leano1998/Analysing_Mallet_Results/blob/main/README.md) finden sich Hilfestellungen für die Benutzung.

### 1.3 topics
Ähnlich des Ordners für die Metadaten enthält dieser Ordner ein Jupyter-Notebook, in dem sich Visualisierungen der Ergebnisse des Topic Modelings finden.

## 2. Zugehörige Publikationen
### 2.1 Datenreport
Der Datenreport zur Publikation und den hier veröffentlichten Scripten
enthält ergänzende Anmerkungen zu Korpuserstellung, -bereinigung und -auswertung
der »Francia«. Er enthält außerdem Beschreibung und Erläuterungen zu den auf
Zenodo publizierten zusätzlichen Dateien sowie eine Auswahl an kommentierten Zahlen,
Statistiken und Visualisierungen. Er findet sich unter folgender DOI: [https://doi.org/10.5281/zenodo.7962977](https://doi.org/10.5281/zenodo.7962977)

### 2.2 Artikel

*Mareike König, Eike Löhden*, Die »Francia« anders lesen. Was Topic Modeling über Schwerpunkte und Trends der Fachzeitschrift verrät, in: Francia 50 (2023), S. 13–54.
