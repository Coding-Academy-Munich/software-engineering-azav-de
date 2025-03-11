# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Branching (Teil 3)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Branch-Management
#
# ```powershell
# # Alle Branches auflisten
# git branch
# git branch -a  # Auch Remote-Branches anzeigen
# ```
# ```powershell
# # Details zu Branches anzeigen
# git branch -v  # Mit letztem Commit
# git branch --merged    # Branches, die in den aktuellen gemergt sind
# git branch --no-merged # Branches, die nicht gemergt sind
# ```

# %% [markdown]
#
# ```powershell
# # Branch umbenennen
# git branch -m alt-name neuer-name
# ```
# ```powershell
# # Branch löschen
# git branch -d branch-name  # Nur wenn gemergt
# git branch -D branch-name  # Erzwingen (auch wenn nicht gemergt)
# ```

# %% [markdown]
#
# ## Remote Branches und Tracking
#
# ```powershell
# # Remote Branches anzeigen
# git branch -r
# ```
# ```powershell
# # Remote abrufen
# git fetch origin
# ```
# ```powershell
# # Lokalen Branch erstellen, der Remote folgt
# git switch feature  # Erstellt automatisch Tracking-Branch
# ```

# %% [markdown]
#
# ```powershell
# # Tracking-Informationen anzeigen
# git branch -vv
# ```
# ```powershell
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
# # Falls nicht vorhanden:
# # git clone https://github.com/Coding-Academy-Munich/GitExample.git
# cd GitExample
# ```
# ```powershell
# # Remote-Branches anzeigen
# git branch -r
# ```
# ```powershell
# # Neuen lokalen Branch erstellen, der einen Remote-Branch verfolgt
# git switch feature-1  # Erstellt automatisch Tracking-Branch (*)
# ```
# (*) Wenn es einen Branch `origin/feature-1`gibt und keinen lokalen Branch `feature-1`
# ```powershell
# # Tracking-Informationen anzeigen
# git branch -vv
# ```
# ```powershell
# # Änderungen vom Remote holen
# git fetch origin
# git log --oneline --decorate --graph --all
# ```
