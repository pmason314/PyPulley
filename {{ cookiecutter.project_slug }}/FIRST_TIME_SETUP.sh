$(pyenv which python) -m pip install --upgrade pip >/dev/null
$(pyenv which python) -m pip install pipx >/dev/null
$(pyenv which python) -m pipx reinstall poetry >/dev/null 2>&1
poetry config --local virtualenvs.prefer-active-python true >/dev/null
poetry config --local virtualenvs.in-project true >/dev/null
poetry self update >/dev/null
poetry self add poetry-dotenv-plugin >/dev/null
poetry add --lock --group dev black ruff pytest pytest-cov pytest-mock >/dev/null
{%- if cookiecutter.formatter == 'black' %}
poetry add --lock --group dev black blacken-docs >/dev/null
{%- endif %}
{%- if cookiecutter.create_git_repo == 'y' %}
poetry add --lock --group dev creosote pre-commit >/dev/null
{%- endif %}
{%- if cookiecutter.create_sphinx_docs == 'y' %}
poetry add --lock --group dev sphinx sphinx-rtd-theme >/dev/null
{%- endif %}
poetry install --no-root

if [ -d ".git" ]; then
    poetry run pre-commit install
fi

poetry env use $PYENV_VERSION
poetry lock >/dev/null
rm -f FIRST_TIME_SETUP.sh
