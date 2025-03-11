# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Branching (Teil 4)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# - Erinnerung: Merging
#
# <img src="img/basic-merging-03.png" style="width:80%;margin:auto"></img>


# %% [markdown]
#
# - Rebasing
#
# <img src="img/basic-rebase-01.png" style="width:80%;margin:auto">Rebase</img>

# %% [markdown]
#
# ## Rebasing
#
# ```powershell
# # Grundlegendes Rebase
# git switch feature
# git rebase main
# ```
# ```powershell
# # Rebase abbrechen
# git rebase --abort
# ```
# ```powershell
# # Konflikte während Rebase lösen
# # Nach Konfliktlösung:
# git add <datei>
# git rebase --continue
# ```

# %% [markdown]
#
# ## Praktisches Beispiel: Rebasing
#
# (Siehe Demonstration)

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
