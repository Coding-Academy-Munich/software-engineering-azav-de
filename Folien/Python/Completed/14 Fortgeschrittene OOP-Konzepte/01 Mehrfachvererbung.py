# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Mehrfachvererbung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
# # Mehrfachvererbung


# %%
class A:
    """Superclass of everything"""

    def __init__(self, arg_a="arg_a", **kwargs):
        super().__init__(**kwargs)
        print(f"__init__(A, {arg_a})")

    def f(self):
        print(f"f(A) on {self!r}")

    def g(self):
        print(f"g(A) on {self!r}")


# %%
class B(A):
    def __init__(self, arg_b="arg_b", **kwargs):
        super().__init__(**kwargs)
        print(f"__init__(B, {arg_b})")

    def f(self):
        print(f"f(B) on {self!r}")
        super().f()

    def g(self):
        print(f"g(B) on {self!r}")
        A.g(self)


# %%
class C(A):
    def __init__(self, arg_c="arg_c", **kwargs):
        super().__init__(**kwargs)
        print(f"__init__(C, {arg_c})")

    def f(self):
        print(f"f(C) on {self!r}")
        super().f()

    def g(self):
        print(f"g(C) on {self!r}")
        A.g(self)


# %%
class D(B, C):
    def __init__(self, arg_d="arg_d", **kwargs):
        super().__init__(**kwargs)
        print(f"__init__(D, {arg_d})")

    def f(self):
        print(f"f(D) on {self!r}")
        super().f()

    def g(self):
        print(f"g(D) on {self!r}")
        B.g(self)
        C.g(self)


# %%
d = D()
d.f()

# %%
d.g()

# %%
type(d).mro()
