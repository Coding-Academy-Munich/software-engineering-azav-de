from pathlib import Path


def root_dir_path():
    return Path(__file__).parents[1] / "test_dir"
