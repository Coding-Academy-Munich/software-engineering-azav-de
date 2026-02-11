# JSON Menu App

A simple text editor demonstrating JSON-based menu configuration.

This example shows how to use JSON to configure a complete application menu
system using the object serialization patterns covered in the course.

## Installation

```bash
pip install -e .
```

Or with uv:

```bash
uv sync
```

## Usage

```bash
json-menu-app
```

Or directly:

```bash
python -m json_menu_app
```

## Menu Configuration

The menu structure is defined in `data/menu-config.json`. You can modify this
file to add or remove menus and menu items, change keyboard shortcuts, or
reorder entries.

The format uses `_type` fields to distinguish between:
- `menu`: Top-level menu containers
- `menuitem`: Individual menu entries with actions
- `separator`: Visual separators between menu items
