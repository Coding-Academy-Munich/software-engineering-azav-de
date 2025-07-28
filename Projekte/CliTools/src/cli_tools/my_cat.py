from pathlib import Path
from typing import Annotated
import typer
import rich

def print_file(path: Annotated[Path, typer.Argument(help="The file to print.", show_default=False, exists=True)]):
    # Printing the rules with the fancy file names is, of course, completely optional
    rich.get_console().rule(file_name(path))
    print(path.read_text())
    rich.get_console().rule(file_name(path))


def file_name(path):
    console_size = rich.get_console().size
    max_path_length = console_size.width - 8
    absolute_path = path.absolute().as_posix()
    if len(absolute_path) > max_path_length:
        return f"...{absolute_path[-max_path_length:]}"
    return absolute_path


def cat():
    typer.run(print_file)


if __name__ == "__main__":
    cat()
