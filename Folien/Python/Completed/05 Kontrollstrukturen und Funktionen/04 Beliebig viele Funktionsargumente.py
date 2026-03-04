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
def my_add(*args):
    result = 0
    for i in args:
        result += i
    return result


# %%
my_add(1, 2, 3, 4, 5, 6)


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
def print_lines(*args):
    for arg in args:
        print(arg)


# %%
print_lines("hey", "you")


# %% [markdown]
# Das kann auch mit anderen Argumenten kombiniert werden:

# %%
def add_more_than_two(x, y, *more_args):
    result = x + y
    for i in more_args:
        result += i
    return result


# %%
add_more_than_two(1, 2, 3, 4, 5, 6)

# %%
add_more_than_two(1, 2)


# %%
# add_more_than_two(1)

# %% [markdown]
# ## Beliebig viele benannte Argumente:
#
# Ebenso kann eine Funktion beliebig viele benannte Argumente haben:

# %%
def my_keys(**kwargs):
    print("Keyword arguments:", kwargs)


# %%
my_keys(x=1, y=2)


# %% [markdown]
# Es ist möglich diese beiden Features zu kombinieren:

# %%
def takes_arbitrary_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:    ", kwargs)


# %%
takes_arbitrary_args(1, "foo", a="alpha", b="beta")


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
def print_named_lines(**kwargs):
    for k, v in kwargs.items():
        print("Key:", k, "-- value:", v)


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
def add(x, y):
    return x + y


# %%
my_list = [3, 4]

# %%
# add(my_list)

# %%
add(my_list[0], my_list[1])

# %%
add(*my_list)

# %%
my_dict = {"a": "alpha", "b": "beta"}

# %%
takes_arbitrary_args(my_list, my_dict)

# %%
takes_arbitrary_args(*my_list, **my_dict)

# %%
takes_arbitrary_args(3, 4, a="alpha", b="beta")
