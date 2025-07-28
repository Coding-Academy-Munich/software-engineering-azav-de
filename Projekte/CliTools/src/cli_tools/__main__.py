from . import __version__

import typer
from typing_extensions import Annotated
from rich import print


def version_callback(value: bool):
    if value:
        print(f"Python CLI Tools (Version {__version__})")
        raise typer.Exit()


def typer_main(
        version: Annotated[
            bool | None,
            typer.Option(help="Show the version and exit.", callback=version_callback),
        ] = None,
):
    print("[bold blue]Python CLI Tools[/bold blue]")
    print("[red]my-ls[/red]:      List files in a directory.")
    print("[red]my-cat[/red]:     Print the contents of a file.")


def main():
    typer.run(typer_main)


if __name__ == "__main__":
    main()
