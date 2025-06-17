import os
import sys


def print_tree(path: str, prefix: str = "") -> None:
    """Recursively print a tree representation of files under ``path``."""
    try:
        entries = sorted(os.listdir(path))
    except FileNotFoundError:
        print(f"Path not found: {path}")
        return

    for index, name in enumerate(entries):
        full_path = os.path.join(path, name)
        connector = "└── " if index == len(entries) - 1 else "├── "
        print(prefix + connector + name)
        if os.path.isdir(full_path):
            extension = "    " if index == len(entries) - 1 else "│   "
            print_tree(full_path, prefix + extension)


if __name__ == "__main__":
    start = sys.argv[1] if len(sys.argv) > 1 else "."
    print(start)
    print_tree(start)
