# Lib5K Project Template [![CookieCutter Template](https://img.shields.io/badge/cookiecutter-template-blue)](https://github.com/cookiecutter/cookiecutter)
This is a [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template repository for quickly creating [@frc5024](https://github.com/frc5024) [Lib5K](https://github.com/frc5024/lib5k)-based robot projects.

## Usage

```sh
# Install cookiecutter
python3 -m pip install cookiecutter

# Go to workspace directory
cd /path/to/workspace

# Create a new project folder
# You will be prompted to configure the project settings by this command
cookiecutter gh:ewpratten/template-lib5k

# Enter and build project
cd ./<robot_name>
./gradlew build
```
