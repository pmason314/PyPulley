"""
Post-project-creation hooks.

After successfully creating the cookiecutter and validating it with the pre-generation hooks, set up the new project
 environment by installing Python, Poetry, and other dev dependencies.
"""

import os
import re
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def install_python_and_deps():
    """Automatically install the specified version of Python as well as other standard development tooling."""
    python_version = "{{ cookiecutter.python_version }}"
    if python_version == "latest":
        standard_version_regex = r"^3.[0-9]+.[0-9]+$"
        subprocess.run(["pyenv", "update"])  # Make sure most recent Python versions are accessible
        cmd_output = subprocess.run(["pyenv", "install", "--list"], capture_output=True, encoding="UTF-8")
        all_versions = cmd_output.stdout.split("\n")
        all_versions = map(lambda x: x.strip(), all_versions)
        all_versions = list(filter(lambda version: re.match(standard_version_regex, version), all_versions))
        python_version = all_versions[-1]

    subprocess.run(["pyenv", "install", f"{python_version}"])
    subprocess.run(["pyenv", "local", f"{python_version}"])
    subprocess.run(["pip", "install", "--upgrade", "pip"])
    subprocess.run(["pip", "install", "poetry"])
    subprocess.run(["poetry", "install"])

    if "{{ cookiecutter.create_git_repo }}" == "y":
        subprocess.run(["git", "init"])
        subprocess.run(["poetry", "run", "pre-commit", "install"])


def create_sphinx_docs():
    """Create initial Sphinx documentation setup using the Sphinx api-doc extension."""
    pass


if __name__ == "__main__":
    if "{{ cookiecutter.license }}" == "Not Open Source":
        os.remove(os.path.join(PROJECT_DIRECTORY, "LICENSE"))
    install_python_and_deps()

    if "{{ cookiecutter.create_sphinx_docs }}" == "y":
        create_sphinx_docs()
