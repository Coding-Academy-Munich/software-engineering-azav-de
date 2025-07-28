from cli_tools.my_cat import print_file
from utils import root_dir_path


def test_print_file(capsys):
    print_file(root_dir_path() / "file-1.txt")
    captured = capsys.readouterr()
    assert "Some text.\n1234" in captured.out.strip()
