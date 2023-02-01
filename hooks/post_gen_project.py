"""
Post-project-creation hooks.

After successfully creating the cookiecutter and validating it with the pre-generation hooks, set up the new project
 environment by installing Python, Poetry, and other dev dependencies.
"""

import os
import pathlib
import re
import shutil
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_unused_resources():
    """Delete unused files and directories related to declined template configuration options."""
    if "{{ cookiecutter.license }}" == "Not Open Source":
        pathlib.unlink(PROJECT_DIRECTORY / "LICENSE")

    if "{{ cookiecutter.create_git_repo }}" == "n":
        pathlib.unlink(PROJECT_DIRECTORY / ".pre-commit-config.yaml")

    if "{{ cookiecutter.create_sphinx_docs }}" == "n":
        shutil.rmtree(PROJECT_DIRECTORY / "docs")


def install_python():
    """Figure out and install the specified version of Python."""
    python_version = "{{ cookiecutter.python_version }}"
    standard_version_regex = r"^3.[0-9]+.[0-9]+$"

    subprocess.run(["pyenv", "update"])  # Make sure most recent Python versions are accessible
    cmd_output = subprocess.run(["pyenv", "install", "--list"], capture_output=True, encoding="UTF-8")
    all_versions = cmd_output.stdout.split("\n")
    all_versions = [x.strip() for x in all_versions]
    all_versions = list(filter(lambda version: re.match(standard_version_regex, version), all_versions))

    if python_version == "latest":
        python_version = all_versions[-1]
    else:
        python_version = rf"^{python_version}"
        selected_versions = list(filter(lambda version: re.match(python_version, version), all_versions))
        python_version = selected_versions[-1]

    subprocess.run(["pyenv", "install", python_version])
    subprocess.run(["pyenv", "local", python_version])

    # Add Python version requirement to pyproject.toml for poetry since it can't be inferred from cookiecutter
    with pathlib.Path("pyproject.toml", "a").open() as config_file:
        config_file.write("\n\n[tool.poetry.dependencies]\n")
        config_file.write(f'python = "{python_version}"\n')

    if "{{ cookiecutter.create_git_repo }}" == "y":
        subprocess.run(["git", "init"])


def install_python_dependencies():
    """Install the starting Python packages and other standard development tools."""

    # Everything after here runs on the wrong version of Python - need to spawn a new shell?  Or at least run python
    #  again.
    # pyenv gets set correctly, but the old/initial version is still running
    # https://pythonspot.com/python-subprocess/
    # https://stackoverflow.com/questions/29523246/python-subprocess-is-running-a-different-version-of-python

    # subprocess.run(["pip", "install", "--upgrade", "pip"])
    # subprocess.run(["pip", "install", "poetry"])
    # subprocess.run(["poetry", "self", "add", "poetry-dotenv-plugin"])
    # subprocess.run(["poetry", "install"])

    # if "{{ cookiecutter.create_git_repo }}" == "y": # Change to look for .git directory instead?
    #     subprocess.run(["poetry", "run", "pre-commit", "install"])


if __name__ == "__main__":
    remove_unused_resources()
    install_python()
    install_python_dependencies()
