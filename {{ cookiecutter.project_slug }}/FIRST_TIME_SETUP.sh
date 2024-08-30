echo "Installing dev packages..."
uv add ruff ipykernel pytest --dev >/dev/null 2>&1
{%- if cookiecutter.create_git_repo == 'y' %}
uv add creosote pre-commit --dev >/dev/null 2>&1
{%- endif %}
{%- if cookiecutter.create_sphinx_docs == 'y' %}
uv add dev sphinx sphinx-rtd-theme --dev >/dev/null 2>&1
{%- endif %}

if [ -d ".git" ]; then
    uv run pre-commit install >/dev/null 2>&1
fi

cat config_template.toml >> pyproject.toml

rm -f FIRST_TIME_SETUP.sh
rm -f config_template.toml

echo "Done!  Project is ready at $(pwd)"
