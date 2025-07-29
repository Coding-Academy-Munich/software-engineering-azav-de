#!/usr/bin/env python3
"""
A simple note-taking CLI application built with typer.
"""

import typer
from pathlib import Path

import platformdirs
from rich.console import Console
from rich.table import Table
from rich import print as rprint

from .note import NoteCollection

app = typer.Typer(help="A simple note-taking application")
console = Console()


def get_notes_file_path() -> Path:
    """Get the platform-specific path for storing notes."""
    app_dir = platformdirs.user_data_dir("notes-app", "python-course")
    return Path(app_dir) / "notes.pkl"


def load_notes() -> NoteCollection:
    """Load notes from the pickle file."""
    notes_file = get_notes_file_path()
    return NoteCollection.load_from_file(notes_file)


def save_notes(collection: NoteCollection) -> None:
    """Save notes to the pickle file."""
    notes_file = get_notes_file_path()
    collection.save_to_file(notes_file)


@app.command()
def add(
    title: str = typer.Argument(..., help="The title of the note"),
    text: str = typer.Argument(..., help="The text content of the note"),
    tag: list[str] | None = typer.Option(
        None, "--tag", help="Add a tag (can be used multiple times)"
    ),
    tags: str | None = typer.Option(
        None, "--tags", help="Comma-separated list of tags"
    ),
):
    """Add a new note with the given title, text, and optional tags."""
    # Combine tags from both options
    all_tags = []
    if tag:
        all_tags.extend(tag)
    if tags:
        all_tags.extend([t.strip() for t in tags.split(",")])

    # Remove empty tags
    all_tags = [t for t in all_tags if t.strip()]

    collection = load_notes()

    if collection.add_note(title, text, all_tags):
        save_notes(collection)
        rprint(f"[green]✓[/green] Note '{title}' added successfully!")
        if all_tags:
            rprint(f"[dim]Tags: {', '.join(all_tags)}[/dim]")
    else:
        rprint(f"[red]✗[/red] Error: A note with title '{title}' already exists!")
        raise typer.Exit(1)


@app.command()
def show(
    full: bool = typer.Option(
        False, "--full", help="Show full text of notes, not just titles"
    )
):
    """Show all notes."""
    collection = load_notes()
    notes = collection.get_all_notes()

    if not notes:
        rprint("[yellow]No notes found.[/yellow]")
        return

    if full:
        # Show full notes
        for i, note in enumerate(notes, 1):
            rprint(f"\n[bold blue]{i}. {note.title}[/bold blue]")
            rprint(f"[dim]{note.text}[/dim]")
            if note.tags:
                rprint(f"[green]Tags: {', '.join(sorted(note.tags))}[/green]")
    else:
        # Show just titles in a table
        table = Table(title="All Notes")
        table.add_column("Title", style="cyan")
        table.add_column("Tags", style="green")

        for note in notes:
            tags_str = ", ".join(sorted(note.tags)) if note.tags else ""
            table.add_row(note.title, tags_str)

        console.print(table)


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    title: bool = typer.Option(False, "--title", help="Search only in titles"),
    text: bool = typer.Option(False, "--text", help="Search only in text"),
    tag: bool = typer.Option(False, "--tag", help="Search only in tags"),
):
    """Search for notes matching the given criteria."""
    collection = load_notes()

    # If no specific search type is specified, search in all fields
    if not any([title, text, tag]):
        search_title = search_text = search_tags = True
    else:
        search_title = title
        search_text = text
        search_tags = tag

    results = collection.search_notes(query, search_title, search_text, search_tags)

    if not results:
        rprint(f"[yellow]No notes found matching '{query}'[/yellow]")
        return

    rprint(f"[green]Found {len(results)} note(s) matching '{query}':[/green]\n")

    for i, note in enumerate(results, 1):
        rprint(f"[bold blue]{i}. {note.title}[/bold blue]")
        rprint(f"[dim]{note.text}[/dim]")
        if note.tags:
            rprint(f"[green]Tags: {', '.join(sorted(note.tags))}[/green]")
        rprint()  # Empty line between notes


@app.command()
def delete(title: str = typer.Argument(..., help="The title of the note to delete")):
    """Delete a note by its title."""
    collection = load_notes()

    if collection.delete_note(title):
        save_notes(collection)
        rprint(f"[green]✓[/green] Note '{title}' deleted successfully!")
    else:
        rprint(f"[red]✗[/red] Error: No note found with title '{title}'!")
        raise typer.Exit(1)


@app.command()
def info():
    """Show information about the notes storage."""
    notes_file = get_notes_file_path()
    collection = load_notes()

    rprint(f"[bold]Notes Storage Information[/bold]")
    rprint(f"Storage location: {notes_file}")
    rprint(f"File exists: {'Yes' if notes_file.exists() else 'No'}")
    rprint(f"Number of notes: {len(collection.get_all_notes())}")


if __name__ == "__main__":
    app()
