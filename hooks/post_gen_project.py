"""Post-project-creation hooks.

After successfully creating the cookiecutter and validating it with the pre-generation hooks, set up the new project
 environment by installing Python, Poetry, and other dev dependencies.
"""

import logging
import os
import shutil
import subprocess
import sys
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

logging.basicConfig(stream=sys.stdout, format="%(message)s", level=logging.INFO)
logger = logging.getLogger()


def install_python() -> None:
    """Figure out and install the specified version of Python.

    Returns:
        int: specific Python version selected for the project
    """
    python_version = "{{ cookiecutter.python_version }}"

    # Install and update uv
    try:
        subprocess.run("uv self update", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
    except subprocess.CalledProcessError:
        logger.info("Installing uv...")
        subprocess.run(
            "curl -LsSf https://astral.sh/uv/install.sh | sh", shell=True, stdout=subprocess.DEVNULL, check=True
        )

    if python_version == "latest":
        python_version = subprocess.run(
            "uv python list | head -n 5 | grep -v 'rc' | head -n 1 | awk '{print $1;}'",
            capture_output=True,
            text=True,
            shell=True,
            check=True,
        )
        python_version = python_version.stdout.strip()

    subprocess.run(["uv", "init", "--python", python_version, "--python-preference", "only-managed"], check=True)
    subprocess.run(["uv", "venv", "--python", python_version, "--python-preference", "only-managed"], check=True)

    if "{{ cookiecutter.create_git_repo }}" == "y":
        subprocess.run(["git", "init"], stdout=subprocess.DEVNULL, check=True)


def remove_unused_resources() -> None:
    """Delete unused files and directories related to declined template configuration options."""
    Path.unlink(Path(PROJECT_DIRECTORY) / "hello.py")

    if "{{ cookiecutter.license }}" == "Not Open Source":
        Path.unlink(Path(PROJECT_DIRECTORY) / "LICENSE")

    if "{{ cookiecutter.create_git_repo }}" == "n":
        Path.unlink(Path(PROJECT_DIRECTORY) / ".gitignore")
        Path.unlink(Path(PROJECT_DIRECTORY) / ".pre-commit-config.yaml")
        shutil.rmtree(Path(PROJECT_DIRECTORY) / ".github")

    if "{{ cookiecutter.create_sphinx_docs }}" == "n":
        shutil.rmtree(Path(PROJECT_DIRECTORY) / "docs")


def add_pyproject_details() -> None:
    """Add project details to the pyproject.toml file."""
    if "{{ cookiecutter.license }}" == "MIT License":
        license_classifier = "MIT License: License :: OSI Approved :: MIT License"
    elif "{{ cookiecutter.license }}" == "BSD License":
        license_classifier = "BSD License: License :: OSI Approved :: BSD License"
    elif "{{ cookiecutter.license }}" == "Apache License 2.0":
        license_classifier = "Apache Software License 2.0: License :: OSI Approved :: Apache Software License"
    elif "{{ cookiecutter.license }}" == "GNU General Public License v3":
        license_classifier = (
            "GNU General Public License v3: License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        )

    project_license = "{{ cookiecutter.license }}"
    pyproject_path = Path(PROJECT_DIRECTORY) / "pyproject.toml"
    email = subprocess.run(["git", "config", "--get", "user.email"], capture_output=True, text=True, check=True)
    email = email.stdout.strip()
    author = "{{ cookiecutter.author }}"
    author_line = '{ name = "' + author + '", email = "' + email + '" },'

    with pyproject_path.open("r") as file:
        lines = file.readlines()

    with pyproject_path.open("w") as file:
        for line in lines:
            file.write(line)
            if line.strip().startswith("readme = "):
                if project_license != "Not Open Source":
                    file.write("license = { text = " + f'"{project_license}"' + " }\n")
                file.write("authors = [\n")
                file.write(f"    {author_line}\n")
                file.write("]\n")
                file.write("classifiers = [\n")
                file.write(f'    "{license_classifier}",\n')
                file.write('    "Programming Language :: Python :: 3",\n')
                file.write('    "Natural Language :: English",\n')
                file.write("]\n")

            elif line.strip().startswith("requires-python"):
                file.write("\n")
        file.write("\n[tool.uv]\n")
        file.write("package = true\n")


if __name__ == "__main__":
    project_python_version = install_python()
    remove_unused_resources()
    add_pyproject_details()
    subprocess.run(["sh", "FIRST_TIME_SETUP.sh"], check=True)
