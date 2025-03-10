# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Grundlagen (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Commit-Historie anzeigen
#
# ```powershell
# # Grundlegende Historie anzeigen
# git log
# ```
# ```powershell
# # Kompaktere Ansicht
# git log --oneline
# ```
# ```powershell
# # Mit Darstellung der Änderungen
# git log -p
# ```

# %% [markdown]
#
# # Statistiken anzeigen
# git log --stat
# ```
# ```powershell
# # Grafische Darstellung
# git log --graph --oneline --all
# ```
# ```powershell
# # Nach Autor filtern
# git log --author="Name"
# ```
# ```powershell
# # Nach Zeitraum filtern
# git log --since="2023-01-01" --until="2023-12-31"
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Commit-Historie anzeigen
#
# Schauen wir uns die Historie unseres Demo-Projekts an:
#
# ```powershell
# git log
# git log --oneline
# ```

# %% [markdown]
#
# ## Unterschiede anzeigen
#
# ```powershell
# # Unterschiede im Arbeitsverzeichnis zu Staging-Area/letztem Commit
# git diff
# ```
# ```powershell
# # Unterschiede zwischen Staging-Area und letztem Commit
# git diff --staged    # or --cached
# ```
# ```powershell
# # Unterschiede zwischen zwei Commits
# git diff commit1 commit2
# ```
# ```powershell
# # Unterschiede für eine bestimmte Datei
# git diff -- dateiname.txt
# ```
# ```powershell
# # Unterschiede zwischen Branches
# git diff branch1 branch2
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Unterschiede anzeigen
#
# Ändern wir eine Datei und untersuchen die Unterschiede:
#
# ```powershell
# # Ändern wir die README-Datei
# echo -e "# Git Demo Projekt\n\nEin einfaches Projekt zum Lernen von Git." > README.md
# ```
# ```powershell
# # Unterschiede anzeigen
# git diff
# ```
# ```powershell
# # Zur Staging-Area hinzufügen und Unterschiede erneut anzeigen
# git add README.md
# git diff          # Zeigt nichts an
# git diff --staged # Zeigt die staged Änderungen
# ```

# %% [markdown]
#
# ## Dateien ignorieren mit .gitignore
#
# ```
# # Kommentar
# *.log           # Alle Dateien mit .log-Endung ignorieren
# build/          # Ganzes Verzeichnis ignorieren
# /config.json    # Nur im Root-Verzeichnis ignorieren
# !important.log  # Ausnahme: diese .log-Datei nicht ignorieren
# ```
#
# Typische Patterns:
# - Temporäre Dateien: `*.tmp`, `~*`
# - Build-Artefakte: `dist/`, `build/`, `*.o`
# - Umgebungsdateien: `.env`
# - Abhängigkeiten: `node_modules/`, `vendor/`

# %% [markdown]
#
# ## Praktisches Beispiel: .gitignore erstellen
#
# Erstellen wir eine .gitignore-Datei für unser Projekt:
#
# ```powershell
# # Erstellen wir einige Dateien, die ignoriert werden sollen
# touch temp.log debug.log
# mkdir build
# touch build/output.bin
# ```
# ```powershell
# # Erstellen wir eine .gitignore-Datei
# echo -e "# Logs\n*.log\n\n# Build-Verzeichnis\nbuild/" > .gitignore
# ```
# ```powershell
# # Überprüfen wir den Status
# git status
# ```

# %% [markdown]
#
# ## Dateien löschen und umbenennen
#
# ```powershell
# # Datei aus dem Working Directory und Index entfernen
# git rm datei.txt
# ```
# ```powershell
# # Datei nur aus dem Index entfernen (im Verzeichnis behalten)
# git rm --cached datei.txt
# ```
# ```powershell
# # Datei umbenennen
# git mv alte_datei.txt neue_datei.txt
# ```
#
# Hinter den Kulissen:
# - `git rm` = `rm datei.txt` + `git add datei.txt`
# - `git mv` = `mv alte_datei.txt neue_datei.txt` + `git add neue_datei.txt`

# %% [markdown]
#
# ## Praktisches Beispiel: Dateien löschen und umbenennen
#
# ```powershell
# # Erstellen wir eine Datei zum Löschen
# echo "Zu löschende Datei" > zu_loeschen.txt
# git add zu_loeschen.txt
# git commit -m "Füge zu_loeschen.txt hinzu"
# ```
# ```powershell
# # Datei löschen
# git rm zu_loeschen.txt
# git status
# ```
# ```powershell
# # Umbenennen einer Datei
# git mv app.js main.js
# git status
# ```
# ```powershell
# # Änderungen committen
# git commit -m "Lösche zu_loeschen.txt und benenne app.js in main.js um"
# ```

# %% [markdown]
#
# ## Änderungen rückgängig machen
#
# ```powershell
# # Änderungen in der Working Copy zurücksetzen
# git restore <datei>
# git checkout -- <datei>  # ältere Git-Versionen
# ```
# ```powershell
# # Änderungen aus der Staging-Area entfernen (unstage)
# git restore --staged <datei>
# git reset HEAD <datei>   # ältere Git-Versionen
# ```
# ```powershell
# # Datei auf einen früheren Commit zurücksetzen
# git restore --source=<commit> <datei>
# ```
# ```powershell
# # Letzten Commit ändern
# git commit --amend
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Änderungen rückgängig machen
#
# ```powershell
# # Ändern wir eine Datei
# echo "Fehlerhafte Änderung" >> main.js
# git status
# git diff main.js
# ```
# ```powershell
# # Änderung rückgängig machen
# git restore main.js
# git status
# git diff main.js  # Keine Unterschiede mehr
# ```
# ```powershell
# # Änderung stagen und dann unstagen
# echo "Neue Zeile" >> main.js
# git add main.js
# git status
# ```
# ```powershell
# git restore --staged main.js
# git status  # Die Datei ist nun unstaged, aber immer noch geändert
# ```
