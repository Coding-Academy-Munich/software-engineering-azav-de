# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Branching (Teil 1)</b>
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
# <img src="img/commit-and-tree-01.png" style="width:80%;margin:auto"></img>

# %% [markdown]
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
# git clone https://github.com/Coding-Academy-Munich/GitExample.git
# cd GitExample
# ```

# %% [markdown]
#
# ## Git-Commits
#
# <img src="img/history-01.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# ## Git-Branches
#
# - **Branch**: Leichtgewichtiger beweglicher Zeiger auf einen Commit
#
# <img src="img/branch-and-history-01.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# ## Branches erstellen
#
# ```powershell
# # Aktuellen Branch anzeigen
# git branch
# ```
# ```powershell
# # Neuen Branch erstellen
# git branch feature
# ```
# ```powershell
# # Zum neuen Branch wechseln
# git switch feature
# ```

# %% [markdown]
#
# ## Git-Branches
#
# - **Branch**: Leichtgewichtiger beweglicher Zeiger auf einen Commit
#
# <img src="img/branch-and-history-02.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# ## Aktueller Branch
#
# - `HEAD`: Leichtgewichtiger beweglicher Zeiger auf aktuellen Branch (oder Commit)
#
# <img src="img/branch-and-history-03.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# ```powershell
# # Branch erstellen und gleich wechseln
# git switch -c feature
# ```
# ```powershell
# # ODER in älteren Git-Versionen
# git checkout -b feature
# ```

# %% [markdown]
#
# ## Branching Beispiel
#
# - Ausgangszustand: Ein Branch (master)
#
# <img src="img/basic-branching-01.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# - Erzeugen eines neuen Branches (`feature`)
# - Wechseln zum neuen Branch
#
# <img src="img/basic-branching-02.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# - Änderungen im neuen Branch
# - Committen der Änderungen
#
# <img src="img/basic-branching-03.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# - Wechseln zurück zum `master`-Branch
# - Hotfix basierend auf `master` erstellen (in neuem Branch `hotfix`)
#
# <img src="img/basic-branching-04.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# - Hinzufügen von Änderungen zum `hotfix`-Branch
# - Committen der Änderungen
#
# <img src="img/basic-branching-05.png" style="width:80%;margin:auto"></img>

# %% [markdown]
#
# ## Praktisches Beispiel: Branches erstellen
#
# ```powershell
# # Branches anzeigen
# git branch
# ```
# ```powershell
# # Feature-Branch erstellen
# git branch feature
# ```
# ```powershell
# # Zum feature Branch wechseln
# git switch feature
# ```
# ```powershell
# # Änderungen im feature Branch vornehmen
# # Änderungen committen
# git add -A
# git commit -m "Add new feature"
# ```

# %% [markdown]
# ```powershell
# # Zurück zum master-Branch wechseln
# git switch master
# ```
# ```powershell
# # Bugfix-Branch erstellen und gleich wechseln
# git switch -c hotfix
#
# # Alle Branches anzeigen
# git branch
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
# # Branches visualisieren
# git log --oneline --decorate --graph --all
# ```
