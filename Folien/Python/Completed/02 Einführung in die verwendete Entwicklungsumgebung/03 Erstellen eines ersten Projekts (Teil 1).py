# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Erstellen eines ersten Projekts (Teil 1)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Zeichnen von geometrischen Formen
#
# - `turtle` Modul ermöglicht das Zeichnen von geometrischen Formen
# - "Schildkröte" bewegt sich auf einer Zeichenfläche
# - Zeichnet dabei eine Linie
# - Befehle steuern die Bewegung der Schildkröte

# %% [markdown]
#
# # Erstellung eines ersten Projekts
#
# <br>
# <div style="overflow:auto;">
#     <img src="img/rectangle.png" style="width:15%;float:right;margin-left:10px;"/>
#     <ul style="margin:0; padding-left:20px;">
#         <li>Programm zum Zeichnen eines Quadrats</code></li>
#         <li>Anlegen eines Verzeichnisses für das Projekt</li>
#         <li>Erstellen einer Python-Datei<br>(Text-Datei mit der Endung <code>.py</code>)</li>
#         <li>Schreiben des Programmcodes</li>
#         <li>Ausführen des Programms</li>
#     </ul>
# </div>

# %% [markdown]
#
# <div style="overflow:auto;">
#     <img src="img/rectangle.png" style="width:15%;float:right;margin-left:10px;"/>
#     <ul style="margin:0; padding-left:20px;">
#         <li>Anlegen eines Verzeichnisses <code>TurtleDrawings</code></li>
#         <li>Erstellen einer Datei <code>square.py</code></li>
#         <li>Schreiben des Programmcodes (siehe nächste Folie)</li>
#         <li>Ausführen des Programms mit VS Code</li>
#     </ul>
# </div>

# %% [markdown]
#
# ## Programmcode

# %% [markdown]
#
# ```python
# # import turtle
#
# # Create a turtle object
# t = turtle.Turtle()
#
# # Set pen color
# t.color("blue")
#
# # Set the turtle's speed
# t.speed(1)
#
# # Set the drawing pen's size
# t.pensize(5)
#
# # Draw a simple square
# for i in range(4):
#     t.forward(200)  # Move forward 100 pixels
#     t.right(90)     # Turn right 90 degrees
#
# # Keep the window open until it's clicked
# turtle.done()
# ````

# %% [markdown]
#
# ## Workshop: Zeichnen eines Sterns
#
# <div style="overflow:auto;">
#     <img src="img/star.png" style="width:20%;float:right;margin-left:10px;"/>
#     <p>Schreiben Sie ein Python Programm, das einen Stern zeichnet
#     <ul style="margin:0; padding-left:20px;">
#         <li>Verwenden Sie die <code>turtle</code> Bibliothek</li>
#         <li>Der Stern soll 5 Zacken haben und rot sein</li>
#         <li>Dazu müssen Sie die Schildkröte 5 mal nach rechts drehen</li>
#         <li>Jede Drehung beträgt 144 Grad</li>
#         <li>Die Länge der Linien soll 200 Pixel betragen</li>
#     </ul>
# </div>

# %% [markdown]
#
# ```python
# import turtle
#
# # Create a turtle object
# t = turtle.Turtle()
#
# # Set pen color
# t.color("red")
#
# # Set the turtle's speed
# t.speed(1)
#
# # Set the drawing pen's size
# t.pensize(5)
#
# # Draw a simple square
# for i in range(5):
#     t.forward(200)  # Move forward 100 pixels
#     t.right(144)     # Turn right 144 degrees
#
# # Keep the window open until it's clicked
# turtle.done()
# ```
