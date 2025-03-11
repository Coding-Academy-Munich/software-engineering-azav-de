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
