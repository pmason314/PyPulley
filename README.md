# PyPulley

## What Is It?

PyPulley is a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for quickly creating new Python packages or projects. By running a single shell command, you can have dependency management and Python version management in place, linting, formatting, and pre-commit hooks configured, and more.

PyPulley bundles its set of tools and frameworks in an opinionated fashion based on ease of use, and performance, and general best practices. Many of these defaults can be changed as desired.

### TODO - Include screenshot of configuration options

## Table of Contents

- [**Main Features**](#main-features)
  - [Python Versioning](#python-versioning---pyenv)
  - [Dependency Management](#dependency-management---poetry)
  - [Linting](#linting---ruff)
  - [Formatting](#formatting---black)
  - [Unit Testing](#unit-testing---pytest)
  - [Version Control](#version-control---git-and-pre-commit)
  - [Documentation](#documentation---sphinx)
  - [Publishing](#publishing---poetry)
- [**Installation**](#installation)
  - [Prerequisites](#prerequisites)
  - [Installing PyPulley](#installing-pypulley)
- [**Usage**](#usage)
- [**License**](#license)

## Main Features

PyPulley installs all of the following development tools, packages, and frameworks. Alternatives are listed where applicable.

- ### Python Versioning - [**pyenv**](https://github.com/pyenv/pyenv)
  PyPulley will prompt for a version of Python, then use pyenv to install said version. Version numbers can be given as major (e.g. `3`), minor (e.g. `3.10`), patch (e.g. `3.10.9`), or simply `latest` for the most recent stable version of CPython.
- ### Dependency Management - [**Poetry**](https://python-poetry.org/)
  PyPulley prefers Poetry for dependency management in Python-only or Python-majority projects. Poetry's ability to easily create isolated virtual environments and track dependency requirements make it a fantastic choice for setting up new packages. Also included is **poetry-dotenv-plugin**, a small plugin for Poetry that makes local environment variables easily definable and accessible at runtime via a `.env` file.
- ### Linting - [**Ruff**](https://github.com/charliermarsh/ruff)
  Ruff is a relatively new Python linter with the same functionality of flake8, isort, pydocstyle, pyupgrade and other tools combined, all while running orders of magnitude faster than any of them. Ruff is highly configurable as well, making it a flexible choice for any Python project.
- ### Formatting - [**Black**](https://black.readthedocs.io/en/stable/)
  The most popular and most uncompromising Python code formatter. PyPulley agrees with the core premise of Black - consistency across a code base allows everyone to focus on more important matters than which manually-formatted choice is prettier.
- ### Unit Testing - [**pytest**](https://docs.pytest.org/en/latest/)
  pytest - Despite unittest coming included in the standard library, PyPulley believes pytest offers more concise, readable, and reusable tests. Throw in a couple plugins like pytest-mock and pytest-cov for mocking and coverage analysis respectively, and pytest is an extremely powerful testing framework.
- ### Version Control - [**git**](https://git-scm.com/about) and [**pre-commit**](https://pre-commit.com/)
  The overwhelmingly popular choice for version control. PyPulley initializes new projects as git repositories and includes a set of default pre-commit hooks as well.
- ### Documentation - [**Sphinx**](https://www.sphinx-doc.org/en/master/)
  Quoting its own tag line, Sphinx makes it easy to create intelligent and beautiful documentation. PyPulley comes with an optional Sphinx skeleton to enable quick HTML or Markdown documentation, as well as the autodoc extension configured to automatically pull out function docstrings into documentation.
- ### Publishing - [**Poetry**](https://python-poetry.org/)
  Poetry comes back with functionality to version packages, build them from a pyproject.toml file (the yet-unofficial successor to setup.py), and publish them to PyPI or other indexes.

## Installation

### Prerequisites

The sole prerequisite for PyPulley is having [pyenv](https://github.com/pyenv/pyenv) installed for Python version management.

Most of the time pyenv can be installed via either:

- **Automatic Installer:**
  ```sh
  curl https://pyenv.run | bash
  ```
- **Homebrew (Mac OS X):**
  `sh
brew update
brew install pyenv
`
  `See pyenv's [Suggested Build Environment](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) if you encounter any problems. Also note that pyenv on Windows (and therefore PyPulley) is only supported through [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/about).

### Installing PyPulley

Install Pypulley from PyPI using pip:

```sh
pip install pypulley
```

## Usage

Simply run the PyPulley cookiecutter and configure your package by selecting your desired options:

```sh
cookiecutter pypulley
```

Once pyenv installs the select version of Python and the directory structure has been created, run the first-time setup script to finish the dependency installation.

```sh
cd {package-name}
sh FIRST_TIME_SETUP.sh
```

### TODO - Include terminal recording gif here

Now you're ready to go! Below are some selected options and commands from the default set of tools that may be useful.

### TODO - fill out command descriptions

- Poetry:
  - poetry add {package}
  - poetry shell
  - poetry install
  - poetry update
  - poetry show
  - poetry build
  - poetry publish --build
  - poetry version
- Ruff:
  - ruff check
  - Settings to set up to lint on save in VS Code
- Black:
  - black {directory}
- Pytest:
  - pytest {optional directory}

## License

[MIT License](LICENSE)
