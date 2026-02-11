"""Main application window for the JSON Menu App."""

import tkinter as tk
from tkinter import scrolledtext
from pathlib import Path

from json_menu_app.menu_config import load_menu_config, Menu, MenuItem, Separator
from json_menu_app.actions import registry as action_registry


class TextEditorApp:
    """A simple text editor with JSON-configured menus."""

    def __init__(self, config_path=None):
        self.root = tk.Tk()
        self.root.title("JSON Menu App")
        self.root.geometry("800x600")

        self.current_file = None
        self._modified = False
        self._config_path = config_path
        self._bound_shortcuts = []

        self._create_widgets()
        self._load_and_build_menus()

        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def _create_widgets(self):
        self.text = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, undo=True, font=("Consolas", 11)
        )
        self.text.pack(fill=tk.BOTH, expand=True)
        self.text.bind("<<Modified>>", self._on_text_modified)

    def _load_and_build_menus(self):
        config_path = self._config_path or self._find_config_file()
        try:
            config = load_menu_config(config_path)
            self._build_menu_bar(config.menus)
        except Exception as e:
            print(f"Error loading menu config: {e}")
            self._create_fallback_menu()

    def _find_config_file(self):
        # Look for data/menu-config.json relative to the project root.
        # When installed via pip -e, the package is in src/json_menu_app/,
        # so the project root is three levels up.
        package_dir = Path(__file__).resolve().parent
        candidates = [
            package_dir.parent.parent / "data" / "menu-config.json",
            package_dir / "data" / "menu-config.json",
            Path.cwd() / "data" / "menu-config.json",
        ]
        for path in candidates:
            if path.exists():
                return path
        return candidates[0]

    def _unbind_shortcuts(self):
        for tk_key in self._bound_shortcuts:
            self.root.unbind(tk_key)
        self._bound_shortcuts.clear()

    def _build_menu_bar(self, menus):
        self._unbind_shortcuts()
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        for menu in menus:
            tk_menu = tk.Menu(menubar, tearoff=0)
            menubar.add_cascade(label=menu.name, menu=tk_menu)

            for item in menu.items:
                if isinstance(item, Separator):
                    tk_menu.add_separator()
                elif isinstance(item, MenuItem):
                    action_name = item.action

                    def make_command(name):
                        return lambda: action_registry.handle(name, self)

                    tk_menu.add_command(
                        label=item.name,
                        command=make_command(action_name),
                        accelerator=item.shortcut or "",
                    )

                    if item.shortcut:
                        self._bind_shortcut(item.shortcut, item.action)

    def _bind_shortcut(self, shortcut, action):
        tk_key = shortcut.replace("Ctrl", "Control").replace("+", "-")
        # Lowercase single-character keys: tkinter binds <Control-n>, not <Control-N>
        parts = tk_key.rsplit("-", 1)
        if len(parts) == 2 and len(parts[1]) == 1:
            tk_key = f"{parts[0]}-{parts[1].lower()}"
        tk_key = f"<{tk_key}>"

        def handler(event):
            action_registry.handle(action, self)
            return "break"

        self.root.bind(tk_key, handler)
        self._bound_shortcuts.append(tk_key)

    def _create_fallback_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(
            label="Exit", command=lambda: action_registry.handle("exit", self)
        )

    def _on_text_modified(self, event):
        if self.text.edit_modified():
            self.set_modified(True)
            self.text.edit_modified(False)

    def _on_closing(self):
        action_registry.handle("exit", self)

    def is_modified(self):
        return self._modified

    def set_modified(self, modified):
        self._modified = modified
        self._update_title()

    def clear_edit_modified(self):
        """Clear tkinter's internal edit_modified flag after programmatic changes."""
        self.text.edit_modified(False)

    def _update_title(self):
        filename = Path(self.current_file).name if self.current_file else "Untitled"
        marker = " *" if self._modified else ""
        self.root.title(f"JSON Menu App - {filename}{marker}")

    def run(self):
        self.root.mainloop()
