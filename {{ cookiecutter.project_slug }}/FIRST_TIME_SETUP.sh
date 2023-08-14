$(pyenv which python) -m pip install --upgrade pip >/dev/null
$(pyenv which python) -m pip install pipx pip >/dev/null
$(pyenv which python) -m pipx install poetry >/dev/null
$(pyenv which python) -m pipx upgrade poetry >/dev/null
$(pyenv which python) -m poetry config virtualenvs.prefer-active-python true >/dev/null
$(pyenv which python) -m poetry config --local virtualenvs.in-project true >/dev/null
$(pyenv which python) -m poetry self update >/dev/null
$(pyenv which python) -m poetry self add poetry-dotenv-plugin >/dev/null
$(pyenv which python) -m poetry install --no-root

if [ -d ".git" ]; then
    $(pyenv which python) -m poetry run pre-commit install
fi

$(pyenv which python) poetry env use $PYENV_VERSION
$(pyenv which python) -m poetry lock

rm -f FIRST_TIME_SETUP.sh
