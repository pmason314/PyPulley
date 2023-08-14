$(pyenv which python) -m pip install --upgrade pip >/dev/null
$(pyenv which python) -m pip install pipx >/dev/null
$(pyenv which python) -m pipx reinstall poetry >/dev/null
poetry config --local virtualenvs.prefer-active-python true >/dev/null
poetry config --local virtualenvs.in-project true >/dev/null
poetry self update >/dev/null
poetry self add poetry-dotenv-plugin >/dev/null
poetry install --no-root

if [ -d ".git" ]; then
    poetry run pre-commit install
fi

poetry env use $PYENV_VERSION
poetry lock
rm -f FIRST_TIME_SETUP.sh
