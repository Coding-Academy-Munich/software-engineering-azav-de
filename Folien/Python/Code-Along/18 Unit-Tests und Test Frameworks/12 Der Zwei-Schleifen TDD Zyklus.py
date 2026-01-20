# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Der Zwei-Schleifen TDD Zyklus</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# ## Jenseits von Rot-Grün-Refaktor
#
# - Der klassische TDD-Zyklus ist **taktisch**, nicht **strategisch**.
# - Er beantwortet nicht:
#   - Welches Feature soll als Nächstes gebaut werden?
#   - Wie passt die aktuelle Arbeit in das Gesamtbild?
# - Ohne eine übergeordnete Führung können wir uns in Details verlieren, die
#   keinen Geschäftswert liefern ("Gold Plating").

# %% [markdown]
# ## Das Zwei-Schleifen-Modell (Outside-In TDD)
#
# <img src="img/double-loop.png" alt="Double Loop TDD" style="width: 70%;
#   display: block; margin-left: auto; margin-right: auto;"/>
#
# - **Äußere Schleife (Akzeptanztests):** Definiert ein Feature aus der
#   Benutzerperspektive.
# - **Innere Schleife (Unit-Tests):** Implementiert die Funktionalität, um den
#   Akzeptanztest zu erfüllen.

# %% [markdown]
# ### Die Äußere Schleife: Strategische Führung
#
# 1. **Schreiben Sie einen Akzeptanztest:** Formulieren Sie einen Test, der das
#    Geschäfts- oder Benutzerziel beschreibt.
#     - Dieser Test ist eine "ausführbare Spezifikation".
#     - Er wird fehlschlagen, weil die Funktionalität noch nicht existiert.
#     - Zwingt zu Designentscheidungen über die äußere Schnittstelle (z.B.
#       API-Endpunkt) von Anfang an.
#
# 2.  **Verwenden Sie BDD/ATDD:**
#     - **ATDD (Acceptance Test-Driven Development):** Kollaborative Definition
#       der Akzeptanzkriterien mit dem Business.
#     - **BDD (Behavior-Driven Development):** Nutzung einer strukturierten
#       Sprache (z.B. Gherkin) für Tests, um das gemeinsame Verständnis zu
#       fördern.

# %% [markdown]
# ### Die Innere Schleife: Taktische Implementierung
#
# 1.  **Analysiere den Fehlschlag:** Die Fehlermeldung des Akzeptanztests gibt
#     das Ziel für den ersten Unit-Test vor.
#     - *Akzeptanztest schlägt fehl*: `HTTP 404 Not Found für POST /cart`
#     - *Nächster Schritt*: Schreibe einen Unit-Test für einen
#       `CartController`.
#
# 2.  **Red-Green-Refactor Kaskade:**
#     - Schreibe einen fehlschlagenden Unit-Test für den `CartController`.
#     - Schreibe minimalen Code, damit er besteht (z.B. den Controller und den
#       Endpunkt erstellen).
#     - Der Akzeptanz-Test schlägt nun fehl, weil der Controller einen
#       `CartService` aufruft, der nicht existiert.
#     - Dieser neue Fehlschlag leitet den nächsten Unit-Test für den
#       `CartService` ein.
#
# 3.  **Wiederhole:** Dieser Prozess setzt sich fort und treibt die Entwicklung
#     von der Systemgrenze nach innen.

# %% [markdown]
# ## Workshop: Eine To-Do-Listen-Anwendung
#
# **Ziel:** Wir werden eine einfache In-Memory-To-Do-Listen-Anwendung mit dem
# Zwei-Schleifen-Ansatz entwickeln.
#
# **Features:**
# 1. Eine Aufgabe zu einer Liste hinzufügen.
# 2. Alle Aufgaben in der Liste anzeigen.
# 3. Eine Aufgabe als erledigt markieren.
#
# **Hinweis:** Ein Starter-Kit für diese Übung ist im Ordner
# `code/starter_kits/two_loop_cycle_sk` verfügbar.

# %% [markdown]
# ### Umgang mit dem Akzeptanztest während der inneren Schleife
#
# Während wir in der inneren Schleife arbeiten, wollen wir nur unsere
# Unit-Tests ausführen. Der fehlschlagende Akzeptanztest würde sonst:
# - Die Test-Ausgabe unübersichtlich machen
# - Den Build als "fehlgeschlagen" markieren
#
# **pytest bietet mehrere Lösungen:**

# %% [markdown]
# ### Option 1: `@pytest.mark.xfail` (Empfohlen)
#
# Markiert den Test als "erwarteter Fehlschlag":
#
# ```python
# import pytest
#
# @pytest.mark.xfail(reason="Feature noch nicht implementiert")
# def test_full_todo_list_scenario():
#     ...
# ```
#
# - Test läuft, aber Fehlschlag bricht den Build nicht ab
# - Wenn der Test unerwartet besteht, wird dies angezeigt (XPASS)
# - Ideal für TDD: Der Test dokumentiert das Ziel

# %% [markdown]
# ### Option 2: Benutzerdefinierte Marker mit `-m`
#
# Trennt Akzeptanztests von Unit-Tests:
#
# ```python
# import pytest
#
# @pytest.mark.acceptance
# def test_full_todo_list_scenario():
#     ...
#
# def test_new_list_is_empty():  # Unit-Test ohne Marker
#     ...
# ```
#
# ```bash
# # Nur Unit-Tests ausführen (ohne Akzeptanztests)
# pytest -m "not acceptance"
#
# # Nur Akzeptanztests ausführen
# pytest -m acceptance
# ```

# %% [markdown]
# ### Schritt 1: Die äußere Schleife (Rot)
#
# Zuerst schreiben wir einen Akzeptanztest, der das gesamte gewünschte
# Verhalten beschreibt. Dieser Code wird fehlschlagen, weil die Klassen
# `Task` und `TodoList` noch nicht existieren. Das ist der rote Zustand unserer
# äußeren Schleife.

# %% [markdown]
#
# Das ist unser Akzeptanztest.
# Er wird fehlschlagen, weil die Klassen `Task` und `TodoList`
# noch nicht existieren.

# %% [markdown]
# ```python
# def test_full_todo_list_scenario():
#     # Arrange
#     todo_list = TodoList()
#
#     # Act 1: Add tasks
#     todo_list.add_task("Implement Two-Loop TDD")
#     todo_list.add_task("Write workshop slides")
#
#     # Assert 1
#     tasks1 = todo_list.get_tasks()
#     assert len(tasks1) == 2, "Should have 2 tasks after adding"
#     assert tasks1[0].description == "Implement Two-Loop TDD"
#     assert tasks1[0].completed is False, "New task should not be completed"
#
#     # Act 2: Complete a task
#     todo_list.mark_as_complete("Write workshop slides")
#
#     # Assert 2
#     tasks2 = todo_list.get_tasks()
#     completed_task = next(
#         (t for t in tasks2 if t.description == "Write workshop slides"), None
#     )
#     assert completed_task is not None, "Completed task should be found"
#     assert completed_task.completed is True, "Task should be marked as complete"
#     print("Acceptance test passed!")
# ```

# %% [markdown]
# ### Schritt 2: Die innere Schleife (Rot-Grün-Refaktor)
#
# Jetzt konzentrieren wir uns auf den ersten Fehler.
# Python wird sich beschweren, dass `TodoList` nicht existiert. Das ist unser
# Signal, in die innere Schleife einzutauchen.
#
# **Ihre Aufgabe:**
# 1.  Schreiben Sie den **allerersten, kleinsten Unit-Test**, um den Prozess zu
#     starten. Ein guter Anfang wäre ein Test, der prüft, ob eine neu erstellte
#     `TodoList` leer ist.
# 2.  Erstellen Sie die minimalen Klassen (`Task`, `TodoList`) und Methoden,
#     damit dieser erste Unit-Test besteht.
# 3.  Arbeiten Sie sich durch die Fehler des Akzeptanztests. Für jede fehlende
#     Funktionalität (z. B. `add_task`, `mark_as_complete`), schreiben Sie
#     einen neuen, fokussierten Unit-Test und implementieren Sie die
#     Funktionalität.
# 4.  Führen Sie nach jedem inneren Zyklus den Akzeptanztest erneut aus, um
#     Ihren Fortschritt zu sehen.

# %%

# %%

# %%
