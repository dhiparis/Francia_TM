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
Visualisierungen von den Metadaten der Zeitschrift verwendet wurde. Die Information wurden mittels 
eines Webparsers von der Webseite der [Zeitschrift bei der Universität Heidelberg](https://journals.ub.uni-heidelberg.de/index.php/fr/)
gezogen. Einige Fehler, die wir dabei gefunden haben, wurden bereits an die Universität weitergegeben.
Zudem haben wir die Autorinnen und Autoren der Francia extrahiert und Analysen über die Geschlechterverteilung
durchgeführt. Diese finden sich ebenfalls in dem Jupyter-Notebook. Der Datenbestand, auf den es sich bezieht, findet
sich zusammen mit dem dazugehörigen Datenreport auf [Zenodo](https://zenodo.org/).

### 1.2 scripts
In dem Unterordner *scripts* finden sich die - auch in den Jupyter-Notebooks - verwendeten Scripte.
Sie zum Teil spezifisch für die Auswertung von mallet-topic-modelling hier anhand der Francia geschrieben.
Eine etwas allgemeinere Version für die Auswertung von mallet-Ergebnissen bei Topic-Modelling findet sich auch in dem GitHub repository
[*Analysing_Mallet_Results*](https://github.com/Leano1998/Analysing_Mallet_Results). In der zugehörigen [README.md](https://github.com/Leano1998/Analysing_Mallet_Results/blob/main/README.md) finden sich 
auch Hilfestellungen für die Benutzung.

### 1.3 topics
Ähnlich des Ordners für die Metadaten enthält dieser Ordner ein Jupyter-Notebook, in dem sich Visualisierungen für
die Ergebnisse des Topic-Modellings finden.