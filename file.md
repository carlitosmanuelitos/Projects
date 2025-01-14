import json
import os
import hashlib
import shutil
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    filename='data_artifact.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants
SOURCE_FILES = ["api_documentation.json", "physical_data_model.json", "reference_data.json"]
MERGED_FILE = "data_artifacts.json"
VERSION_HISTORY_DIR = "version_history/"

# Ensure version history directory exists
os.makedirs(VERSION_HISTORY_DIR, exist_ok=True)

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load {file_path}: {e}")
        return {}

def save_json(file_path, data):
    """Save JSON data to a file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"File saved: {file_path}")
    except Exception as e:
        logging.error(f"Failed to save {file_path}: {e}")

def calculate_checksum(file_path):
    """Calculate a file's checksum."""
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception as e:
        logging.error(f"Failed to calculate checksum for {file_path}: {e}")
        return None

def backup_current_version():
    """Backup the current data_artifacts.json file to version history."""
    if os.path.exists(MERGED_FILE):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(VERSION_HISTORY_DIR, f"data_artifacts_{timestamp}.json")
        try:
            shutil.copy(MERGED_FILE, backup_path)
            logging.info(f"Version backed up: {backup_path}")
        except Exception as e:
            logging.error(f"Failed to backup version: {e}")

def merge_files():
    """Merge the source JSON files into a single file."""
    merged_data = {}
    for file_name in SOURCE_FILES:
        data = load_json(file_name)
        if data:
            merged_data.update(data)

    # Save the merged file and create a backup if changes are detected
    current_checksum = calculate_checksum(MERGED_FILE)
    new_data_json = json.dumps(merged_data, sort_keys=True)
    new_checksum = hashlib.md5(new_data_json.encode()).hexdigest()

    if current_checksum != new_checksum:
        backup_current_version()
        save_json(MERGED_FILE, merged_data)
        logging.info("Merged data updated and saved.")
    else:
        logging.info("No changes detected in source files.")

if __name__ == "__main__":
    merge_files()
