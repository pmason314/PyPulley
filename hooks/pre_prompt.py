"""Cookiecutter hooks that get run before the user enters their prompt responses."""

import json
import subprocess
from pathlib import Path


def add_username_to_cc_dict() -> None:
    """Get the username of the current user."""
    author = subprocess.run(["git", "config", "--get", "user.name"], capture_output=True, text=True, check=True)
    author = author.stdout.strip()

    # Load the cookiecutter context from cookiecutter.json
    with Path("cookiecutter.json").open() as f:
        cookiecutter_context = json.load(f)

    # Update the cookiecutter context with the author
    cookiecutter_context["author"] = author

    # Save the updated context back to cookiecutter.json
    with Path("cookiecutter.json").open("w") as f:
        json.dump(cookiecutter_context, f, indent=4)


if __name__ == "__main__":
    add_username_to_cc_dict()
