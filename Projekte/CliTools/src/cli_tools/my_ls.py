from pathlib import Path
from typing import Annotated

import typer


def get_files(path: Path) -> list[Path]:
    if not path.exists():
        raise ValueError(f"Path {path} does not exist")
    elif path.is_dir():
        files = list(path.glob("*"))
    else:
        files = [path]
    return sorted(files)


def print_files(path: Annotated[Path, typer.Argument(help="The path to list.")] = Path.cwd(),
                verbose: Annotated[bool, typer.Option("--verbose", "-v", help="Show more information.")] = False):
    files = get_files(path)
    if verbose:
        print_files_verbose(files)
    else:
        for file in files:
            if file.is_dir():
                print(f"{file.name}/")
            else:
                print(file.name)


def print_files_verbose(files):
    max_filename_length = max((len(file.name) for file in files if not file.is_dir()), default=0)
    max_size_length = len(str(max((file.stat().st_size for file in files if not file.is_dir()), default=0)))
    for file in files:
        if file.is_dir():
            print(f"{file.name}/")
        else:
            print(f"{file.name:<{max_filename_length + 1}}{file.stat().st_size:>{max_size_length}} bytes")


def ls():
    typer.run(print_files)


if __name__ == "__main__":
    ls()
