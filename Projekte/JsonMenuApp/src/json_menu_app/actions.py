"""Action handler registry and implementations for the text editor."""

from tkinter import messagebox, filedialog

from json_menu_app.menu_config import load_menu_config


class ActionRegistry:
    """Registry mapping action names to handler functions.

    Each handler receives the app instance so it can access
    the text widget and other application state.
    """

    def __init__(self):
        self._handlers = {}

    def register(self, name, handler):
        self._handlers[name] = handler

    def get(self, name):
        return self._handlers.get(name)

    def handle(self, name, app):
        handler = self.get(name)
        if handler:
            handler(app)


registry = ActionRegistry()


def new_file(app):
    if app.is_modified():
        response = messagebox.askyesnocancel(
            "Save Changes?",
            "Do you want to save changes before creating a new file?",
        )
        if response is None:
            return
        if response:
            save_file(app)
    app.text.delete("1.0", "end")
    app.current_file = None
    app.clear_edit_modified()
    app.set_modified(False)


def open_file(app):
    if app.is_modified():
        response = messagebox.askyesnocancel(
            "Save Changes?",
            "Do you want to save changes before opening a file?",
        )
        if response is None:
            return
        if response:
            save_file(app)
    filename = filedialog.askopenfilename(
        title="Open File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if filename:
        try:
            with open(filename, encoding="utf-8") as f:
                content = f.read()
            app.text.delete("1.0", "end")
            app.text.insert("1.0", content)
            app.current_file = filename
            app.clear_edit_modified()
            app.set_modified(False)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file:\n{e}")


def save_file(app):
    if app.current_file:
        try:
            content = app.text.get("1.0", "end-1c")
            with open(app.current_file, "w", encoding="utf-8") as f:
                f.write(content)
            app.set_modified(False)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
    else:
        save_as_file(app)


def save_as_file(app):
    filename = filedialog.asksaveasfilename(
        title="Save As",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if filename:
        try:
            content = app.text.get("1.0", "end-1c")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            app.current_file = filename
            app.set_modified(False)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")


def exit_app(app):
    if app.is_modified():
        response = messagebox.askyesnocancel(
            "Save Changes?",
            "Do you want to save changes before exiting?",
        )
        if response is None:
            return
        if response:
            save_file(app)
    app.root.quit()


def cut(app):
    try:
        app.text.event_generate("<<Cut>>")
    except Exception:
        pass


def copy(app):
    try:
        app.text.event_generate("<<Copy>>")
    except Exception:
        pass


def paste(app):
    try:
        app.text.event_generate("<<Paste>>")
    except Exception:
        pass


def select_all(app):
    app.text.tag_add("sel", "1.0", "end")
    app.text.mark_set("insert", "1.0")
    app.text.see("insert")


def about(app):
    messagebox.showinfo(
        "About JSON Menu App",
        "JSON Menu App v0.1.0\n\n"
        "A simple text editor demonstrating\n"
        "JSON-based menu configuration.\n\n"
        "Part of the Python Programming Course",
    )


def load_menu_layout(app):
    filename = filedialog.askopenfilename(
        title="Load Menu Layout",
        filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")],
    )
    if filename:
        try:
            config = load_menu_config(filename)
            app._build_menu_bar(config.menus)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load menu layout:\n{e}")


registry.register("new_file", new_file)
registry.register("open_file", open_file)
registry.register("save_file", save_file)
registry.register("save_as_file", save_as_file)
registry.register("exit", exit_app)
registry.register("cut", cut)
registry.register("copy", copy)
registry.register("paste", paste)
registry.register("select_all", select_all)
registry.register("about", about)
registry.register("load_menu_layout", load_menu_layout)
