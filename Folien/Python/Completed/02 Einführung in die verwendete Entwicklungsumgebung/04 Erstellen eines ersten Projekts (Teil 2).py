# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Erstellen eines ersten Projekts (Teil 2)</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Zeichnen einer Spirale
#
# - Als eine etwas interessanteres Beispiel wollen wir eine bunte Spirale zeichnen

# %% [markdown]
#
# ```python
# import turtle
# import random
# import math
#
# # Set up the window
# window = turtle.Screen()
# window.bgcolor("black")
#
# # Create a turtle object
# t = turtle.Turtle()
# t.speed(10)  # Speed up the turtle
# t.pensize(2)  # Slightly thicker line
#
# # Create a colorful spiral
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# size = 10
#
# # Now draw the actual spiral
# t.speed(10)
# size = 10
# for i in range(60):
#     # Change color every few steps
#     t.color(colors[i % len(colors)])
#
#     # Draw a line and turn
#     t.forward(size)
#     t.right(45)
#
#     # Increase the line length each time
#     size += 3
#
# # Hide the turtle when finished
# t.hideturtle()
#
# # Keep the window open until it's clicked
# turtle.done()
# ```

# %% [markdown]
#
# ## Zeichnen von Sternen im Hintergrund
#
# - Wir wollen nun Sterne im Hintergrund zeichnen
# - Die Sterne sollen zufällig verteilt sein und unterschiedliche Größen haben
# - Sie sollen außerhalb der Spirale liegen
# - Wir verwenden dazu die `random` Bibliothek
# - Aufgrund des Workshops wissen wir bereits, wie wir Sterne zeichnen können
#
# Pasten Sie den folgenden Code in das Programm (vor der Zeile `t.hideturtle()`):


# %% [markdown]
#
# ```python
# # The approximate radius of the spiral
# spiral_radius = 300
#
# t.penup()
# t.speed(0)  # Fastest speed
#
# for _ in range(250):
#     # Generate coordinates outside the spiral area
#     for _ in range(1000):
#         x = random.randint(-500, 500)
#         y = random.randint(-500, 500)
#
#         # Calculate distance from origin
#         distance = math.sqrt(x*x + y*y)
#
#         # Check if outside the spiral area
#         if distance > spiral_radius:
#             break
#
#     t.goto(x, y)
#     t.pendown()
#
#     # Use a random color from the list
#     t.color(random.choice(colors))
#
#     # Draw stars with random sizes
#     size = random.randint(15, 30)
#     t.setheading(0)  # Reset the direction
#     for _ in range(5):
#         t.forward(size)
#         t.right(144)
#
#     t.penup()
# ```

# %% [markdown]
#
# ## Workshop: Zeichnen eines bunten Sterns
#
# - Schreiben Sie ein Python Programm, das einen bunten Stern zeichnet
# - Der Stern soll aus 5 Linien bestehen, die in unterschiedlichen Farben
#   gezeichnet werden
# - Dabei können Sie das Programm aus dem vorherigen Workshop verwenden

# %% [markdown]
#
# ```python
# import turtle
# import random
#
# # Set up the window
# window = turtle.Screen()
# window.bgcolor("black")
#
# # Create a turtle object
# t = turtle.Turtle()
#
# # Set pen color
# colors = ["red", "orange", "yellow", "blue", "purple", "green"]
#
# # Set the turtle's speed
# t.speed(1)
#
# # Set the drawing pen's size
# t.pensize(5)
#
# # Draw a simple square
# for i in range(5):
#     # t.color(random.choice(colors))  # Random color
#     t.color(colors[i % len(colors)])  # Fixed sequence of colors
#     t.forward(200)  # Move forward 100 pixels
#     t.right(144)     # Turn right 144 degrees
#
# # Keep the window open until it's clicked
# turtle.done()
# ````
