# Config Manager

**A minimal terminal-based tool for managing your configuration files.**

---

## Features

- **List all configs** with grouping and colored output  
  ```bash
  config -n
  ```
- **Edit a config** in your preferred editor (defaults to `nvim`)  
  ```bash
  config <name>
  ```
- **Print the file path** by name  
  ```bash
  config -p <name>
  ```
- **Show file contents** on screen  
  ```bash
  config -c <name>
  ```
- **Add a new config** to the index (optional `group` and `command`):  
  ```bash
  config -a <name> <path> [group=<group>] [command="<shell command>"]
  ```
- **Delete configs**  
  - By name:  
    ```bash
    config -d name <name>
    ```  
  - By group (with confirmation):  
    ```bash
    config -d group <group>
    ```
- **Show help** for all commands:  
  ```bash
  config -h
  ```

---

## Requirements

- Python 3

---

## Script Configuration

At the top of `config.py` you can adjust:

- `CONFIG_PATH` — path to your `config.json`  
- `EDITOR` — editor command (default: `nvim`)  
- `saveall()` — backup function (Git, rsync, rclone, etc.)

```python
EDITOR      = "nvim"
CONFIG_PATH = "/home/seva/.config/scripts/config.json"

def saveall():
    # Example: run your backup script
    subprocess.Popen([
        "python3",
        "/home/seva/git/backup/my_configs/main.py"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
```

---

## Example `config.json` Structure

```json
{
  "fish": {
    "path": "/home/seva/.config/fish/config.fish",
    "group": "terminal",
    "command": ["fish", "-c", "source ~/.config/fish/config.fish"]
  },
  "kitty": {
    "path": "/home/seva/.config/kitty/kitty.conf",
    "group": "terminal",
    "command": ["sh", "-c", "kill -SIGUSR1 $(pgrep kitty)"]
  },
  "hyprland": {
    "path": "/home/seva/.config/hypr/hyprland.conf",
    "group": "hyprland",
    "command": ["hyprctl", "reload"]
  },
  "waybar": {
    "path": "/home/seva/.config/waybar/config",
    "group": "waybar",
    "command": ["pkill", "-SIGUSR1", "waybar"]
  },
  "nvim": {
    "path": "/home/seva/.config/nvim/init.lua",
    "group": "nvim"
  }
}
```

---

## TODO (WIP)

- TUI interface via `npyscreen`  
- Shell autocompletion for `bash`/`fish`  
- Export/import subsets of configs  
- Improved error messages and JSON validation  
- Hot-reload for groups like `nvim` upon change  
