# Battletanks

Battletanks is written in Python and uses the Pygame Community Edition game library.

So far, Battletanks has only been built and tested on Linux.

## Building from source

### Requirements

* [uv](https://docs.astral.sh/uv/)
* Git

### Running

1. Clone Battletanks: `git clone https://github.com/DamareonC/battletanks`
2. Move to Battletanks directory: `cd battletanks`
3. Run Battletanks: `uv run src/main.py`*

*To just set up for building from source, run `uv sync`

### Building from source

* Follow the steps under [Running](#running)
* Enter the virtual environment: `source .venv/bin/activate` (Mac/Linux with zsh/bash) or `.venv\Scripts\activate` (Windows with PowerShell)
* Build Battletanks: `pyinstaller --onefile src/main.py --name battletanks`

To exit the virtual environment, run `deactivate`