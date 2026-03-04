# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Beliebig viele Funktionsargumente</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# Requires lists and dicts

# %% [markdown]
# ## Beliebig viele Funktionsargumente:
#
# Man kann Funktionen definieren, die beliebig viele Argumente bekommen können:

# %%

# %%

# %% [markdown]
#
# ## Mini-Workshop
#
# Schreiben Sie eine Funktion `print_lines(*args)`, die beliebig viele
# Argumente bekommt und ein Argument pro Zeile ausgibt:
# ```
# >>> print_lines("hey", "you")
# hey
# you
# ```

# %%

# %%

# %% [markdown]
# Das kann auch mit anderen Argumenten kombiniert werden:

# %%

# %%

# %%

# %%

# %% [markdown]
# ## Beliebig viele benannte Argumente:
#
# Ebenso kann eine Funktion beliebig viele benannte Argumente haben:

# %%

# %%

# %% [markdown]
# Es ist möglich diese beiden Features zu kombinieren:

# %%

# %%


# %% [markdown]
#
# ## Mini-Workshop
#
# Schreiben Sie eine Funktion `print_named_lines(**kwargs)`, die beliebig viele
# Keyword-Argumente bekommt und sie in folgender Form auf dem Bildschirm
# ausgibt:
# ```python
# >>> print_named_lines(foo="My Foo", bar="My Bar", quux="My Quux")
# Key: foo -- value: My Foo
# Key: bar -- value: My Bar
# Key: quux -- value: My Quux
# ```


# %%

# %%
print_named_lines(foo="My Foo", bar="My Bar", quux="My Quux")

# %% [markdown]
# ## "Splicing" von Argumenten
#
# - Wenn man eine Liste `args` hat, kann man die darin enthaltenen Werte mit
#   der Syntax `*args` als positionale Argumente übergeben.
# - Wenn man ein Dictionary `kwargs` hat, kann man die Key/Value-Paare mit der
#   Syntax `**kwargs` als benannte Argumente übergeben:

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
