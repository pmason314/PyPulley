"""
Post-project-creation hooks.

After successfully creating the cookiecutter and validating it with the pre-generation hooks, set up the new project
 environment by installing Python, Poetry, and other dev dependencies.
"""

import logging
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DEPENDENCY_LINE = 18  # Where to insert the tool.poetry.dependencies section of pyproject.toml

logging.basicConfig(stream=sys.stdout, format="%(message)s", level=logging.INFO)
logger = logging.getLogger()


def remove_unused_resources() -> None:
    """Delete unused files and directories related to declined template configuration options."""
    if "{{ cookiecutter.license }}" == "Not Open Source":
        Path.unlink(Path(PROJECT_DIRECTORY) / "LICENSE")

    if "{{ cookiecutter.create_git_repo }}" == "n":
        Path.unlink(Path(PROJECT_DIRECTORY) / ".pre-commit-config.yaml")

    if "{{ cookiecutter.create_sphinx_docs }}" == "n":
        shutil.rmtree(Path(PROJECT_DIRECTORY) / "docs")


def install_python() -> str:
    """
    Figure out and install the specified version of Python.

    Returns:
        int: specific Python version selected for the project
    """
    python_version = "{{ cookiecutter.python_version }}"
    standard_version_regex = r"^3.[0-9]+.[0-9]+$"

    # Make sure the most recent Python versions are available to pyenv
    logger.info("Updating pyenv...")
    subprocess.run(["pyenv", "update"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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

    # Skip installation if version already exists
    logger.info(f"Installing Python {python_version}...")
    subprocess.run(["pyenv", "install", python_version, "-s"], stdout=subprocess.DEVNULL)
    subprocess.run(["pyenv", "local", python_version])

    # Add Python version requirement to pyproject.toml for poetry since it can't be inferred from cookiecutter
    with Path("pyproject.toml").open() as config_file:
        contents = config_file.readlines()
        contents.insert(DEPENDENCY_LINE, f'python = "~{python_version}"\n')

    with Path("pyproject.toml").open("w") as config_file:
        config_file.writelines(contents)

    # Install dev dependencies

    if "{{ cookiecutter.create_git_repo }}" == "y":
        logger.info("Creating git repository...")
        subprocess.run(["git", "init"], stdout=subprocess.DEVNULL)

    return python_version


def install_python_dependencies(python_version: str) -> None:
    """Install all tools and frameworks with a specific version of Python."""
    # Set the PYENV_VERSION environment variable so it can be used by the setup script, then unset it after
    os.environ["PYENV_VERSION"] = python_version
    logger.info("Installing poetry...")
    subprocess.run(["sh", "FIRST_TIME_SETUP.sh"])
    del os.environ["PYENV_VERSION"]


if __name__ == "__main__":
    remove_unused_resources()
    project_python_version = install_python()
    install_python_dependencies(project_python_version)
