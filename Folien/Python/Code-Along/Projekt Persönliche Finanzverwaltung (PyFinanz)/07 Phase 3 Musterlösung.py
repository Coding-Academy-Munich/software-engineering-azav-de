# %% [markdown]
#
# <div style="text-align:center; font-size:200%;">
#  <b>Phase 3: Musterlösung</b>
# </div>
# <br/>
# <div style="text-align:center;">Dr. Matthias Hölzl</div>
# <br/>
#
# <div style="text-align:center;">Coding-Akademie München</div>
# <br/>


# %% [markdown]
#
# # Phase 3: Musterlösung

# %% [markdown]
#
# ## `storage.py` (JSON-Funktionen)

# %% [markdown]
#
# ```python
# from __future__ import annotations
#
# import json
# from pathlib import Path
#
# from pyfinanz.account import Account
# from pyfinanz.category import Category, TransactionType
# from pyfinanz.transaction import Transaction
#
#
# def save_account_to_json(account: Account, path: Path) -> None:
#     data = {
#         "name": account.name,
#         "transactions": [
#             {
#                 "description": tx.description,
#                 "amount": tx.amount,
#                 "transaction_type": tx.transaction_type.value,
#                 "category": tx.category.value,
#                 "date": tx.date,
#                 "tags": sorted(tx.tags),
#             }
#             for tx in account.transactions
#         ],
#     }
#     path.write_text(json.dumps(data, indent=2), encoding="utf-8")
#
#
# def load_account_from_json(path: Path) -> Account:
#     data = json.loads(path.read_text(encoding="utf-8"))
#     account = Account(name=data["name"])
#     for tx_data in data["transactions"]:
#         account.add_transaction(
#             Transaction(
#                 description=tx_data["description"],
#                 amount=tx_data["amount"],
#                 transaction_type=TransactionType(tx_data["transaction_type"]),
#                 category=Category(tx_data["category"]),
#                 date=tx_data["date"],
#                 tags=frozenset(tx_data.get("tags", [])),
#             )
#         )
#     return account
# ```
