import pytest
import tempfile
from pathlib import Path
from typer.testing import CliRunner
from unittest.mock import patch

from cli_tools.notes.note import NoteCollection
from cli_tools.notes.notes_app import app, get_notes_file_path, load_notes, save_notes

runner = CliRunner()


class TestStorageFunctions:
    """Test the storage-related functions."""
    
    def test_get_notes_file_path(self):
        """Test that get_notes_file_path returns a valid path."""
        path = get_notes_file_path()
        assert isinstance(path, Path)
        assert path.name == "notes.pkl"
        assert "notes-app" in str(path)
    
    def test_load_notes_empty_file(self):
        """Test loading notes when file doesn't exist."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "nonexistent.pkl"
            
            with patch('cli_tools.notes.notes_app.get_notes_file_path', return_value=temp_file):
                collection = load_notes()
                assert isinstance(collection, NoteCollection)
                assert len(collection.notes) == 0
    
    def test_save_and_load_notes(self):
        """Test saving and loading notes to/from a file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "test_notes.pkl"
            
            # Create a collection with some notes
            original_collection = NoteCollection()
            original_collection.add_note("Test Note", "Test content", ["tag1", "tag2"])
            original_collection.add_note("Another Note", "More content", ["tag3"])
            
            # Save the collection
            with patch('cli_tools.notes.notes_app.get_notes_file_path', return_value=temp_file):
                save_notes(original_collection)
                
                # Verify file was created
                assert temp_file.exists()
                
                # Load the collection
                loaded_collection = load_notes()
                
                # Verify the loaded collection matches the original
                assert len(loaded_collection.notes) == 2
                
                note1 = loaded_collection.get_note_by_title("Test Note")
                assert note1 is not None
                assert note1.text == "Test content"
                assert note1.tags == {"tag1", "tag2"}
                
                note2 = loaded_collection.get_note_by_title("Another Note")
                assert note2 is not None
                assert note2.text == "More content"
                assert note2.tags == {"tag3"}
    
    def test_load_notes_corrupted_file(self):
        """Test loading notes from a corrupted pickle file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "corrupted.pkl"
            
            # Create a corrupted file
            with open(temp_file, 'w') as f:
                f.write("This is not a pickle file")
            
            with patch('cli_tools.notes.notes_app.get_notes_file_path', return_value=temp_file):
                collection = load_notes()
                assert isinstance(collection, NoteCollection)
                assert len(collection.notes) == 0


class TestCLICommands:
    """Test the CLI commands with temporary storage."""
    
    @pytest.fixture
    def temp_notes_file(self):
        """Fixture that provides a temporary notes file."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / "test_notes.pkl"
            with patch('cli_tools.notes.notes_app.get_notes_file_path', return_value=temp_file):
                yield temp_file
    
    def test_add_command_success(self, temp_notes_file):
        """Test successfully adding a note via CLI."""
        result = runner.invoke(app, [
            "add", "Test Title", "Test content",
            "--tag", "python",
            "--tag", "programming"
        ])
        
        assert result.exit_code == 0
        assert "Note 'Test Title' added successfully!" in result.stdout
        assert "Tags: python, programming" in result.stdout
        
        # Verify the note was saved
        assert temp_notes_file.exists()
        collection = NoteCollection.load_from_file(temp_notes_file)
        note = collection.get_note_by_title("Test Title")
        assert note is not None
        assert note.text == "Test content"
        assert note.tags == {"python", "programming"}
    
    def test_add_command_with_comma_separated_tags(self, temp_notes_file):
        """Test adding a note with comma-separated tags."""
        result = runner.invoke(app, [
            "add", "Test Title", "Test content",
            "--tags", "python,programming,tutorial"
        ])
        
        assert result.exit_code == 0
        
        collection = NoteCollection.load_from_file(temp_notes_file)
        note = collection.get_note_by_title("Test Title")
        assert note.tags == {"python", "programming", "tutorial"}
    
    def test_add_command_duplicate_title(self, temp_notes_file):
        """Test adding a note with duplicate title fails."""
        # Add first note
        runner.invoke(app, ["add", "Test Title", "First content"])
        
        # Try to add second note with same title
        result = runner.invoke(app, ["add", "Test Title", "Second content"])
        
        assert result.exit_code == 1
        assert "A note with title 'Test Title' already exists!" in result.stdout
    
    def test_show_command_empty(self, temp_notes_file):
        """Test show command with no notes."""
        result = runner.invoke(app, ["show"])
        
        assert result.exit_code == 0
        assert "No notes found." in result.stdout
    
    def test_show_command_with_notes(self, temp_notes_file):
        """Test show command with existing notes."""
        # Add some notes
        runner.invoke(app, ["add", "Note 1", "Content 1", "--tag", "tag1"])
        runner.invoke(app, ["add", "Note 2", "Content 2", "--tag", "tag2"])
        
        result = runner.invoke(app, ["show"])
        
        assert result.exit_code == 0
        assert "Note 1" in result.stdout
        assert "Note 2" in result.stdout
        assert "tag1" in result.stdout
        assert "tag2" in result.stdout
    
    def test_show_command_full(self, temp_notes_file):
        """Test show command with --full flag."""
        runner.invoke(app, ["add", "Test Note", "Test content", "--tag", "test"])
        
        result = runner.invoke(app, ["show", "--full"])
        
        assert result.exit_code == 0
        assert "Test Note" in result.stdout
        assert "Test content" in result.stdout
        assert "Tags: test" in result.stdout
    
    def test_search_command_found(self, temp_notes_file):
        """Test search command finding notes."""
        runner.invoke(app, ["add", "Python Tutorial", "Learn Python programming", "--tag", "coding"])
        runner.invoke(app, ["add", "Java Guide", "Introduction to Java", "--tag", "programming"])
        
        result = runner.invoke(app, ["search", "Python"])
        
        assert result.exit_code == 0
        assert "Found 1 note(s) matching 'Python'" in result.stdout
        assert "Python Tutorial" in result.stdout
        assert "Learn Python programming" in result.stdout
    
    def test_search_command_not_found(self, temp_notes_file):
        """Test search command when no notes match."""
        runner.invoke(app, ["add", "Test Note", "Test content"])
        
        result = runner.invoke(app, ["search", "JavaScript"])
        
        assert result.exit_code == 0
        assert "No notes found matching 'JavaScript'" in result.stdout
    
    def test_search_command_specific_field(self, temp_notes_file):
        """Test search command with specific field options."""
        runner.invoke(app, ["add", "Python Tutorial", "Learn Java programming", "--tag", "coding"])
        
        # Search only in title
        result = runner.invoke(app, ["search", "Python", "--title"])
        assert result.exit_code == 0
        assert "Found 1 note(s) matching 'Python'" in result.stdout
        
        # Search only in text (should not find Python)
        result = runner.invoke(app, ["search", "Python", "--text"])
        assert result.exit_code == 0
        assert "No notes found matching 'Python'" in result.stdout
        
        # Search only in text (should find Java)
        result = runner.invoke(app, ["search", "Java", "--text"])
        assert result.exit_code == 0
        assert "Found 1 note(s) matching 'Java'" in result.stdout
    
    def test_delete_command_success(self, temp_notes_file):
        """Test successfully deleting a note."""
        runner.invoke(app, ["add", "Test Note", "Test content"])
        
        result = runner.invoke(app, ["delete", "Test Note"])
        
        assert result.exit_code == 0
        assert "Note 'Test Note' deleted successfully!" in result.stdout
        
        # Verify note was deleted
        collection = NoteCollection.load_from_file(temp_notes_file)
        assert collection.get_note_by_title("Test Note") is None
    
    def test_delete_command_not_found(self, temp_notes_file):
        """Test deleting a non-existent note."""
        result = runner.invoke(app, ["delete", "Nonexistent Note"])
        
        assert result.exit_code == 1
        assert "No note found with title 'Nonexistent Note'!" in result.stdout
    
    def test_info_command(self, temp_notes_file):
        """Test the info command."""
        runner.invoke(app, ["add", "Test Note", "Test content"])
        
        result = runner.invoke(app, ["info"])
        
        assert result.exit_code == 0
        assert "Notes Storage Information" in result.stdout
        assert "Storage location:" in result.stdout
        assert "File exists: Yes" in result.stdout
        assert "Number of notes: 1" in result.stdout