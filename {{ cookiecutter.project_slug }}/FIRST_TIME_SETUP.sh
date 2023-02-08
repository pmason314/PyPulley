pip install --upgrade pip >/dev/null
pip install poetry >/dev/null
poetry self update >/dev/null
poetry config virtualenvs.prefer-active-python true >/dev/null
poetry env remove --all >/dev/null
poetry self add poetry-dotenv-plugin >/dev/null
poetry install

if [ -d ".git" ]; then
    poetry run pre-commit install
fi

poetry lock

rm -f FIRST_TIME_SETUP.sh
