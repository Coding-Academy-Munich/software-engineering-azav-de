# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Grundlagen (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Remote Repositories nutzen
#
# ```powershell
# # Repository klonen
# git clone https://github.com/username/repository.git
# git clone https://github.com/username/repository.git lokaler_name
# ```
# ```powershell
# # Remotes anzeigen
# git remote -v
# ```
# ```powershell
# # Remote hinzufügen
# git remote add <name> <url>
# ```
# ```powershell
# # Änderungen vom Remote abrufen (ohne Merge)
# git fetch <remote>
# ```
# ```powershell
# # Änderungen abrufen und integrieren
# git pull <remote> <branch>
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Remote Repository klonen
#
# Klonen wir ein Beispiel-Repository:
#
# ```powershell
# # Wechseln wir ins Kurs-Verzeichnis
# cd ~/AZAV
# ```
# ```powershell
# # Klonen des Beispiel-Repositories
# git clone https://github.com/Coding-Academy-Munich/GitExample.git
# ```
# ```powershell
# # Verzeichnis wechseln und Remotes anzeigen
# cd GitExample
# git remote -v
# ```
# ```powershell
# # Commit-Historie anzeigen
# git log --oneline
# ```

# %% [markdown]
#
# ## Zusammenfassung: Git Grundlagen
#
# - `git init`: Repository initialisieren
# - `git status`: Dateistatus überprüfen
# - `git add`: Dateien zum Staging-Bereich hinzufügen
# - `git commit`: Änderungen ins Repository übernehmen
# - `git log`: Commit-Historie anzeigen
# - `git diff`: Unterschiede anzeigen
# - `.gitignore`: Dateien ignorieren
# - `git clone`: Remote-Repository klonen
# - `git remote`: Remote-Verbindungen verwalten
# - `git fetch`, `git pull`: Änderungen vom Remote holen
#
# Im nächsten Video: Branching, Merging und weitere Konzepte.

# %% [markdown]
#
# ## Resources for more information
#
# - Git documentation: https://git-scm.com/doc
# - Pro Git book (free): https://git-scm.com/book
# - Git Cheatsheet: https://education.github.com/git-cheat-sheet-education.pdf


# %% [markdown]
#
# ## Workshop: Erstellen eines Git Repositories
#
# Erstellen Sie ein Git Repository, fügen Sie Dateien hinzu, bearbeiten Sie die
# Dateien. Führen Sie mehrere Commits durch, verwenden Sie die besprochenen
# Befehle um den Status des Repositories anzuzeigen, die Änderungen zu
# verfolgen, usw.
#
# ### Mögliche Aktionen
#
# (Die folgenden Operationen sind nur Beispiele, die Sie beliebig erweitern
# können.)
#
# - Legen Sie ein Verzeichnis `GitWorkshop` an, initialisieren Sie darin ein
#   leeres Git Repository.
# - Erzeugen Sie Dateien `datei1.txt` und `datei2.txt` mit kurzen Texten.
# - Stagen und committen Sie die Dateien.
# - Überprüfen Sie den Zustand Ihres Repositories mit `git status`, `git log`
#   und `git diff` mit verschiedenen Optionen.
# - Ändern Sie den Inhalt einer Datei, überprüfen Sie den Zustand des
#   Repositories.
# - Committen Sie die Datei, überprüfen Sie den Zustand Ihres Repositories.
# - Fügen Sie zusätzliche Dateien hinzu, löschen Sie Dateien, benennen Sie
#   Dateien um oder verschieben Sie sie, ändern Sie die Inhalte der Dateien.
# - Committen Sie dabei regelmäßig und überprüfen Sie den Zustand des
#   Repositories.
