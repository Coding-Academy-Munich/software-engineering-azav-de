import pickle
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _typeshed import SupportsWrite


@dataclass
class Note:
    """Represents a single note with title, text, and tags."""
    title: str
    text: str
    tags: set[str] = field(default_factory=set)

    def __post_init__(self):
        """Ensure tags is always a set."""
        if isinstance(self.tags, (list, tuple)):
            self.tags = set(self.tags)

    def matches_search(self, query: str, search_title: bool = True,
                      search_text: bool = True, search_tags: bool = True) -> bool:
        """Check if the note matches a search query."""
        query_lower = query.lower()

        if search_title and query_lower in self.title.lower():
            return True
        if search_text and query_lower in self.text.lower():
            return True
        if search_tags and any(query_lower in tag.lower() for tag in self.tags):
            return True

        return False


@dataclass
class NoteCollection:
    """A collection of notes with functionality for managing them."""
    notes: list[Note] = field(default_factory=list)

    def add_note(self, title: str, text: str, tags: list[str] | None = None) -> bool:
        """
        Add a new note to the collection.

        Args:
            title: The note title
            text: The note text
            tags: Optional list of tags

        Returns:
            True if note was added, False if a note with the same title already exists
        """
        if self.get_note_by_title(title) is not None:
            return False

        note_tags = set(tags) if tags else set()
        note = Note(title=title, text=text, tags=note_tags)
        self.notes.append(note)
        return True

    def get_note_by_title(self, title: str) -> Note | None:
        """Get a note by its exact title."""
        for note in self.notes:
            if note.title == title:
                return note
        return None

    def delete_note(self, title: str) -> bool:
        """
        Delete a note by title.

        Args:
            title: The title of the note to delete

        Returns:
            True if note was deleted, False if note was not found
        """
        note = self.get_note_by_title(title)
        if note is None:
            return False

        self.notes.remove(note)
        return True

    def search_notes(self, query: str, search_title: bool = True,
                    search_text: bool = True, search_tags: bool = True) -> list[Note]:
        """
        Search for notes matching the given criteria.

        Args:
            query: The search query
            search_title: Whether to search in titles
            search_text: Whether to search in text
            search_tags: Whether to search in tags

        Returns:
            List of matching notes
        """
        return [
            note for note in self.notes
            if note.matches_search(query, search_title, search_text, search_tags)
        ]

    def get_all_notes(self) -> list[Note]:
        """Get all notes in the collection."""
        return self.notes.copy()

    def save_to_file(self, file_path: Path) -> None:
        """Save the note collection to a pickle file."""
        file_path.parent.mkdir(parents=True, exist_ok=True)
        f: "SupportsWrite[bytes]"
        with open(file_path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_from_file(cls, file_path: Path) -> 'NoteCollection':
        """
        Load a note collection from a pickle file.

        Returns:
            NoteCollection instance, or empty collection if file doesn't exist
        """
        if not file_path.exists():
            return cls()

        try:
            with open(file_path, 'rb') as f:
                return pickle.load(f)
        except (pickle.PickleError, EOFError, FileNotFoundError):
            # If file is corrupted or empty, return empty collection
            return cls()
