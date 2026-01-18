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

def get_modules():
    """Get list of available modules."""
    modules_file = os.path.join(DATA_DIR, "modules.json")
    if os.path.exists(modules_file):
        with open(modules_file, "r") as f:
            return json.load(f)
    return {"general": [], "application": []}

def get_workspaces():
    """Get list of workspaces."""
    workspaces_file = os.path.join(DATA_DIR, "workspaces.json")
    if os.path.exists(workspaces_file):
        with open(workspaces_file, "r") as f:
            return json.load(f)
    return []

def add_workspace(workspace_data):
    """Add a new workspace."""
    workspaces_file = os.path.join(DATA_DIR, "workspaces.json")
    workspaces = get_workspaces()
    workspaces.append(workspace_data)
    with open(workspaces_file, "w") as f:
        json.dump(workspaces, f, indent=4)
    return workspace_data
