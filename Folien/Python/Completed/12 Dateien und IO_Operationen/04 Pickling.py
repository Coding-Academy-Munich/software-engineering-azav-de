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
import pickle
from pprint import pprint

# %%
my_list = [1, 2, 3, 4]
my_other_list = [3, 4, 5]
my_dict = {1: my_list, 2: my_other_list, 3: "a string", 4: ["some list"]}


# %%
pprint(my_dict)


# %%
my_pickle = pickle.dumps(my_dict)
pprint(my_pickle)

# %%
restored_pickle = pickle.loads(my_pickle)

# %%
pprint(restored_pickle)

# %%
my_dict == restored_pickle

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
