import json
import os

# Get the directory of the current file.
file_dir: str = os.path.dirname(__file__)

# Construct a platform-independent path to the JSON file.
json_file_path: str = os.path.join(
    file_dir, 'data', 'zip_code_url_map.json'
)

# Load the JSON data, which pairs a forecast URL with each zip code.
with open(json_file_path, 'r') as json_file:
    zip_code_to_url_map: dict[str, str] = json.load(json_file)
