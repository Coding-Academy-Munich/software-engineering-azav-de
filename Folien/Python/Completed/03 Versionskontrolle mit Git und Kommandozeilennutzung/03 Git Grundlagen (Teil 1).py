# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Grundlagen (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Git Grundlagen
#
# - Verteiltes Versionskontrollsystem (DVCS)
# - Verfolgt Änderungen an Dateien
# - Ermöglicht Zusammenarbeit in Teams
# - Entwickelt von Linus Torvalds (2005)

# %% [markdown]
#
# ## Was ist ein verteiltes Versionskontrollsystem?
#
# - Jeder Nutzer hat eine vollständige Kopie des Repositories
# - Arbeitet unabhängig vom Netzwerk
# - Dezentrale Architektur
# - Hohe Redundanz und Ausfallsicherheit

# %% [markdown]
#
# <img src="img/distributed-01.png" style="width:50%;margin:auto" alt="Verteiltes Versionskontrollsystem"></img>

# %% [markdown]
#
# ## Hilfe in Git bekommen
#
# ```powershell
# # Allgemeine Hilfe
# git help
# git help -a   # Alle verfügbaren Befehle anzeigen
# git help -g   # Verfügbare Anleitungen anzeigen
# ```
# ```powershell
# # Hilfe zu einem bestimmten Befehl
# git help <Befehl>
# git <Befehl> --help
# git <Befehl> -h   # Kurzübersicht
# ```
# ```powershell
# # Beispiele
# git help commit
# git add --help
# ```

# %% [markdown]
#
# ## Ein Repository erstellen
#
# ```powershell
# # Ein neues Git-Repository initialisieren
# mkdir [projekt]
# cd [projekt]
# git init
# ```
# ```powershell
# # Überprüfen
# ls -Hidden
# ```
#
# Nach `git init`:
# - Ein `.git` Verzeichnis wurde erstellt
# - Enthält die gesamte Datenbank und Konfiguration
# - Löschen dieses Verzeichnisses entfernt die Git-Historie

# %% [markdown]
#
# ## Praktisches Beispiel: Repository erstellen
#
# Erstellen wir ein einfaches Repository für unser Demo-Projekt:
#
# ```powershell
# mkdir GitDemo
# cd GitDemo
# git init
# ls -Hidden
# ls
# ```
# ```powershell
# # Erstellen wir eine einfache Datei
# echo "# Git Demo Projekt" > README.md
# ls
# ```

# %% [markdown]
#
# ## Dateistatus in Git
#
# - **Untracked**: Datei ist Git nicht bekannt
# - **Unmodified**: Datei ist eingecheckt und unverändert
# - **Modified**: Datei wurde verändert seit letztem Commit
# - **Staged**: Aktuelle Version ist für Commit vorgemerkt

# %% [markdown]
#
# ## Repository-Status überprüfen
#
# ```powershell
# git status
# ```
#
# Status-Ausgabe enthält:
# - Aktuellen Branch
# - Geänderte Dateien ("Changes not staged for commit")
# - Dateien in der Staging-Area ("Changes to be committed")
# - Nicht verfolgte Dateien ("Untracked files")
#
# Kurze Statusanzeige:
# ```powershell
# git status -s
# # Oder
# git status --short
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Status überprüfen
#
# Überprüfen wir den Status unseres Demo-Projekts:
#
# ```powershell
# git status
# ```
#
# Die README.md sollte als "untracked" angezeigt werden.

# %% [markdown]
#
# ## Dateien zum Staging-Bereich hinzufügen
#
# Die Staging-Area ist eine Zwischenstufe vor dem Commit.
#
# ```powershell
# # Einzelne Datei hinzufügen
# git add dateiname.txt
# ```
# ```powershell
# # Alle Dateien im aktuellen Verzeichnis hinzufügen
# git add .
# ```
# ```powershell
# # Alle Änderungen (inkl. Löschungen) hinzufügen
# git add -A
# ```
# ```powershell
# # Interaktiv hinzufügen (mit Auswahl)
# git add -i
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Dateien hinzufügen
#
# Fügen wir unsere README-Datei zum Staging-Bereich hinzu:
#
# ```powershell
# git add README.md
# git status
# ```
# ```powershell
# # Fügen wir eine weitere Datei hinzu
# echo "console.log('Hello, Git!');" > app.js
# git status
# ```

# %% [markdown]
#
# ## Änderungen committen
#
# ```powershell
# # Commit mit Nachricht
# git commit -m "Eine aussagekräftige Commit-Nachricht"
# ```
# ```powershell
# # Commit mit detaillierter Nachricht im Editor
# git commit
# ```
# ```powershell
# # Staging und Commit in einem Schritt (nur für bekannte Dateien)
# git commit -am "Nachricht"
# ```
# ```powershell
# # Letzten Commit ändern
# git commit --amend
# ```
#
# Ein Commit ist ein Schnappschuss Ihres Projekts zu einem bestimmten Zeitpunkt.

# %% [markdown]
#
# ## Praktisches Beispiel: Commit erstellen
#
# Committen wir unsere Datei:
#
# ```powershell
# git commit -m "Erstelle README.md mit Projektbeschreibung"
# git status
# ```
# ```powershell
# # Fügen wir jetzt die JS-Datei hinzu und committen sie
# git add app.js
# git commit -m "Füge einfache JavaScript-Datei hinzu"
# ```
