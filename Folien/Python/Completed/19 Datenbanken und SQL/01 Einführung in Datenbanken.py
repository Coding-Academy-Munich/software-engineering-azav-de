# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Einführung in Datenbanken</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Was ist eine Datenbank?
#
# - Sammlung von Daten
#   - Effiziente zum Speichern, Abrufen und Manipulieren von großen Datenmengen
# - Die Software, die eine Datenbank verwaltet, wird als Datenbanksystem (Data
#   Base Management System, DBMS) bezeichnet
# - Eine Datenbank ist eine Sammlung von Daten, die in einem DBMS organisiert
#   und gespeichert ist
# - Oft sagt man aber auch einfach "Datenbank" für das DBMS

# %% [markdown]
#
# ## Beispiele für Datenbanken:
#
# - Telefonbuch
# - Bibliothekskatalog
# - Online-Einkaufsseite (Backend)
# - ...

# %% [markdown]
#
# ## Merkmale einer Datenbank
#
# - Konsistente und genaue Datenspeicherung
# - Effiziente Datenabfrage und -manipulation
# - Einfache gemeinsame Nutzung von Daten zwischen Anwendungen
# - Datensicherheit und Zugriffskontrolle
# - Skalierbarkeit und Flexibilität

# %% [markdown]
#
# ##  Arten von Datenbanken:
#
# Verschiedene Arten von Datenbanken bieten unterschiedliche Kompromisse
# zwischen diesen Merkmalen
#
# - **Relationale Datenbanken**
# - NoSQL-Datenbanken
#   - Graph-Datenbanken
#   - Objektorientierte Datenbanken
#   - Dokumentorientierte Datenbanken

# %% [markdown]
#
# ## Relationale Datenbanken:
#
# <img src="img/relational-db-01.png"
#      style="width:100%;margin:auto" alt="Relationale Datenbank"></img>

# %% [markdown]
#
# ### Relationale Datenbanken
#
# - Verwenden eine tabellenbasierte Struktur zum Speichern von Daten
# - Daten werden in Zeilen und Spalten organisiert
#   - Spalten sind Attribute
#   - Zeilen sind Datensätze
# - Beziehungen zwischen Tabellen werden durch Primär- und Fremdschlüssel hergestellt
# - Beispiele sind MySQL, PostgreSQL und Oracle Database


# %% [markdown]
#
# ### NoSQL-Datenbanken:
#
# Dies ist eine allgemeine Kategorie, die auch andere umfasst, wie z.B. graph-
# oder dokumentenorientierte Datenbanken.
#
# - Entwickelt für unstrukturierte Daten und nicht-relationale Datenmodelle
# - Sie verwenden oft keine Tabellen und kein festes Schema
#   - Es gibt aber auch NoSQL Datenbanken mit festem Schema
# - Daten werden als Schlüssel-Wert-Paare, JSON oder in anderen Formaten
#   gespeichert
# - Beispiele sind MongoDB, Couchbase und Cassandra

# %% [markdown]
#
# ### Graph-Datenbanken
#
# <img src="img/graph-db-01.png"
#      style="width:70%;margin:auto" alt="Graph Datenbank"></img>

# %% [markdown]
#
# ### Graph-Datenbanken
#
# - Entwickelt, um komplexe Beziehungen zwischen Datenpunkten darzustellen.
# - Daten werden als Knoten, Kanten und Eigenschaften gespeichert
# - Das Durchlaufen des Graphen ermöglicht komplexe Abfragen und Analysen
# - Beispiele sind Neo4j und OrientDB

# %% [markdown]
#
# ### Objektorientierte Datenbanken
#
# - Entwickelt, um Objekte, Klassen und Methoden zu speichern.
# - Daten werden als Objekte mit Attributen und Verhaltensweisen
#   gespeichert
# - Sie unterstützen Vererbung und Polymorphismus
# - Beispiele sind db4o und ObjectDB

# %% [markdown]
#
# ### Dokumentorientierte Datenbanken
#
# - Entwickelt für die Speicherung und Verwaltung von Dokumenten
# - Daten werden als JSON, XML oder in anderen Formaten gespeichert
# - Flexibles Schema, das sich ändern kann, wenn sich die Daten ändern
# - Beispiele sind MongoDB, CouchDB und RavenDB
