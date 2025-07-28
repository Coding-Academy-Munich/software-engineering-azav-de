from cli_tools.my_ls import get_files, print_files
from utils import root_dir_path


def test_get_files_for_root_dir():
    expected = ["file-1.txt", "file-2.md", "file-3.txt", "subdir", "utils.cpp"]
    result = get_files(root_dir_path())
    assert [path.name for path in result] == expected


def test_get_files_for_subdir():
    expected = ["file-4.txt"]
    result = get_files(root_dir_path() / "subdir")
    assert [path.name for path in result] == expected


def test_get_files_for_file():
    expected = ["file-1.txt"]
    result = get_files(root_dir_path() / "file-1.txt")
    assert [path.name for path in result] == expected


def test_print_files_for_root_dir(capsys):
    print_files(root_dir_path())
    captured = capsys.readouterr()
    assert captured.out == "file-1.txt\nfile-2.md\nfile-3.txt\nsubdir/\nutils.cpp\n"