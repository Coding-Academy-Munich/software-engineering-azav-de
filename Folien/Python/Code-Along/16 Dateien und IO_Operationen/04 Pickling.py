# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Pickling</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>

# %% [markdown]
#
# ## Pickles
#
# Das `pickle` Modul bietet die Möglichkeit, Python Objekte einfach zu speichern
# und zu laden.

# %%

# %%


# %%


# %%

# %%

# %%

# %%

# %%
my_dict is restored_pickle

# %%
my_list.append(my_other_list)
my_other_list.append(my_list)

# %%
pprint(my_list)


# %%
pprint(my_dict)

# %%
my_pickle = pickle.dumps(my_dict)
restored_pickle = pickle.loads(my_pickle)

# %%
pprint(restored_pickle)

# %%
# Don't try this...
# my_dict == restored_pickle
