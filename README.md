# Config Manager

**A minimal terminal-based tool for managing user configuration files.**

## Features

This script provides a convenient interface for working with personal configuration files:

* Interactive selection of configs via TUI
* Editing files in your preferred editor
* Quick access to file paths by name
* Viewing file contents
* Adding new config entries to a JSON index

## Requirements

Only one Python library is required:

```bash
pip install npyscreen
```

## Setup

1. Create a `config.json` file containing your config names and their absolute paths:

```json
{
  "nvim": "/home/seva/.config/nvim/init.lua",
  "waybar": "/home/seva/.config/waybar/config"
}
```

2. In the script, adjust the following variables if needed:

* `CONFIG_PATH` — path to your `config.json`
* `EDITOR` — editor used to open files (defaults to `nvim`)
* `saveall()` function — by default **commented out**. You can insert any backup mechanism there (e.g., `git`, `rsync`, `rclone`, etc.).

Example:

```python
def saveall():
    subprocess.Popen([
        "python3",
        "/home/seva/git/backup/my_configs/main.py"
    ])
```

Replace the content with your own backup logic or leave it commented out.

## Usage

```bash
# Launch TUI interface:
./config.py

# Print path to config:
./config.py -p <name>

# Show file content:
./config.py -c <name>

# Add a new config:
./config.py -a <name> <path>

# List all config names:
./config.py -n

# Show help:
./config.py -h
```

