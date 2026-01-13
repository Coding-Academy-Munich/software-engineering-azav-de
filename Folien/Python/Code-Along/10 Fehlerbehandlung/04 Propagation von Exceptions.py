# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Propagation von Exceptions</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# # Stack-Unwinding
#
# Wenn eine Exception ausgelöst wird, werden geschachtelte Funktionsaufrufe so lange
# abgebrochen, bis ein passender Handler gefunden wird:

# %%
def function_1():
    local_var_1 = 10
    local_var_2 = 20
    function_2()
    print("function_1(): done")

# %%
def function_2():
    try:
        local_var_1 = 5
        local_var_2 = 10
        local_var_3 = 15
        function_3()
        print("function_2(): done")
    except Exception:
        print("function_2(): caught Exception")

# %%
def function_3():
    local_var_1 = 2
    function_4()
    print("function_3(): done")


# %%
def function_4():
    local_var_1 = 4
    raise ValueError("Raising ValueError")
    print("function_4(): done")

# %%
function_1()


# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01a.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01b.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01c.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01d.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-01e.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-02.png" alt="Call Stack"
#      style="float: left; width: 37.3%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-03.png" alt="Call Stack"
#      style="float: left; width: 37.3%; margin-left: 10%;"/>

# %% [markdown]
#
# <img src="img/stack-code.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%; margin-top: 3%;"/>
#
# <img src="img/stack-04.png" alt="Call Stack"
#      style="float: left; width: 30%; margin-left: 10%;"/>


# %%
from typing import Callable


# %% [markdown]
#
# - Der Typ `Callable` kann z.B. verwendet werden, um auszudrücken, dass wir
#   eine Funktion als Argument übergeben wollen.
# - Das kann auch eine Konstruktorfunktion sein, wie z.B. `list` oder
#   `ValueError`.

# %%

# %%

# %%

# %%

# %%

# %%

# %% [markdown]
#
# - Wir haben schon gesehen, dass Exceptions eine Hierarchie bilden:
#   ```
#   BaseException
#    └── Exception
#         ├── ArithmeticError
#         ├── LookupError
#         │    ├── IndexError
#         │    └── KeyError
#         ├── TypeError
#         └── ValueError
#   ```
# - Mit `issubclass()` können wir das überprüfen.

# %%

# %%

# %%

# %%

# %%
def outer_caller_v0(error_type: Callable = ValueError):
    intermediate_fun_v0(error_type)


# %%
def intermediate_fun_v0(error_type: Callable):
    try:
        raise_and_handle_error_v0(error_type)
    except:
        raise


# %%
def raise_and_handle_error_v0(error_type: Callable):
    try:
        raise error_type(f"Raising {error_type.__name__}")
    except LookupError:
        pass

# %%
# outer_caller_v0(ValueError)

# %%

# %%
def outer_caller(error_type: Callable = ValueError):
    print("outer_caller(): before calling")
    intermediate_fun(error_type)
    print("outer_caller(): after calling")


# %%
def intermediate_fun(error_type: Callable):
    print("  intermediate_fun(): before try")
    try:
        print("  intermediate_fun(): before calling")
        raise_and_handle_error(error_type)
        print("  intermediate_fun(): after calling")
    except:
        raise
    print("  intermediate_fun(): after except")


# %%
def raise_and_handle_error(error_type: Callable):
    print("    raise_and_handle_error(): before try")
    try:
        print("    raise_and_handle_error(): before raise")
        raise error_type(f"Raising {error_type.__name__}")
        print("    raise_and_handle_error(): after raise")  # noqa
    except LookupError as error:
        print(f"<<< raise_and_handle_error(): caught LookupError [{error}]")
    print("    raise_and_handle_error(): after except")


# %%
outer_caller(LookupError)

# %%
outer_caller(IndexError)

# %%
# outer_caller(ValueError)


# %%
def outer_caller_with_try(error_type: Callable = ValueError):
    print("outer_caller(): before try")
    try:
        print("outer_caller(): before calling")
        intermediate_fun(error_type)
        print("outer_caller(): after calling")
    except Exception as error:
        print(f"<<< outer_caller(): caught Exception: {error}")
    print("outer_caller(): after except")


# %%
outer_caller_with_try(IndexError)


# %%


# %% [markdown]
#
# ## Workshop: Verschachtelte Ausnahmen
#
# In diesem Workshop wollen wir betrachten, wie sich verschachtelte Ausnahmen
# verhalten.
#
# Gegeben seien die folgenden Funktionen.
#
# Welche Ausgabe erwarten Sie für Aufrufe von `outer_caller_ws()` und
# `outer_caller_with_try_ws()` mit den verschiedenen `Type`-Werten?

# %%
def raise_and_handle_error_ws(exception_type: Callable):
    print("    raise_and_handle_error_ws(): before try")
    try:
        print("    raise_and_handle_error_ws(): before raise")
        raise exception_type(f"Raising {exception_type.__name__}")
    except LookupError as error:
        print(f"<<< raise_and_handle_error_ws(): caught LookupError [{error}]")
        raise
    except ValueError as error:
        print(f"<<< raise_and_handle_error_ws(): caught ValueError [{error}]")
    print("    raise_and_handle_error_ws(): after except")


# %%
def intermediate_fun_ws(exception_type: Callable):
    print("  intermediate_fun_ws(): before call")
    try:
        raise_and_handle_error_ws(exception_type)
    except IndexError as error:
        print(f"<<< intermediate_fun_ws(): caught IndexError [{error}]")
        # This causes Python to report that the IndexError is the
        # "direct cause of" the TypeError
        raise TypeError(f"Raising inner TypeError from [{error}]") from error
    except LookupError as error:
        print(f"<<< intermediate_fun_ws(): caught LookupError [{error}]")
        # This causes Python to report that during handling of LookupError
        # "another exception occurred"
        raise TypeError("Raising inner TypeError")
    except Exception as error:
        print(f"<<< intermediate_fun_ws(): caught Exception [{error}]")
        print("  intermediate_fun_ws(): re-raising exception")
        # This causes Python to act as if the exception had never been caught
        raise
        print("  intermediate_fun_ws(): re-raised exception")  # noqa
    print("  intermediate_fun_ws() after call")


# %%
def outer_caller_ws(exception_type: Callable = ValueError):
    print("outer_caller_ws(): before calling")
    intermediate_fun_ws(exception_type)
    print("outer_caller_ws(): after calling")


# %%
outer_caller_ws(ValueError)

# %%
# outer_caller_ws(LookupError)

# %%
# outer_caller_ws(IndexError)

# %%


# %%

# %%
outer_caller_with_try_ws(ValueError)

# %%
outer_caller_with_try_ws(LookupError)

# %%
outer_caller_with_try_ws(IndexError)
