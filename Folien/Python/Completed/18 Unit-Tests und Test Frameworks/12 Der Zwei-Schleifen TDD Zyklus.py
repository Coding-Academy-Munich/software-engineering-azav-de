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
# ## Kata: Eine To-Do-Listen-Anwendung
#
# **Ziel:** Wir werden eine einfache In-Memory-To-Do-Listen-Anwendung mit dem
# Zwei-Schleifen-Ansatz entwickeln.
#
# **Features:**
# 1. Eine Aufgabe zu einer Liste hinzufügen.
# 2. Alle Aufgaben in der Liste anzeigen.
# 3. Eine Aufgabe als erledigt markieren.
# 4. Eine erledigte Aufgabe löschen.
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
# ## Der Akzeptanztest definiert das Design
#
# - Das Schreiben des Akzeptanztests ist eine **Designentscheidung**.
# - Wir entscheiden, wie die API unseres Systems aussehen soll.
# - Verschiedene Designs führen zu unterschiedlichen Akzeptanztests.
# - Wir werden drei verschiedene Designansätze erkunden:
#   1. **Objektorientiert mit Property**: Zugriff über `.tasks`-Eigenschaft
#   2. **Listen-ähnlich**: `len(todo_list)`, `todo_list[0]`, `del todo_list[...]`
#   3. **Funktional**: Freie Funktionen + einfache Dictionaries

# %% [markdown]
# ### Variante 1: Objektorientiert mit Property
#
# ```python
# def test_todo_list_scenario_v1():
#     todo_list = TodoListV1()
#
#     todo_list.add("Implement TDD")
#     todo_list.add("Write slides")
#     todo_list.add("Review materials")
# ```
#
# ```python
#     assert len(todo_list.tasks) == 3
#     assert todo_list.tasks[0].description == "Implement TDD"
#
#     todo_list.mark_completed("Write slides")
#     todo_list.delete("Write slides")
#
#     assert len(todo_list.tasks) == 2
# ```

# %% [markdown]
# ### Variante 2: Listen-ähnliche Schnittstelle
#
# ```python
# def test_todo_list_scenario_v2():
#     todo_list = TodoListV2()
#
#     todo_list.add("Implement TDD")
#     todo_list.add("Write slides")
#     todo_list.add("Review materials")
# ```
#
# ```python
#     assert len(todo_list) == 3                     # __len__
#     assert todo_list[0].description == "Implement TDD"  # __getitem__(int)
#     assert "Write slides" in todo_list            # __contains__
#
#     todo_list["Write slides"].completed = True    # __getitem__(str)
#     del todo_list["Write slides"]                 # __delitem__
#
#     assert len(todo_list) == 2
# ```

# %% [markdown]
# ### Variante 3: Funktional mit Dictionaries
#
# ```python
# def test_todo_list_scenario_v3():
#     todo_list: list[dict] = []                    # Einfache Liste!
#
#     add_task(todo_list, "Implement TDD")
#     add_task(todo_list, "Write slides")
#     add_task(todo_list, "Review materials")
# ```
#
# ```python
#     assert len(todo_list) == 3
#     assert todo_list[0]["description"] == "Implement TDD"
#
#     mark_task_completed(todo_list, "Write slides")
#     delete_task(todo_list, "Write slides")
#
#     assert len(todo_list) == 2
# ```

# %% [markdown]
# ### Design-Kompromisse
#
# | Ansatz | Vorteile | Nachteile |
# |--------|----------|-----------|
# | **OO mit Property** | Klare Kapselung, explizite Methoden | Mehr Boilerplate |
# | **Listen-ähnlich** | Pythonisch, vertraute Syntax | Komplexere Implementierung |
# | **Funktional** | Einfache Daten, leicht zu serialisieren | Keine Kapselung |
#
# Wir implementieren alle drei Varianten, um die unterschiedlichen
# Designentscheidungen zu demonstrieren.

# %% [markdown]
# ## Implementierung: Variante 1 (OO mit Property)
#
# Wir beginnen mit der objektorientierten Variante als Übung für die innere
# Schleife.

# %% [markdown]
# ### Schritt 1: Die äußere Schleife (Rot)
#
# Zuerst schreiben wir einen Akzeptanztest, der das gesamte gewünschte
# Verhalten beschreibt. Dieser Code wird fehlschlagen, weil die Klassen
# `TaskV1` und `TodoListV1` noch nicht existieren.

# %% [markdown]
# ### Schritt 2: Die innere Schleife (Rot-Grün-Refaktor)
#
# **Ihre Aufgabe:**
# 1. Schreiben Sie den **allerersten, kleinsten Unit-Test**, z.B. ob eine neue
#    `TodoListV1` leer ist.
# 2. Erstellen Sie die minimalen Klassen (`TaskV1`, `TodoListV1`) und Methoden.
# 3. Arbeiten Sie sich durch die Fehler des Akzeptanztests.
# 4. Führen Sie nach jedem Zyklus den Akzeptanztest erneut aus.

# %% [markdown]
#
# ### Lösung Variante 1: Die Datenstrukturen

# %%
from dataclasses import dataclass


# %%
@dataclass
class TaskV1:
    description: str
    completed: bool = False


# %%
class TodoListV1:
    def __init__(self):
        self._tasks: list[TaskV1] = []

    @property
    def tasks(self) -> list[TaskV1]:
        return self._tasks

    def add(self, description: str) -> None:
        self._tasks.append(TaskV1(description))

    def mark_completed(self, description: str) -> None:
        for task in self._tasks:
            if task.description == description:
                task.completed = True
                return

    def delete(self, description: str) -> None:
        self._tasks = [t for t in self._tasks if t.description != description]


# %% [markdown]
# ### Lösung Variante 1: Unit-Tests

# %%
def test_v1_new_list_is_empty():
    todo_list = TodoListV1()
    assert len(todo_list.tasks) == 0


# %%
test_v1_new_list_is_empty()


# %%
def test_v1_add_task():
    todo_list = TodoListV1()
    todo_list.add("Test task")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].description == "Test task"
    assert todo_list.tasks[0].completed is False


# %%
test_v1_add_task()


# %%
def test_v1_mark_completed():
    todo_list = TodoListV1()
    todo_list.add("Task to complete")
    todo_list.mark_completed("Task to complete")
    assert todo_list.tasks[0].completed is True


# %%
test_v1_mark_completed()


# %%
def test_v1_delete():
    todo_list = TodoListV1()
    todo_list.add("Task to delete")
    todo_list.add("Task to keep")
    todo_list.delete("Task to delete")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].description == "Task to keep"


# %%
test_v1_delete()


# %% [markdown]
# ### Lösung Variante 1: Vollständiger Akzeptanztest

# %%
def test_full_todo_list_scenario_v1():
    # Arrange
    todo_list = TodoListV1()

    # Act 1: Add tasks
    todo_list.add("Implement Two-Loop TDD")
    todo_list.add("Write workshop slides")
    todo_list.add("Review course materials")

    # Assert 1: Verify all tasks added via .tasks property
    assert len(todo_list.tasks) == 3
    assert todo_list.tasks[0].description == "Implement Two-Loop TDD"
    assert all(not task.completed for task in todo_list.tasks)

    # Act 2: Complete a task
    todo_list.mark_completed("Write workshop slides")

    # Assert 2: Verify completion state
    completed = [t for t in todo_list.tasks if t.completed]
    pending = [t for t in todo_list.tasks if not t.completed]
    assert len(completed) == 1
    assert completed[0].description == "Write workshop slides"
    assert len(pending) == 2

    # Act 3: Delete the completed task
    todo_list.delete("Write workshop slides")

    # Assert 3: Verify deletion
    assert len(todo_list.tasks) == 2
    assert all(t.description != "Write workshop slides" for t in todo_list.tasks)
    print("Variant 1 acceptance test passed!")


# %%
test_full_todo_list_scenario_v1()


# %% [markdown]
# ## Implementierung: Variante 2 (Listen-ähnlich)
#
# Diese Variante implementiert das Python Data Model für eine listen-ähnliche
# Schnittstelle.

# %%
@dataclass
class TaskV2:
    description: str
    completed: bool = False


# %%
class TodoListV2:
    def __init__(self):
        self._tasks: list[TaskV2] = []

    def __len__(self) -> int:
        return len(self._tasks)

    def __getitem__(self, key: int | str) -> TaskV2:
        if isinstance(key, int):
            return self._tasks[key]
        for task in self._tasks:
            if task.description == key:
                return task
        raise KeyError(key)

    def __contains__(self, description: str) -> bool:
        return any(t.description == description for t in self._tasks)

    def __iter__(self):
        return iter(self._tasks)

    def __delitem__(self, description: str) -> None:
        self._tasks = [t for t in self._tasks if t.description != description]

    def add(self, description: str) -> None:
        self._tasks.append(TaskV2(description))


# %% [markdown]
# ### Variante 2: Akzeptanztest

# %%
def test_full_todo_list_scenario_v2():
    # Arrange
    todo_list = TodoListV2()

    # Act 1: Add tasks
    todo_list.add("Implement Two-Loop TDD")
    todo_list.add("Write workshop slides")
    todo_list.add("Review course materials")

    # Assert 1: List-like access
    assert len(todo_list) == 3
    assert todo_list[0].description == "Implement Two-Loop TDD"
    assert todo_list["Write workshop slides"].description == "Write workshop slides"
    assert "Write workshop slides" in todo_list

    # Act 2: Complete a task using bracket access
    todo_list["Write workshop slides"].completed = True

    # Assert 2: Check completion using iteration
    completed_task = todo_list["Write workshop slides"]
    assert completed_task.completed is True
    assert sum(1 for t in todo_list if not t.completed) == 2

    # Act 3: Delete the completed task using del
    del todo_list["Write workshop slides"]

    # Assert 3: Verify deletion
    assert len(todo_list) == 2
    assert "Write workshop slides" not in todo_list
    print("Variant 2 acceptance test passed!")


# %%
test_full_todo_list_scenario_v2()


# %% [markdown]
# ## Implementierung: Variante 3 (Funktional)
#
# Diese Variante verwendet einfache Dictionaries und freie Funktionen.

# %%
def add_task(todo_list: list[dict], description: str) -> None:
    """Add a new task to the todo list."""
    todo_list.append({"description": description, "completed": False})


def find_task(todo_list: list[dict], description: str) -> dict | None:
    """Find a task by description."""
    return next((t for t in todo_list if t["description"] == description), None)


def mark_task_completed(todo_list: list[dict], description: str) -> None:
    """Mark a task as completed."""
    task = find_task(todo_list, description)
    if task:
        task["completed"] = True


def delete_task(todo_list: list[dict], description: str) -> None:
    """Delete a task from the todo list."""
    for i, task in enumerate(todo_list):
        if task["description"] == description:
            del todo_list[i]
            return


# %% [markdown]
# ### Variante 3: Akzeptanztest

# %%
def test_full_todo_list_scenario_v3():
    # Arrange: Simple list of dicts - no class needed!
    todo_list: list[dict] = []

    # Act 1: Add tasks using free functions
    add_task(todo_list, "Implement Two-Loop TDD")
    add_task(todo_list, "Write workshop slides")
    add_task(todo_list, "Review course materials")

    # Assert 1: Direct list/dict access
    assert len(todo_list) == 3
    assert todo_list[0]["description"] == "Implement Two-Loop TDD"
    assert all(not task.get("completed", False) for task in todo_list)

    # Act 2: Complete a task
    mark_task_completed(todo_list, "Write workshop slides")

    # Assert 2: Check completion
    completed = [t for t in todo_list if t.get("completed")]
    pending = [t for t in todo_list if not t.get("completed")]
    assert len(completed) == 1
    assert completed[0]["description"] == "Write workshop slides"
    assert len(pending) == 2

    # Act 3: Delete completed task
    delete_task(todo_list, "Write workshop slides")

    # Assert 3: Verify deletion
    assert len(todo_list) == 2
    assert not any(t["description"] == "Write workshop slides" for t in todo_list)
    print("Variant 3 acceptance test passed!")


# %%
test_full_todo_list_scenario_v3()


# %% [markdown]
# ## Zusammenfassung
#
# - Der Akzeptanztest definiert das Design der API.
# - Drei verschiedene Designs führen zu drei unterschiedlichen Implementierungen:
#   - **V1**: Objektorientiert mit `.tasks`-Property
#   - **V2**: Listen-ähnlich mit `__len__`, `__getitem__`, `del`
#   - **V3**: Funktional mit freien Funktionen und Dictionaries
# - Alle erfüllen dieselben Anforderungen, aber mit unterschiedlicher API.

# %%
def run_all_variant_tests():
    test_full_todo_list_scenario_v1()
    test_full_todo_list_scenario_v2()
    test_full_todo_list_scenario_v3()
    print("\n--- All variant tests passed! ---")


# %%
run_all_variant_tests()

# %%
