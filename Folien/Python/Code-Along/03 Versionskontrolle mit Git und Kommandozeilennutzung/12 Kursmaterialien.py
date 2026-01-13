# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Kursmaterialien</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Kursmaterialien
#
# ### GitHub-Seite
#
# https://github.com/Coding-Academy-Munich/software-engineering-azav-de
#
# ### Link zum Repository
#
# https://github.com/Coding-Academy-Munich/software-engineering-azav-de.git

# %% [markdown]
#
# ## Layout des Repositories
#
# ```
# .
# ├── Folien
# │   ├── Html
# │   │   ├── Code-Along
# │   │   └── Completed
# │   ├── Notebooks
# │   │   ├── Code-Along
# │   │   └── Completed
# │   └── Python
# │       └── Completed
# └── Projekte
#     ├── GitExample
#     ├── GraspAdventure
#     └── ...
# ```


# %% [markdown]
#
# ## Inhalt der Folien-Ordner
#
# ```
# .
# ├── Folien
# │   ├── Html
# │   │   ├── Code-Along
# │   │   │   ├── 01 Einführung in Software Engineering und Kursüberblick
# │   │   │   ├── 02 Einführung in die verwendete Entwicklungsumgebung
# │   │   │   └── ...
# │   │   └── Completed
# │   │       ├── 01 Einführung in Software Engineering und Kursüberblick
# │   │       ├── 02 Einführung in die verwendete Entwicklungsumgebung
# │   │       └── ...
# │   ├── Notebooks
# │   │   ├── Code-Along
# │   │   │   ├── 01 Einführung in Software Engineering und Kursüberblick
# │   │   │   ├── 02 Einführung in die verwendete Entwicklungsumgebung
# │   │   │   └── ...
# │   │   └── Completed
# │   │       ├── 01 Einführung in Software Engineering und Kursüberblick
# │   │       ├── 02 Einführung in die verwendete Entwicklungsumgebung
# │   │       └── 06 ...
# │   └── Python
# │       └── Completed
# │           ├── 01 Einführung in Software Engineering und Kursüberblick
# │           ├── 02 Einführung in die verwendete Entwicklungsumgebung
# │           └── ...
# └── Projekte
#     └── ...
# ```

# %% [markdown]
#
# ## Empfohlene Vorgehensweise
#
# 1. Repository klonen
# 2. Erstellen eines eigenen Branches `local/v1`
#    - `git switch -c local/v1 origin/master`
# 3. Täglich:
#    - `git fetch origin`
#    - `git rebase origin/master` des Branches `local/v1`
# 4. Bei Konflikten, die schwer zu lösen sind:
#    - `git rebase --abort`
#    - `git switch -c local/v2 origin/master`
# 5. Workshops bearbeiten, Lösungen in `local/v1` committen
#    - Bzw. in `local/v2`, `local/v3`, ...
