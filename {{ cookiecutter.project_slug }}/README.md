# {{cookiecutter.project_name}}

## What is it?

Fill in an introduction and a description of your package here!


## Installation

Add installation instructions as needed.

## Usage

Provide motivating examples, various use cases, and anything else that would be helpful to a potential user.

## PyPulley Tools Reference (DELETE ME)

- Poetry:
  - [`poetry add {package}`](https://python-poetry.org/docs/cli/#add) - Add a required package or dev dependency to `pyproject.toml` and install it.
  - [`poetry shell`](https://python-poetry.org/docs/basic-usage#activating-the-virtual-environment) - Create a nested shell and activate the `poetry` virtual environment for the project.
  - [`poetry install`](https://python-poetry.org/docs/cli/#install) - Install all dependencies from the project's `pyproject.toml`.
  - [`poetry update`](https://python-poetry.org/docs/cli/#update) - Update all dependency versions where possible and update `poetry.lock` accordingly.
  - [`poetry show`](https://python-poetry.org/docs/cli/#show) - List all available packages in the virtual environment.
  - [`poetry build`](https://python-poetry.org/docs/cli/#build) - Build the package wheel.
  - [`poetry publish --build`](https://python-poetry.org/docs/cli/#publish) - Build and [publish](https://python-poetry.org/docs/repositories/#publishable-repositories) the project to a remote repository or index.
  - [`poetry version`](https://python-poetry.org/docs/cli/#version) - Show the current project version or bump the version of the project in `pyproject.toml`.
- Ruff:
  - [`ruff check {directory}`](https://github.com/charliermarsh/ruff#command-line-interface) - Run Ruff on the given files or directories.
  - TODO - Settings to set up to lint on save in VS Code
- Black:
  - [`black {directory}`](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#usage) - Run Black on the given file or directory.
- Pytest:
  - [`pytest {directory}`](https://docs.pytest.org/en/7.2.x/reference/reference.html#command-line-flags) - Run pytest on the given file or directory.

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}
{%- if cookiecutter.license in license_classifiers %}
## License

[{{cookiecutter.license}}](LICENSE)
{%- endif %}
