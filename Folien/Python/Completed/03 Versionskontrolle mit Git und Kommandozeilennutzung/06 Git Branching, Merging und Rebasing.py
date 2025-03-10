# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Branching, Merging und Rebasing</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Git Branching, Merging und Rebasing
#
# - Branches: Parallele Entwicklungslinien
# - Merging: Zusammenführen von Branches
# - Rebasing: Alternative Methode zur Integration von Änderungen
# - Kernkonzepte für kollaborative Softwareentwicklung

# %% [markdown]
#
# ## Git-Objekte: Die interne Struktur
#
# <img src="img/commit-and-tree-01.png" style="width:80%;margin:auto">Git Objects</img>
#
# - **Commits**: Snapshots des Projekts mit Metadaten
# - **Trees**: Verzeichnisstrukturen (Baumstrukturen)
# - **Blobs**: Dateiinhalte
# - **Refs**: Zeiger auf Commits (Branches, Tags)

# %% [markdown]
#
# ## Praktischer Einstieg: Beispielprojekt erstellen
#
# ```powershell
# # Neues Verzeichnis erstellen
# mkdir branch-demo
# cd branch-demo
# git init
#
# # Initiale Dateien erstellen
# echo "# Branching Demo" > README.md
# echo "console.log('Main application');" > app.js
# echo "body { font-family: Arial, sans-serif; }" > styles.css
#
# # Erste Änderungen committen
# git add .
# git commit -m "Initial commit mit README, app.js und styles.css"
# ```

# %% [markdown]
#
# ## Git-Branches
#
# <img src="img/branch-and-history-01.png" style="width:80%;margin:auto">Git Branches</img>
#
# - **Branch**: Leichtgewichtiger beweglicher Zeiger auf einen Commit

# %% [markdown]
#
# ## Branches erstellen
#
# ```powershell
# # Aktuellen Branch anzeigen
# git branch
#
# # Neuen Branch erstellen
# git branch feature
#
# # Branch erstellen und gleich wechseln
# git switch -c new-feature
# # ODER in älteren Git-Versionen
# git checkout -b bugfix
# ```
#
# Ein Branch ist nur ein Zeiger auf einen Commit!

# %% [markdown]
#
# ## Praktisches Beispiel: Branches erstellen
#
# ```powershell
# # Branches anzeigen
# git branch
#
# # Feature-Branch erstellen
# git branch feature
#
# # Bugfix-Branch erstellen und gleich wechseln
# git switch -c bugfix
# # ODER
# git checkout -b bugfix
#
# # Alle Branches anzeigen
# git branch
# ```

# %% [markdown]
#
# ## Zwischen Branches wechseln
#
# ```powershell
# # Zu einem existierenden Branch wechseln
# git checkout branch-name
# # ODER in neueren Git-Versionen
# git switch branch-name
#
# # Zum vorherigen Branch zurückkehren
# git checkout -
# git switch -
#
# # Mit unkommittierten Änderungen wechseln
# git checkout -b new-branch  # Nimmt Änderungen mit
# git stash                   # Speichert Änderungen temporär
# git checkout other-branch
# git stash pop               # Holt Änderungen zurück
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Branch-Wechsel und Änderungen
#
# ```powershell
# # Zum bugfix-Branch wechseln (falls noch nicht dort)
# git switch bugfix
#
# # Änderung im bugfix-Branch vornehmen
# echo "console.log('Bug fixed!');" >> app.js
# git add app.js
# git commit -m "Fix critical bug in app.js"
#
# # Zurück zum main-Branch wechseln
# git switch main
#
# # app.js anzeigen (sollte die Bugfix-Änderung nicht enthalten)
# cat app.js
# ```

# %% [markdown]
#
# ## Branches visualisieren
#
# ```powershell
# # Einfache Darstellung mit Graphen
# git log --oneline --decorate --graph --all
#
# # Mit Farbmarkierungen und kompakt
# git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --all
#
# # Graphisches Tool starten (wenn installiert)
# gitk --all &
#
# # Git-internes Visualisierungstool
# git gui &
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Branches visualisieren
#
# ```powershell
# # Änderungen im main-Branch
# git switch main
# echo "// Main-Branch-Update" >> app.js
# git add app.js
# git commit -m "Update app.js im main-Branch"
#
# # Änderungen im feature-Branch
# git switch feature
# echo "h1 { color: blue; }" >> styles.css
# git add styles.css
# git commit -m "Füge blaue Überschriften in styles.css hinzu"
#
# # Branches visualisieren
# git log --oneline --decorate --graph --all
# ```

# %% [markdown]
#
# ## Divergierende Branches
#
# - Branches entwickeln sich unabhängig voneinander
# - Gleiche Dateien können unterschiedlich geändert werden
# - Jeder Branch hat seine eigene Commit-Historie
#
# <img src="img/basic-branching-01.png" style="width:80%;margin:auto">Diverging Branches</img>

# %% [markdown]
#
# ## Praktisches Beispiel: Divergierende Branches
#
# ```powershell
# # Erstellen wir divergierende Änderungen in verschiedenen Branches
#
# # Im main-Branch
# git switch main
# echo "function mainFeature() { return 'main'; }" >> app.js
# git add app.js
# git commit -m "Füge mainFeature Funktion hinzu"
#
# # Im feature-Branch
# git switch feature
# echo "function newFeature() { return 'feature'; }" >> app.js
# git add app.js
# git commit -m "Füge newFeature Funktion hinzu"
#
# # Branches anzeigen
# git log --oneline --decorate --graph --all
# ```

# %% [markdown]
#
# ## Branches zusammenführen mit Merge
#
# ```powershell
# # Zum Ziel-Branch wechseln (wohin soll gemergt werden)
# git switch main
#
# # Merge durchführen
# git merge feature
#
# # Bei einem Fast-Forward-Merge
# git merge feature  # Verschiebt einfach den Branch-Pointer
#
# # Drei-Wege-Merge erzeugt einen Merge-Commit
# git merge feature  # Wenn es Divergenzen gibt
#
# # Merge mit eigener Commit-Nachricht
# git merge --no-ff feature -m "Merge feature Branch"
# ```
#
# <img src="img/basic-merging-01.png" style="width:80%;margin:auto">Merge</img>

# %% [markdown]
#
# ## Praktisches Beispiel: Merging
#
# ```powershell
# # Fast-forward Merge: bugfix in main integrieren
# git switch main
# git merge bugfix
# git log --oneline --decorate --graph --all
#
# # Drei-Wege-Merge: feature in main integrieren
# git merge feature
# git log --oneline --decorate --graph --all
#
# # Erzwungener Merge-Commit mit --no-ff
# git switch main
# git checkout -b new-feature
# echo "// Neue Funktion" >> app.js
# git add app.js
# git commit -m "Füge neue Funktion hinzu"
# git switch main
# git merge --no-ff new-feature -m "Merge new-feature mit --no-ff"
# git log --oneline --decorate --graph --all
# ```

# %% [markdown]
#
# ## Merge-Konflikte lösen
#
# ```powershell
# # Wenn Git einen Konflikt meldet:
# git status  # Zeigt Dateien mit Konflikten
#
# # Öffne die Dateien mit Konflikten im Editor
# # Datei enthält Markierungen:
# # <<<<<<< HEAD
# # Deine Änderungen
# # =======
# # Andere Änderungen
# # >>>>>>> feature
#
# # Nach der Bearbeitung:
# git add <konfliktdatei>  # Konfliktlösung markieren
# git merge --continue     # Merge fortsetzen
# # ODER
# git commit -m "Löse Merge-Konflikt"
#
# # Merge abbrechen
# git merge --abort
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Merge-Konflikt erzeugen und lösen
#
# ```powershell
# # Erzeuge einen Konflikt
# git switch main
# echo "// Diese Zeile wird Konflikt verursachen - main" >> styles.css
# git add styles.css
# git commit -m "Ändere styles.css in main"
#
# git switch feature
# echo "// Diese Zeile wird Konflikt verursachen - feature" >> styles.css
# git add styles.css
# git commit -m "Ändere styles.css in feature"
#
# # Versuche zu mergen (erzeugt Konflikt)
# git switch main
# git merge feature
#
# # Löse den Konflikt
# # 1. Öffne die Datei mit einem Editor
# # 2. Bearbeite die Konfliktmarkierungen
# # 3. Speichere die Datei
# git add styles.css
# git commit -m "Löse Merge-Konflikt in styles.css"
# ```

# %% [markdown]
#
# ## Branch-Management
#
# ```powershell
# # Alle Branches auflisten
# git branch
# git branch -a  # Auch Remote-Branches anzeigen
#
# # Details zu Branches anzeigen
# git branch -v  # Mit letztem Commit
# git branch --merged    # Branches, die in den aktuellen gemergt sind
# git branch --no-merged # Branches, die nicht gemergt sind
#
# # Branch umbenennen
# git branch -m alt-name neuer-name
#
# # Branch löschen
# git branch -d branch-name  # Nur wenn gemergt
# git branch -D branch-name  # Erzwingen (auch wenn nicht gemergt)
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Branch-Management
#
# ```powershell
# # Branches auflisten
# git branch
# git branch -v
#
# # Gemergter vs. nicht-gemergter Branch
# git branch --merged
# git branch --no-merged
#
# # Branch umbenennen
# git branch -m new-feature better-feature
# git branch
#
# # Branch löschen
# git branch -d bugfix  # Sollte funktionieren, falls gemergt
# git branch -d feature  # Zeigt Warnung, falls nicht gemergt
# git branch -D feature  # Erzwingt Löschung
# git branch
# ```

# %% [markdown]
#
# ## Remote Branches und Tracking
#
# ```powershell
# # Remote Branches anzeigen
# git branch -r
#
# # Remote abrufen
# git fetch origin
#
# # Lokalen Branch erstellen, der Remote folgt
# git checkout -b feature origin/feature
# # ODER in neueren Versionen
# git checkout feature  # Erstellt automatisch Tracking-Branch
#
# # Tracking-Informationen anzeigen
# git branch -vv
#
# # Tracking für existierenden Branch einrichten
# git branch -u origin/feature feature
# # ODER
# git branch --set-upstream-to=origin/feature feature
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Remote Branches
#
# ```powershell
# # Wechseln wir zu einem geklonten Repository (aus der vorherigen Lektion)
# cd ~/GitExample
# # Falls nicht vorhanden:
# # git clone https://github.com/Coding-Academy-Munich/GitExample.git
# cd GitExample
#
# # Remote-Branches anzeigen
# git branch -r
#
# # Neuen lokalen Branch erstellen, der einen Remote-Branch verfolgt
# git checkout -b feature origin/main
#
# # Tracking-Informationen anzeigen
# git branch -vv
#
# # Änderungen vom Remote holen
# git fetch origin
# git log --oneline --decorate --graph --all
# ```

# %% [markdown]
#
# ## Rebasing
#
# ```powershell
# # Grundlegendes Rebase
# git switch feature
# git rebase main
#
# # Interaktives Rebase
# git rebase -i HEAD~3  # Letzte 3 Commits
#
# # Rebase abbrechen
# git rebase --abort
#
# # Konflikte während Rebase lösen
# # Nach Konfliktlösung:
# git add <datei>
# git rebase --continue
#
# # Auf Remote-Branch rebasen
# git fetch origin
# git rebase origin/main
# ```
#
# <img src="img/basic-rebase-01.png" style="width:80%;margin:auto">Rebase</img>

# %% [markdown]
#
# ## Praktisches Beispiel: Rebasing
#
# ```powershell
# # Wechseln wir zurück zum branch-demo Verzeichnis
# cd ~/branch-demo
#
# # Erstellen wir einen Branch für das Rebase-Beispiel
# git switch main
# git checkout -b rebase-example
#
# # Änderungen im rebase-example Branch
# echo "// Rebase-Beispiel" >> app.js
# git add app.js
# git commit -m "Änderungen für Rebase-Beispiel"
#
# # Änderungen im main-Branch
# git switch main
# echo "// Main-Update" >> app.js
# git add app.js
# git commit -m "Update im main-Branch"
#
# # Rebase durchführen
# git switch rebase-example
# git rebase main
#
# # Historie anzeigen
# git log --oneline --decorate --graph --all
# ```

# %% [markdown]
#
# ## Rebase vs. Merge
#
# **Merge:**
# - Erstellt einen Merge-Commit
# - Bewahrt die Geschichte (wann wurde gemergt)
# - Keine Änderung bestehender Commits
# - Sicherer für öffentliche/geteilte Branches
#
# **Rebase:**
# - Erzeugt lineare Geschichte
# - "Verschiebt" Commits auf neue Basis
# - Ändert betroffene Commit-Hashes
# - Besser für nicht-geteilte Branches

# %% [markdown]
#
# ## Zusammenfassung
#
# - **Git-Objekte**: Commits, Trees, Blobs bilden die interne Struktur
# - **Branches**: Leichtgewichtige Zeiger auf Commits für parallele Entwicklung
# - **Branch-Wechsel**: `git switch` oder `git checkout`
# - **Branch-Visualisierung**: `git log --graph` oder grafische Tools
# - **Merging**: `git merge` führt Änderungen aus verschiedenen Branches zusammen
# - **Konflikte lösen**: Manuelles Editieren der konfliktmarkierten Dateien
# - **Remote Branches**: Verfolgen des Zustands entfernter Repositories
# - **Rebasing**: `git rebase` für lineare Historie als Alternative zum Mergen
# - **Branch-Management**: Branches organisieren, verfolgen und bereinigen
