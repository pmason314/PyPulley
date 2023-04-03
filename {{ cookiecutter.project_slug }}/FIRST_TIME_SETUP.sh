echo $(pyenv which python)
$(pyenv which python) -m pip install --upgrade pip >/dev/null
$(pyenv which python) -m pip install poetry >/dev/null
$(pyenv which python) -m poetry self update >/dev/null
$(pyenv which python) -m poetry config virtualenvs.prefer-active-python true >/dev/null
$(pyenv which python) -m poetry env remove --all >/dev/null
$(pyenv which python) -m poetry self add poetry-dotenv-plugin >/dev/null
$(pyenv which python) -m poetry install --no-root

if [ -d ".git" ]; then
    $(pyenv which python) -m poetry run pre-commit install
fi

$(pyenv which python) poetry env use $(echo $PYENV_VERSION)
$(pyenv which python) -m poetry lock

rm -f FIRST_TIME_SETUP.sh
