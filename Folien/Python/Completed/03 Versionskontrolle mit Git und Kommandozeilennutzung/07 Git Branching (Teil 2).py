# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Branching (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Divergierende Branches
#
# - Branches entwickeln sich unabhängig voneinander
# - Gleiche Dateien können unterschiedlich geändert werden
# - Jeder Branch hat seine eigene Commit-Historie
#
# <img src="img/basic-branching-05.png" style="width:50%;margin:auto"></img>

# %% [markdown]
#
# ## Praktisches Beispiel: Divergierende Branches
#
# ```powershell
# # Branches anzeigen (GitExample Repository)
# git log --oneline --decorate --graph --all
# ```

# %% [markdown]
#
# ## Branches zusammenführen mit Merge
#
# - Divergierende Branches
#
# <img src="img/basic-merging-01.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# - Mergen des `feature`-Branches in den `main`-Branch
# - Keine Konflikte, da `main` ein direkter Vorfahre von `feature` ist
# - Ein Fast-Forward-Merge wird durchgeführt
#
# <img src="img/basic-merging-02.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# - Mergen des `hotfix`-Branches in den `main`-Branch
# - `main` ist kein direkter Vorfahre von `hotfix`
# - Ein Drei-Wege-Merge wird durchgeführt
# - Ein neuer Merge-Commit wird erzeugt
#
# <img src="img/basic-merging-03.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# ## Branches zusammenführen mit Merge
#
# ```powershell
# # Zum Ziel-Branch wechseln (wohin soll gemergt werden)
# git switch main
# ```
# ```powershell
# # Merge durchführen
# git merge feature
# ```
# ```powershell
# # Bei einem Fast-Forward-Merge
# git merge feature  # Verschiebt einfach den Branch-Pointer
# ```
# ```powershell
# # Drei-Wege-Merge erzeugt einen Merge-Commit
# git merge hotfix  # Wenn es Divergenzen gibt
# ```

# %% [markdown]
#
# ## Merge-Konflikte lösen
#
# ```powershell
# # Wenn Git einen Konflikt meldet:
# git status  # Zeigt Dateien mit Konflikten
# ```
# ```powershell
# # Öffne die Dateien mit Konflikten im Editor
# # Datei enthält Markierungen:
# # <<<<<<< HEAD
# # Deine Änderungen
# # =======
# # Andere Änderungen
# # >>>>>>> feature
# ```

# %% [markdown]
#
# ```powershell
# # Nach der Bearbeitung:
# git add <konfliktdatei>  # Konfliktlösung markieren
# git merge --continue     # Merge fortsetzen
# # ODER
# git commit -m "Löse Merge-Konflikt"
# ```
# ```powershell
# # Merge abbrechen
# git merge --abort
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Merge-Konflikt erzeugen und lösen
#
# ```powershell
# # Wechsle in den master Branch
# git switch main
# # Ändere main/app.js
# # ...
# # Committe die Änderungen im master Branch
# git commit -m "Ändere main/app.js in main"
# ```
# ```powershell
# git switch feature
# # Erzeuge einen Konflikt durch Ändern derselben Stelle in main/app.js
# # ...
# git commit -m "Ändere main/app.js in feature"
# ```
# ```powershell
# # Versuche zu mergen (erzeugt Konflikt)
# git switch main
# git merge feature
# ```

# %% [markdown]
#
# ```powershell
# # Löse den Konflikt
# # 1. Öffne die Datei mit einem Editor
# # 2. Bearbeite die Konfliktmarkierungen
# # 3. Speichere die Datei
# git add main/app.js
# git commit -m "Löse Merge-Konflikt in main/app.js"
# ```

# %% [markdown]
#
# ## Workshop: Merge-Konflikte
#
# - Wechseln Sie in das Git-Repository, das Sie im letzten Workshop angelegt
#   haben. (Oder erzeugen Sie ein neues Repository)
# - Erstellen Sie einen neuen Branch `feature` und ändern Sie eine Datei.
# - Wechseln Sie zurück zum `master`-Branch und ändern Sie dieselbe Datei.
# - Versuchen Sie, den `feature`-Branch in den `master`-Branch zu mergen.
# - Funktioniert der Merge? Falls nicht, lösen Sie den Konflikt.
# - Experimentieren Sie mit verschiedenen Änderungen um zu sehen, welche
#   Änderungen Konflikte verursachen.
# - Versuchen Sie die entstandenen Konflikte zu lösen.

