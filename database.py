import os
import json

DATA_DIR = "data"
CONFIG_FILE = "data/config.json"

def init_db():
    """Ensure the data directory exists."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        print(f"Created data directory at {DATA_DIR}")

def get_config():
    """Read the configuration file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None

def create_config(username):
    """Create the configuration file with the username."""
    config = {"username": username}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)
    return config
