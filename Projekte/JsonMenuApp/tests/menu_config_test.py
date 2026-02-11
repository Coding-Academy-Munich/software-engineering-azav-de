"""Tests for menu configuration loading and serialization."""

import json

import pytest

from json_menu_app.menu_config import (
    Menu,
    MenuConfig,
    MenuItem,
    Separator,
    load_menu_config,
    menu_object_hook,
    menu_serializer,
    save_menu_config,
)


class TestMenuItem:
    def test_creation_with_shortcut(self):
        item = MenuItem("New", "new_file", "Ctrl+N")
        assert item.name == "New"
        assert item.action == "new_file"
        assert item.shortcut == "Ctrl+N"

    def test_creation_without_shortcut(self):
        item = MenuItem("About", "about")
        assert item.shortcut is None

    def test_repr_with_shortcut(self):
        item = MenuItem("New", "new_file", "Ctrl+N")
        assert repr(item) == "MenuItem('New', 'new_file', 'Ctrl+N')"

    def test_repr_without_shortcut(self):
        item = MenuItem("About", "about")
        assert repr(item) == "MenuItem('About', 'about')"

    def test_equality(self):
        a = MenuItem("New", "new_file", "Ctrl+N")
        b = MenuItem("New", "new_file", "Ctrl+N")
        assert a == b

    def test_inequality(self):
        a = MenuItem("New", "new_file", "Ctrl+N")
        b = MenuItem("Open", "open_file", "Ctrl+O")
        assert a != b


class TestSeparator:
    def test_repr(self):
        assert repr(Separator()) == "Separator()"

    def test_equality(self):
        assert Separator() == Separator()


class TestMenu:
    def test_creation(self):
        items = [MenuItem("New", "new_file"), Separator(), MenuItem("Exit", "exit")]
        menu = Menu("File", items)
        assert menu.name == "File"
        assert len(menu.items) == 3

    def test_equality(self):
        items = [MenuItem("Exit", "exit")]
        assert Menu("File", items) == Menu("File", items)


class TestMenuConfig:
    def test_creation(self):
        menus = [
            Menu("File", [MenuItem("Exit", "exit")]),
            Menu("Help", [MenuItem("About", "about")]),
        ]
        config = MenuConfig(menus)
        assert len(config.menus) == 2


class TestObjectHook:
    def test_menuitem(self):
        d = {"_type": "menuitem", "name": "New", "action": "new_file", "shortcut": "Ctrl+N"}
        result = menu_object_hook(d)
        assert isinstance(result, MenuItem)
        assert result == MenuItem("New", "new_file", "Ctrl+N")

    def test_menuitem_without_shortcut(self):
        d = {"_type": "menuitem", "name": "About", "action": "about"}
        result = menu_object_hook(d)
        assert result.shortcut is None

    def test_separator(self):
        d = {"_type": "separator"}
        result = menu_object_hook(d)
        assert isinstance(result, Separator)

    def test_menu_with_preparsed_items(self):
        items = [MenuItem("New", "new_file"), Separator()]
        d = {"_type": "menu", "name": "File", "items": items}
        result = menu_object_hook(d)
        assert isinstance(result, Menu)
        assert result.name == "File"
        assert len(result.items) == 2

    def test_unknown_type_passthrough(self):
        d = {"_type": "unknown", "foo": "bar"}
        assert menu_object_hook(d) == d

    def test_no_type_passthrough(self):
        d = {"foo": "bar"}
        assert menu_object_hook(d) == d


class TestSerializer:
    def test_menuitem_with_shortcut(self):
        result = menu_serializer(MenuItem("New", "new_file", "Ctrl+N"))
        assert result == {
            "_type": "menuitem",
            "name": "New",
            "action": "new_file",
            "shortcut": "Ctrl+N",
        }

    def test_menuitem_without_shortcut(self):
        result = menu_serializer(MenuItem("About", "about"))
        assert result == {"_type": "menuitem", "name": "About", "action": "about"}
        assert "shortcut" not in result

    def test_separator(self):
        assert menu_serializer(Separator()) == {"_type": "separator"}

    def test_menu(self):
        menu = Menu("File", [MenuItem("Exit", "exit")])
        result = menu_serializer(menu)
        assert result["_type"] == "menu"
        assert result["name"] == "File"

    def test_unsupported_type_raises(self):
        with pytest.raises(TypeError):
            menu_serializer(42)


class TestRoundTrip:
    def test_full_round_trip(self):
        original = MenuConfig(
            [
                Menu(
                    "File",
                    [
                        MenuItem("New", "new_file", "Ctrl+N"),
                        MenuItem("Open", "open_file", "Ctrl+O"),
                        Separator(),
                        MenuItem("Exit", "exit"),
                    ],
                ),
                Menu("Help", [MenuItem("About", "about")]),
            ]
        )
        json_str = json.dumps(original, default=menu_serializer, indent=2)
        data = json.loads(json_str, object_hook=menu_object_hook)
        result = MenuConfig(data["menus"])
        assert result == original


class TestFileIO:
    def test_load_menu_config(self, tmp_path):
        config_data = {
            "menus": [
                {
                    "_type": "menu",
                    "name": "File",
                    "items": [{"_type": "menuitem", "name": "Exit", "action": "exit"}],
                }
            ]
        }
        config_file = tmp_path / "test-config.json"
        config_file.write_text(json.dumps(config_data), encoding="utf-8")

        config = load_menu_config(config_file)
        assert isinstance(config, MenuConfig)
        assert len(config.menus) == 1
        assert config.menus[0].name == "File"
        assert isinstance(config.menus[0].items[0], MenuItem)

    def test_save_menu_config(self, tmp_path):
        config = MenuConfig([Menu("File", [MenuItem("Exit", "exit")])])
        config_file = tmp_path / "test-config.json"
        save_menu_config(config, config_file)

        assert config_file.exists()
        with open(config_file, encoding="utf-8") as f:
            data = json.load(f)
        assert "menus" in data
        assert data["menus"][0]["name"] == "File"

    def test_save_and_load_round_trip(self, tmp_path):
        original = MenuConfig(
            [
                Menu(
                    "Edit",
                    [
                        MenuItem("Cut", "cut", "Ctrl+X"),
                        Separator(),
                        MenuItem("Paste", "paste", "Ctrl+V"),
                    ],
                )
            ]
        )
        config_file = tmp_path / "round-trip.json"
        save_menu_config(original, config_file)
        loaded = load_menu_config(config_file)
        assert loaded == original
