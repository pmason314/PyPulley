"""Pre-project-creation hooks.

After all arguments to the cookiecutter project template have been given, validate the inputs.  If any fail, abort the
 creation process and clean up any created resources.
"""

import re
import sys


def validate_project_slug() -> None:
    """Validate that the project slug given during project creation can be a proper Python module name."""
    valid_module_regex = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
    module_name = "{{ cookiecutter.project_slug}}"

    if not re.match(valid_module_regex, module_name):
        print(
            f"""ERROR: The project slug {module_name} is not a valid Python module name.
              Please use _ instead of -"""
        )
        # Cancel project creation
        sys.exit(1)


def validate_python_version() -> None:
    """Validate that the version of Python given during project creation.  Only accepts standard CPython versions."""
    python_version = "{{ cookiecutter.python_version }}"
    valid_version_regex = r"^(latest|3|3.[0-9]+|3.[0-9]+.[0-9]+)$"

    if not re.match(valid_version_regex, python_version):
        print(
            f"""ERROR: {python_version} is not a valid version of Python.
              Please choose 'latest' or a specific version like '3.10.8'"""
        )
        # Cancel project creation
        sys.exit(1)


if __name__ == "__main__":
    validate_project_slug()
    validate_python_version()
