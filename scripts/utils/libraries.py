from pathlib import Path


def convert_requirements_to_list(requirements_file: Path) -> list[str]:
    libraries: list[str] = []
    if requirements_file.exists():
        with open(requirements_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    # Extract library name (remove version specifiers)
                    library_name = (
                        line.split("==")[0]
                        .split(">=")[0]
                        .split("<=")[0]
                        .split("~=")[0]
                        .split("!=")[0]
                        .split(">")[0]
                        .split("<")[0]
                        .strip()
                    )
                    libraries.append(library_name)
    return libraries
