"""Menu configuration classes and JSON loading.

Demonstrates the JSON serialization patterns from the course:
- Custom classes with JSON serialization
- Using _type field for type discrimination
- object_hook for bottom-up deserialization
- Nested object structures (Menus contain MenuItems)
"""

import json
from pathlib import Path


class MenuItem:
    """A menu item with a name, action, and optional keyboard shortcut.

    >>> item = MenuItem("New", "new_file", "Ctrl+N")
    >>> item.name
    'New'
    >>> item.action
    'new_file'
    >>> item.shortcut
    'Ctrl+N'
    """

    def __init__(self, name, action, shortcut=None):
        self.name = name
        self.action = action
        self.shortcut = shortcut

    def __repr__(self):
        if self.shortcut:
            return f"MenuItem({self.name!r}, {self.action!r}, {self.shortcut!r})"
        return f"MenuItem({self.name!r}, {self.action!r})"

    def __eq__(self, other):
        if not isinstance(other, MenuItem):
            return NotImplemented
        return (
            self.name == other.name
            and self.action == other.action
            and self.shortcut == other.shortcut
        )


class Separator:
    """A visual separator between menu items.

    >>> Separator()
    Separator()
    """

    def __repr__(self):
        return "Separator()"

    def __eq__(self, other):
        if not isinstance(other, Separator):
            return NotImplemented
        return True


class Menu:
    """A top-level menu containing items (MenuItems or Separators).

    >>> menu = Menu("File", [MenuItem("Exit", "exit")])
    >>> menu.name
    'File'
    >>> len(menu.items)
    1
    """

    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __repr__(self):
        return f"Menu({self.name!r}, {self.items!r})"

    def __eq__(self, other):
        if not isinstance(other, Menu):
            return NotImplemented
        return self.name == other.name and self.items == other.items


class MenuConfig:
    """Root configuration containing all menus.

    >>> config = MenuConfig([Menu("File", [MenuItem("Exit", "exit")])])
    >>> len(config.menus)
    1
    """

    def __init__(self, menus):
        self.menus = menus

    def __repr__(self):
        return f"MenuConfig({self.menus!r})"

    def __eq__(self, other):
        if not isinstance(other, MenuConfig):
            return NotImplemented
        return self.menus == other.menus


def menu_object_hook(d):
    """Object hook for deserializing menu JSON.

    Called for every JSON object (dict) during parsing, bottom-up.
    Nested objects are deserialized before their containers, so
    Menu items are already MenuItem/Separator objects when the
    Menu dict is processed.

    >>> menu_object_hook({"_type": "menuitem", "name": "X", "action": "x"})
    MenuItem('X', 'x')
    >>> menu_object_hook({"_type": "separator"})
    Separator()
    >>> menu_object_hook({"foo": "bar"})
    {'foo': 'bar'}
    """
    type_val = d.get("_type")
    if type_val == "menuitem":
        return MenuItem(d["name"], d["action"], d.get("shortcut"))
    if type_val == "separator":
        return Separator()
    if type_val == "menu":
        return Menu(d["name"], d["items"])
    return d


def menu_serializer(obj):
    """Default serializer for menu objects.

    >>> menu_serializer(MenuItem("X", "x", "Ctrl+X"))
    {'_type': 'menuitem', 'name': 'X', 'action': 'x', 'shortcut': 'Ctrl+X'}
    >>> menu_serializer(Separator())
    {'_type': 'separator'}
    """
    if isinstance(obj, Menu):
        return {"_type": "menu", "name": obj.name, "items": obj.items}
    if isinstance(obj, MenuItem):
        result = {"_type": "menuitem", "name": obj.name, "action": obj.action}
        if obj.shortcut:
            result["shortcut"] = obj.shortcut
        return result
    if isinstance(obj, Separator):
        return {"_type": "separator"}
    if isinstance(obj, MenuConfig):
        return {"menus": obj.menus}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def load_menu_config(file_path):
    """Load menu configuration from a JSON file.

    Args:
        file_path: Path to menu-config.json

    Returns:
        MenuConfig with parsed menus
    """
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f, object_hook=menu_object_hook)
    return MenuConfig(data["menus"])


def save_menu_config(config, file_path):
    """Save menu configuration to a JSON file.

    Args:
        config: MenuConfig to save
        file_path: Output path
    """
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(
            {"menus": config.menus},
            f,
            default=menu_serializer,
            indent=2,
            ensure_ascii=False,
        )
