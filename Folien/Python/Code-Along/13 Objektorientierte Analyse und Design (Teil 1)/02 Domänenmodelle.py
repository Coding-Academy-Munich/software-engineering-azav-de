# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Domänenmodelle</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Was ist ein Domänenmodell?
#
# - Eine **konzeptionelle Repräsentation** einer bestimmten Domäne.
# - **Zweck**: Verständnis und Dokumentation, wie Daten-Elemente innerhalb einer
#   Domäne interagieren.
# - **Beinhaltet** (bei OOAD):
#   - Klassen
#   - Assoziationen (Beziehungen)
#   - Attribute
#   - Operationen

# %% [markdown]
# <div style="display: flex; align-items: flex-start;">
#     <div style="flex: 1; padding-right: 20px;">
#         <h2>Domänenmodelle</h2>
#         <p>Wir wollen Domänenmodelle in verschiedenen Branchen betrachten.</p>
#         <ul>
#             <li>E-Commerce</li>
#             <li>Selbstfahrende Autos</li>
#             <li>Bankenwesen</li>
#         </ul>
#     </div>
#     <div style="flex: 1;">
#         <img src="img/e-commerce.png" alt="E-commerce" style="width: 100%; max-width: 500px;">
#         <img src="img/cars.png" alt="Selbstfahrende Autos" style="width: 100%; max-width: 500px;">
#         <img src="img/bank.png" alt="Selbstfahrende Autos" style="width: 100%; max-width: 500px;">
#     </div>
# </div>

# %% [markdown]
#
# ### Wie finden wir Klassen und Operationen?
#
# - Klassen sind oft Konzepte, die in der Domäne vorkommen
#   - Personen, Orte, Dinge, ...
#   - Abstrakte Konzepte
#   - Im Beschreibungen oft Substantive
# - Operationen sind oft Verben
#   - Oft werden "Dinge, die mit einer Entität gemacht werden" zu Operationen

# %% [markdown]
#
# **Allerdings:** Das ist nicht immer so einfach!
#
# Viele Konzepte können sowohl als Substantiv als auch als Verb ausgedrückt werden:
#
# - Der Kunde **bestellt** ein Produkt.
# - Der Kunde gibt eine **Bestellung** auf.
#
# (Manchmal findet man beides im Domänenmodell wieder.)

# %% [markdown]
#
# <img src="img/e-commerce.png" width="85%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# ### E-Commerce
#
# - Klassen: Unternehmen, Produkte, Kunden, Bestellungen, Positionen
# - Beziehungen:
#   - Unternehmen verkaufen Produkte
#   - Unternehmen haben Kunden und offene Bestellungen
#   - Bestellungen werden von Kunden vorgenommen
#   - Bestellungen enthalten Positionen
#   - Positionen referenzieren Produkte
# - Operationen:
#   - Kunden geben Bestellungen auf
#   - Unternehmen versenden Bestellungen

# %% [markdown]
#
# ### UML-Klassendiagramm
#
# - Domänenmodelle werden oft als UML-Klassendiagramme dargestellt
# - UML = Unified Modeling Language
# - Klassendiagramme sind nur eine von vielen UML-Diagrammarten
# - Wie man Domänenmodelle genau darstellt, ist nicht so wichtig
# - Wesentlich ist, dass alle Stakeholder das Modell verstehen

# %% [markdown]
#
# <img src="img/e-commerce-dm.png" width="65%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/act-placing-order.png" width="55%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/sq-product-selection-simple.png" width="85%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/sq-product-selection.png" width="85%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/sq-checkout-success.png" width="65%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/cars.png" width="100%">

# %% [markdown]
#
# ### Selbstfahrende Autos
#
# - Klassen: Autos, Sensoren, GPS, Karten, Fahrbahn, Route, Orte
# - Beziehungen:
#   - Autos haben Sensoren und GPS
#   - Autos haben Karten
#   - Autos fahren auf Fahrbahnen
#   - Routen verbinden Orte
# - Operationen:
#   - Autos fahren Routen
#   - Autos erkennen Fahrbahnen

# %% [markdown]
#
# <img src="img/cars-dm.png" width="70%"
#      style="margin-left: auto; margin-right: auto;">

# %% [markdown]
#
# <img src="img/bank.png" width="100%">

# %% [markdown]
#
# ### Bankenwesen
#
# - Klassen: Konten, Transaktionen, Kunden
# - Beziehungen:
#   - Kunden besitzen Konten
#   - Konten erfassen Transaktionen
# - Operationen:
#   - Kunden eröffnen Konten
#   - Kunden zahlen Geld auf Konten ein
#   - Kunden überweisen Geld von Konten

# %% [markdown]
#
# <img src="img/bank-dm.png" width="60%"
#      style="margin-left: auto; margin-right: auto;">


# %% [markdown]
#
# ## Workshop: Domänenmodelle
#
# Im Folgenden sind einige Domänen aufgeführt. Versuchen Sie, für jede Domäne
# ein (einfaches) Domänenmodell zu erstellen.
#
# Zeichnen Sie jeweils ein UML-Klassendiagramm mit den Klassen und Beziehungen.
#
# Falls Sie an einem Software-Projekt in einer bestimmten Domäne arbeiten,
# versuchen Sie, ein Domänenmodell für Ihr Projekt zu erstellen.

# %% [markdown]
#
# <img src="img/social-network.png" width="100%">

# %% [markdown]
#
# ### Soziale Netzwerke

# %% [markdown]
#
# <img src="img/medicine.png" width="100%">

# %% [markdown]
#
# ### Gesundheitswesen

# %% [markdown]
#
# <img src="img/uni.png" width="100%">

# %% [markdown]
#
# ### Bildungswesen
#
