import os
import shutil
from typing import Iterable


class FileManager:
    """Utility class for common file operations."""

    @staticmethod
    def remove_same_name(file_path: str, dest_dir: str) -> None:
        """Delete file with the same name in ``dest_dir`` if it exists."""
        dest_file = os.path.join(dest_dir, os.path.basename(file_path))
        if os.path.exists(dest_file):
            os.remove(dest_file)

    @staticmethod
    def copy_all_files(src_dir: str, dest_dir: str) -> None:
        """Copy all files from ``src_dir`` into ``dest_dir``."""
        if not os.path.isdir(src_dir):
            raise FileNotFoundError(src_dir)
        os.makedirs(dest_dir, exist_ok=True)
        for name in os.listdir(src_dir):
            src_path = os.path.join(src_dir, name)
            if os.path.isfile(src_path):
                FileManager.remove_same_name(src_path, dest_dir)
                shutil.copy2(src_path, dest_dir)

    @staticmethod
    def copy_files(files: Iterable[str], dest_dir: str) -> None:
        """Copy the given ``files`` into ``dest_dir``."""
        os.makedirs(dest_dir, exist_ok=True)
        for path in files:
            if os.path.isfile(path):
                FileManager.remove_same_name(path, dest_dir)
                shutil.copy2(path, dest_dir)

    @staticmethod
    def delete_files(files: Iterable[str]) -> None:
        """Delete the given ``files`` if they exist."""
        for path in files:
            if os.path.isfile(path):
                os.remove(path)

    @staticmethod
    def get_size_mb(path: str) -> float:
        """Return the size of ``path`` in megabytes."""
        total = 0
        if os.path.isfile(path):
            total += os.path.getsize(path)
        else:
            for root, _, files in os.walk(path):
                for name in files:
                    full_path = os.path.join(root, name)
                    total += os.path.getsize(full_path)
        return total / (1024 * 1024)

    @staticmethod
    def count_files(path: str) -> int:
        """Return the number of files under ``path``."""
        if os.path.isfile(path):
            return 1
        count = 0
        for _, _, files in os.walk(path):
            count += len(files)
        return count


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="File management utilities")
    parser.add_argument("action", choices=["size", "count"], help="Action to perform")
    parser.add_argument("path", help="Target file or directory")
    args = parser.parse_args()

    if args.action == "size":
        print(f"{FileManager.get_size_mb(args.path):.2f} MB")
    elif args.action == "count":
        print(FileManager.count_files(args.path))
