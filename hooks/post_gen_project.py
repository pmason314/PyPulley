import os
import subprocess
import re

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def install_python_and_deps():
    python_version =  "{{ cookiecutter.python_version }}"
    if python_version == "latest":
        standard_version_regex =  r"^3.[0-9]+.[0-9]+$"
        subprocess.run(["pyenv", "update"]) # Make sure most recent Python versions are accessible
        cmd_output = subprocess.run(["pyenv", "install", "--list"], capture_output=True, encoding="UTF-8")
        all_versions = cmd_output.stdout.split("\n")
        all_versions = map(lambda x: x.strip(), all_versions)
        all_versions = list(filter(lambda version: re.match(standard_version_regex, version), all_versions))
        python_version = all_versions[-1]

    subprocess.run(["pyenv", "install", f"{python_version}"])
    subprocess.run(["pyenv", "local", f"{python_version}"])
    subprocess.run(["pip", "install", "--upgrade", "pip"])
    subprocess.run(["pip", "install", "poetry"])
    subprocess.run(["poetry", "install"])
    subprocess.run(["git", "init"])



if __name__ == "__main__":
    if "{{ cookiecutter.license }}" == "Not Open Source":
        remove_file("LICENSE")
    install_python_and_deps()

