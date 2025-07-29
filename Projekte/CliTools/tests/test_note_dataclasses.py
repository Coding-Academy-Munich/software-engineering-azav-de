import pytest
from cli_tools.notes.note import Note, NoteCollection


class TestNote:
    """Tests for the Note dataclass."""

    def test_note_creation(self):
        """Test basic note creation."""
        note = Note("Test Title", "Test text", {"tag1", "tag2"})
        assert note.title == "Test Title"
        assert note.text == "Test text"
        assert note.tags == {"tag1", "tag2"}

    def test_note_creation_with_list_tags(self):
        """Test note creation with tags as list (should convert to set)."""
        note = Note("Test Title", "Test text", ["tag1", "tag2", "tag1"])
        assert note.tags == {"tag1", "tag2"}

    def test_note_creation_without_tags(self):
        """Test note creation without tags."""
        note = Note("Test Title", "Test text")
        assert note.tags == set()

    def test_matches_search_title(self):
        """Test search matching in title."""
        note = Note("Python Programming", "Learn about functions", {"coding"})

        assert note.matches_search("Python")
        assert note.matches_search("python")  # case insensitive
        assert note.matches_search("Programming")
        assert not note.matches_search("Java")

    def test_matches_search_text(self):
        """Test search matching in text."""
        note = Note("Tutorial", "Learn Python programming", {"coding"})

        assert note.matches_search("Learn")
        assert note.matches_search("python")  # case insensitive
        assert note.matches_search("programming")
        assert not note.matches_search("Java")

    def test_matches_search_tags(self):
        """Test search matching in tags."""
        note = Note("Tutorial", "Learn programming", {"python", "coding"})

        assert note.matches_search("python")
        assert note.matches_search("Python")  # case insensitive
        assert note.matches_search("coding")
        assert not note.matches_search("java")

    def test_matches_search_selective(self):
        """Test search with selective criteria."""
        note = Note("Python Tutorial", "Learn Java", {"coding"})

        # Search only in title
        assert note.matches_search("Python", search_title=True, search_text=False, search_tags=False)
        assert not note.matches_search("Java", search_title=True, search_text=False, search_tags=False)

        # Search only in text
        assert note.matches_search("Java", search_title=False, search_text=True, search_tags=False)
        assert not note.matches_search("Python", search_title=False, search_text=True, search_tags=False)

        # Search only in tags
        assert note.matches_search("coding", search_title=False, search_text=False, search_tags=True)
        assert not note.matches_search("Python", search_title=False, search_text=False, search_tags=True)


class TestNoteCollection:
    """Tests for the NoteCollection dataclass."""

    def test_empty_collection(self):
        """Test creating an empty collection."""
        collection = NoteCollection()
        assert len(collection.notes) == 0
        assert collection.get_all_notes() == []

    def test_add_note_success(self):
        """Test successfully adding a note."""
        collection = NoteCollection()
        result = collection.add_note("Test Title", "Test text", ["tag1", "tag2"])

        assert result is True
        assert len(collection.notes) == 1

        note = collection.notes[0]
        assert note.title == "Test Title"
        assert note.text == "Test text"
        assert note.tags == {"tag1", "tag2"}

    def test_add_note_duplicate_title(self):
        """Test adding a note with duplicate title fails."""
        collection = NoteCollection()
        collection.add_note("Test Title", "First text")

        result = collection.add_note("Test Title", "Second text")
        assert result is False
        assert len(collection.notes) == 1
        assert collection.notes[0].text == "First text"

    def test_add_note_without_tags(self):
        """Test adding a note without tags."""
        collection = NoteCollection()
        result = collection.add_note("Test Title", "Test text")

        assert result is True
        assert collection.notes[0].tags == set()

    def test_get_note_by_title(self):
        """Test getting a note by title."""
        collection = NoteCollection()
        collection.add_note("First Note", "First text")
        collection.add_note("Second Note", "Second text")

        note = collection.get_note_by_title("First Note")
        assert note is not None
        assert note.title == "First Note"
        assert note.text == "First text"

        note = collection.get_note_by_title("Nonexistent")
        assert note is None

    def test_delete_note_success(self):
        """Test successfully deleting a note."""
        collection = NoteCollection()
        collection.add_note("Test Title", "Test text")

        result = collection.delete_note("Test Title")
        assert result is True
        assert len(collection.notes) == 0

    def test_delete_note_not_found(self):
        """Test deleting a non-existent note."""
        collection = NoteCollection()
        collection.add_note("Test Title", "Test text")

        result = collection.delete_note("Nonexistent")
        assert result is False
        assert len(collection.notes) == 1

    def test_search_notes_general(self):
        """Test general search across all fields."""
        collection = NoteCollection()
        collection.add_note("Python Tutorial", "Learn Python programming", ["coding", "education"])
        collection.add_note("Java Guide", "Introduction to Java", ["coding", "beginner"])
        collection.add_note("Database Notes", "SQL and NoSQL concepts", ["database", "education"])

        # Search that matches title
        results = collection.search_notes("Python")
        assert len(results) == 1
        assert results[0].title == "Python Tutorial"

        # Search that matches text
        results = collection.search_notes("Introduction")
        assert len(results) == 1
        assert results[0].title == "Java Guide"

        # Search that matches tags
        results = collection.search_notes("education")
        assert len(results) == 2
        titles = {note.title for note in results}
        assert titles == {"Python Tutorial", "Database Notes"}

    def test_search_notes_selective(self):
        """Test search with selective criteria."""
        collection = NoteCollection()
        collection.add_note("Python Tutorial", "Learn Java programming", ["coding"])

        # Search only in title
        results = collection.search_notes("Python", search_title=True, search_text=False, search_tags=False)
        assert len(results) == 1

        results = collection.search_notes("Java", search_title=True, search_text=False, search_tags=False)
        assert len(results) == 0

        # Search only in text
        results = collection.search_notes("Java", search_title=False, search_text=True, search_tags=False)
        assert len(results) == 1

        results = collection.search_notes("Python", search_title=False, search_text=True, search_tags=False)
        assert len(results) == 0

    def test_search_notes_case_insensitive(self):
        """Test that search is case insensitive."""
        collection = NoteCollection()
        collection.add_note("Python Tutorial", "Learn programming", ["CODING"])

        results = collection.search_notes("python")
        assert len(results) == 1

        results = collection.search_notes("PROGRAMMING")
        assert len(results) == 1

        results = collection.search_notes("coding")
        assert len(results) == 1

    def test_search_notes_no_matches(self):
        """Test search with no matches."""
        collection = NoteCollection()
        collection.add_note("Python Tutorial", "Learn programming", ["coding"])

        results = collection.search_notes("JavaScript")
        assert len(results) == 0

    def test_get_all_notes(self):
        """Test getting all notes returns a copy."""
        collection = NoteCollection()
        collection.add_note("Note 1", "Text 1")
        collection.add_note("Note 2", "Text 2")

        all_notes = collection.get_all_notes()
        assert len(all_notes) == 2

        # Modifying the returned list shouldn't affect the original
        all_notes.append(Note("Note 3", "Text 3"))
        assert len(collection.notes) == 2
