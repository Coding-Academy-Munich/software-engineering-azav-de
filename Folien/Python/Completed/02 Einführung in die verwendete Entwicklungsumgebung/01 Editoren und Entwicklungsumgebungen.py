# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Editoren und Entwicklungsumgebungen</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Editoren und Entwicklungsumgebungen<br>(und Compiler, Interpreter)
# ### Wesentliche Werkzeuge für modernes Software-Engineering

# %% [markdown]
#
# ## I. Texteditoren
#
# **Was sind Texteditoren?**
# - Werkzeuge zum Erstellen und Bearbeiten von reinen Textdateien
# - Unterschied zu Textverarbeitungsprogrammen
# - Grundlage der Programmierung und Softwareentwicklung
# - Reichen von einfach (Notepad) bis fortgeschritten (Vim, Emacs, VS Code)

# %% [markdown]
#
# ## II. Codeausführung: Compiler und Interpreter
#
# **Wie wird Code zu laufender Software?**
# - Compiler: Übersetzen gesamten Code in Maschinensprache
# - Interpreter: Führen Code zeilenweise aus
# - Hybride Ansätze (JIT-Kompilierung)
# - Verschiedene Paradigmen für verschiedene Anforderungen

# %% [markdown]
# ## Compiler (C++)
#
# <img src="img/compiler.svg" style="width:60%;margin:auto"/>

# %% [markdown]
# ## Interpreter (Python)
#
# <img src="img/interpreter.svg" style="width:60%;margin:auto"/>

# %% [markdown]
#
# ## III. Jupyter Notebooks
#
# **Interaktive Rechenumgebungen**
# - Code + Dokumentation + Visualisierung in einem Dokument
# - Zellenbasiertes Ausführungsmodell
# - Literarischer Programmieransatz
# - Beliebt in Data Science, Bildung und Forschung

# %% [markdown]
# ## Jupyter Notebooks
#
# <img src="img/jupyter-notebook.svg" style="width:60%;margin:auto"/>

# %%
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# %%
fact(100)

# %% [markdown]
#
# ## IV. Integrierte Entwicklungsumgebungen (IDEs)
#
# **Umfassende Entwicklungswerkzeuge**
# - Mehr als einfache Textbearbeitung
# - Code-Intelligenz-Funktionen
# - Debugging-Möglichkeiten
# - Projektverwaltung
# - Integrierte Toolchains

# %% [markdown]
#
# ## V. Funktionen moderner Entwicklungsumgebungen
#
# **Jenseits von grundlegender Bearbeitung und Kompilierung**
# - Code-Analyse- und Qualitätswerkzeuge
# - Test-Frameworks und -Integration
# - Containerisierung und Cloud-Entwicklung
# - KI-unterstützte Programmierung
# - Remote-Entwicklungsmöglichkeiten
