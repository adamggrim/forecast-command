import json
import os
from typing import cast

from ._constants import (
    DATA_DIR_NAME,
    ZIP_CODE_TO_URL_MAP_FILE_NAME
)

# Get the directory of the current file.
file_dir: str = os.path.dirname(__file__)

# Construct a platform-independent path to the JSON file.
json_file_path: str = os.path.join(
    file_dir, DATA_DIR_NAME, ZIP_CODE_TO_URL_MAP_FILE_NAME
)

# Load the JSON data, which pairs each zip code with a forecast URL.
with open(json_file_path, 'r') as json_file:
    zip_code_to_url_map: dict[str, str] = cast(
        dict[str, str], json.load(json_file)
    )
