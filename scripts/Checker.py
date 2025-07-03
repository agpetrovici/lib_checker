from pathlib import Path

from scripts.utils.libraries import convert_requirements_to_list


class Checker:
    def __init__(self, requirements_file: Path, repo_path: Path):
        self.requirements_file = requirements_file
        self.repo_path = repo_path
        self._libraries_raw = []
        self._libraries_used = []

    def check_libraries(self):
        self._libraries_raw = convert_requirements_to_list(self.requirements_file)
        self._libraries_used = self._get_libraries_used()

    def _get_libraries_used(self) -> list[str]:
        libraries_used: list[str] = []
        for file in self.repo_path.glob("**/*.py"):
            with open(file, "r") as f:
                content = f.read()
                for library in self._libraries_raw:
                    # Check if library is mentioned in non-comment lines
                    lines = content.split("\n")
                    for line in lines:
                        # Skip lines that are comments (start with #)
                        if line.strip().startswith("#"):
                            continue
                        if (line.strip().startswith("from ") or line.strip().startswith("import ")) and library in line:
                            libraries_used.append(library)
                            break
        print(libraries_used)
        libraries_used = sorted(list(set(libraries_used)))

        # Filter out Python standard libraries
        python_standard_libraries = [
            "abc",
            "argparse",
            "asyncio",
            "base64",
            "collections",
            "contextlib",
            "datetime",
            "decimal",
            "difflib",
            "enum",
            "functools",
            "glob",
            "gzip",
            "hashlib",
            "http",
            "importlib",
            "inspect",
            "io",
            "itertools",
            "json",
            "logging",
            "math",
            "multiprocessing",
            "operator",
            "os",
            "pathlib",
            "pickle",
            "random",
            "re",
            "shutil",
            "signal",
            "socket",
            "sqlite3",
            "statistics",
            "string",
            "subprocess",
            "sys",
            "tempfile",
            "threading",
            "time",
            "traceback",
            "typing",
            "unittest",
            "urllib",
            "uuid",
            "xml",
            "zipfile",
            "zlib",
        ]

        # Remove standard libraries from the used libraries list
        libraries_used = [
            lib for lib in libraries_used if lib not in python_standard_libraries
        ]

        return libraries_used

    def print_report(self) -> None:
        print("Library Usage Report")
        print("==================")
        print(f"Total libraries in requirements: {len(self._libraries_raw)}")
        print(f"Libraries actually used: {len(self._libraries_used)}")
        print(
            f"Usage ratio: {len(self._libraries_used)}/{len(self._libraries_raw)} ({len(self._libraries_used) / len(self._libraries_raw) * 100:.1f}%)"
        )
        print()
        print("Libraries used in the codebase:")
        for library in self._libraries_used:
            print(f"  - {library}")
