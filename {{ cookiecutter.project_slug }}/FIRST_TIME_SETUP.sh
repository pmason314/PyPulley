pip install --upgrade pip
pip install poetry
poetry env remove --all
poetry self add poetry-dotenv-plugin
poetry install

if [ -d ".git" ]; then
    poetry run pre-commit install
fi

poetry lock

rm -f FIRST_TIME_SETUP.sh
