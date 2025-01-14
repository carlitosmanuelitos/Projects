import json
import os
import hashlib
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
VERSION_TRACKER = "version_tracker.json"

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

def calculate_checksum(data):
    """Calculate a JSON data's checksum."""
    json_data = json.dumps(data, sort_keys=True)
    return hashlib.md5(json_data.encode()).hexdigest()

def get_current_version():
    """Get the current version from the version tracker."""
    version_data = load_json(VERSION_TRACKER)
    return version_data.get("version", "v0")

def increment_version(current_version):
    """Increment the semantic version."""
    parts = current_version[1:].split('.')
    if len(parts) == 1:
        return f"v{int(parts[0]) + 1}"
    parts[-1] = str(int(parts[-1]) + 1)
    return f"v{'.'.join(parts)}"

def update_version_tracker(new_version):
    """Update the version tracker with the new version."""
    save_json(VERSION_TRACKER, {"version": new_version})
    logging.info(f"Version tracker updated to: {new_version}")

def backup_version(data, version):
    """Backup the current data_artifacts.json file to version history."""
    backup_path = os.path.join(VERSION_HISTORY_DIR, f"data_artifacts_{version}.json")
    save_json(backup_path, data)
    logging.info(f"Version {version} saved to history.")

def merge_files():
    """Merge the source JSON files into a single file with metadata."""
    merged_data = {}
    for file_name in SOURCE_FILES:
        data = load_json(file_name)
        if data:
            merged_data.update(data)

    # Add metadata
    current_version = get_current_version()
    metadata = {
        "metadata": {
            "version": current_version,
            "last_updated": datetime.now().isoformat(),
            "source_checksums": {file: calculate_checksum(load_json(file)) for file in SOURCE_FILES}
        }
    }
    merged_data.update(metadata)

    # Check for changes
    existing_data = load_json(MERGED_FILE)
    if calculate_checksum(existing_data) != calculate_checksum(merged_data):
        # Increment version, update version tracker, and save
        new_version = increment_version(current_version)
        update_version_tracker(new_version)
        merged_data["metadata"]["version"] = new_version

        backup_version(merged_data, new_version)
        save_json(MERGED_FILE, merged_data)
        logging.info(f"Merged data updated and saved with version {new_version}.")
    else:
        logging.info("No changes detected in source files. Skipping save.")

if __name__ == "__main__":
    merge_files()
