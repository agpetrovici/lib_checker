# Library Usage Checker

This project analyzes Python projects to identify which libraries listed in a `requirements.txt` file are actually being used in the codebase. It compares the declared dependencies against the actual import statements found in Python files throughout the project.

## How it works

The tool scans all Python files in the specified repository path and checks for import statements that match libraries listed in the requirements file. It filters out Python standard libraries and provides a detailed report showing:

- Total number of libraries in requirements.txt
- Number of libraries actually used in the code
- Usage ratio percentage
- List of libraries that are actively used

This helps identify used dependencies to help manage the project with poetry or uv.

## Usage example


```python
from pathlib import Path

from scripts.Checker import Checker

checker = Checker(
    requirements_file=Path(
        "/repository/requirements.txt"
    ),
    repo_path=Path(
        "/repository",
    ),
)

checker.check_libraries()
checker.print_report()
```

Output

```text
Library Usage Report
==================
Total libraries in requirements: 298
Libraries actually used: 19
Usage ratio: 19/298 (6.4%)

Libraries used in the codebase:
  - boto
  - boto3
  - comm
  - fiona
  - fuzzywuzzy
  - geopandas
  - lxml
  - mxlogging
  - numpy
  - pandas
  - psutil
  - regex
  - requests
  - selenium
  - shapely
  - sos
  - urllib3
  - watchdog
```