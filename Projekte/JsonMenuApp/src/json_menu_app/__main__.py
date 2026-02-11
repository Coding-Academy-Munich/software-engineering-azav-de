"""Entry point for the JSON Menu App."""

import argparse

from json_menu_app.app import TextEditorApp


def main():
    parser = argparse.ArgumentParser(
        description="A text editor with JSON-configured menus."
    )
    parser.add_argument(
        "--config",
        help="Path to menu configuration JSON file",
        default=None,
    )
    args = parser.parse_args()
    app = TextEditorApp(config_path=args.config)
    app.run()


if __name__ == "__main__":
    main()
