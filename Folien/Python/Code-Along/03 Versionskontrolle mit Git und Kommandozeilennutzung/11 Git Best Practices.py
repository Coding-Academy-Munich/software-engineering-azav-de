# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Git Best Practices</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Git Best Practices
#
# - Konsistente Commit-Strategien
# - Effektives Branching
# - Klare Kommunikation im Team
# - Sauberes Repository-Management
# - Sinnvolle Workflows

# %% [markdown]
#
# ## Aussagekräftige Commit-Nachrichten
#
# - Kurze, prägnante Betreffzeile (max. 50 Zeichen)
# - Leerzeile nach Betreff
# - Detaillierte Beschreibung im Hauptteil (optional)
# - Schreiben im Imperativ: "Fix bug" statt "Fixed bug"
# - Erklären **warum** eine Änderung gemacht wurde, nicht nur was
#
# ```powershell
# # Beispiel für gute Commit-Nachricht
# git commit -m "Add user authentication feature
#
# - Implement OAuth2 login with Google
# - Create session management
# - Add remember-me functionality
#
# Closes #42"
# ```

# %% [markdown]
#
# ## Atomic Commits
#
# - Ein Commit sollte eine einzelne, logische Änderung enthalten
# - Keine unzusammenhängenden Änderungen mischen
# - Erleichtert das Verständnis der Projektgeschichte
# - Macht Rollbacks und Debugging einfacher
#
# ```powershell
# # Beispiel: Staging bestimmter Dateien
# git add src/auth/login.js
# git commit -m "Fix login validation logic"
#
# # Für verschiedene Änderungen in derselben Datei
# git add -p src/app.js  # Interaktives Staging von Teilen einer Datei
# # (Einfacher in VS Code)
# ```

# %% [markdown]
#
# ## Effektives Branching
#
# - Branches für neue Features, Bugfixes und Experimente erstellen
# - Kurze Lebensdauer von Feature-Branches anstreben
# - Regelmäßig vom Hauptbranch (main/master) aktualisieren
# - Klare Branch-Namenskonventionen einhalten
#
# ```powershell
# # Feature-Branch erstellen und wechseln
# git switch -c feature/user-profile
#
# # Vom main-Branch aktualisieren
# git switch feature/user-profile
# git rebase main
# ```

# %% [markdown]
#
# ## Branch-Namenskonventionen
#
# Gemeinsame Präfixe für unterschiedliche Branch-Typen:
#
# - `feature/` - Neue Funktionen
# - `bugfix/` - Fehlerbehebungen
# - `hotfix/` - Dringende Produktionsprobleme
# - `release/` - Release-Vorbereitungen
# - `refactor/` - Code-Umstrukturierungen
#
# ```powershell
# git switch -c feature/login-page
# git switch -c bugfix/password-reset
# git switch -c hotfix/security-vulnerability
# ```

# %% [markdown]
#
# ## Git Workflow-Modelle
#
# - **Git Flow**: Strukturierter Workflow mit development, feature, release,
#   hotfix und master Branches
# - **GitHub Flow**: Vereinfachter Workflow mit feature Branches und Pull
#   Requests
# - **GitLab Flow**: Erweiterung von GitHub Flow mit Pre-Production/Release
#   Branches
# - **Trunk-Based Development**: Alle Entwicklungen erfolgen am Hauptbranch

# %% [markdown]
#
# ## Pull Requests / Merge Requests
#
# - Code-Reviews vor dem Merge in den Hauptbranch
# - Qualitätssicherung durch Peer-Reviews
# - Wissensaustausch im Team
# - Automatisierte Tests und CI/CD-Integration
#
# Best Practices:
# - Kleine, fokussierte PRs erstellen
# - Klare Beschreibung der Änderungen
# - Selbst-Review vor Abgabe durchführen
# - Konstruktives Feedback geben

# %% [markdown]
#
# ## .gitignore richtig nutzen
#
# - Verhindern Sie, dass unnötige Dateien ins Repository gelangen
# - Ignorieren Sie Build-Artefakte, Abhängigkeiten und lokale Konfigurationen
# - Nutzen Sie Templates für Ihre Programmiersprache/Framework

# %% [markdown]
#
# ```
# # Beispiel .gitignore für Node.js Projekt
# node_modules/
# .env
# dist/
# .cache/
# *.log
# .DS_Store
# coverage/
# ```
#
# Templates finden: [gitignore.io](https://www.gitignore.io/)

# %% [markdown]
#
# ## Konfliktlösung
#
# - Regelmäßig vom Hauptbranch aktualisieren, um Konflikte zu minimieren
# - Konflikte sofort nach dem Auftreten lösen
# - Bei komplexen Konflikten mit dem Autor der Änderungen sprechen
#
# ```powershell
# # Konflikte während Merge/Rebase ansehen
# git status
#
# # Nach dem Bearbeiten der Konfliktdateien
# git add <konfliktdatei>
# git rebase --continue  # (oder git merge --continue)
# ```

# %% [markdown]
#
# ## Sicherheit und Datenschutz
#
# - Niemals sensible Daten ins Repository einchecken
#   - Passwörter, API-Schlüssel, Tokens
#   - Produktionsdaten, persönlich identifizierbare Informationen
# - Für Umgebungsvariablen `.env.example`-Dateien verwenden
# - Git-Hooks für Pre-commit Überprüfungen nutzen
#
# ```powershell
# # Falls doch sensible Daten eingecheckt wurden
# git filter-branch --force --index-filter \
# "git rm --cached --ignore-unmatch path/to/sensitive/file" \
# --prune-empty --tag-name-filter cat -- --all
# ```

# %% [markdown]
#
# ## Sinnvolle Commit-Häufigkeit
#
# - Committen Sie früh und oft
# - Idealerweise bei jedem abgeschlossenen logischen Schritt
# - Vor dem Verlassen des Arbeitsplatzes
# - Vor riskanten Änderungen

# %% [markdown]
#
# ## Repository-Pflege
#
# - Regelmäßige Überprüfung und Bereinigung
# - Große Binärdateien vermeiden oder mit Git LFS verwalten
# - Alte Branches löschen, die nicht mehr benötigt werden
#
# ```powershell
# # Veraltete Remote-Tracking-Branches bereinigen
# git fetch --prune
#
# # Geschlossene Feature-Branches löschen
# git branch -d feature/completed-feature
#
# # Auf dem Remote-Repository löschen
# git push origin --delete feature/completed-feature
# ```
