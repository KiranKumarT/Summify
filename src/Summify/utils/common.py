import os
from box.exceptions import BoxValueError
import yaml
from Summify.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path (Path): The path to the yaml file.

    Raises:
        BoxValueError: If the yaml file is invalid.
        e: invalid yaml file.

    Returns:
        ConfigBox: A ConfigBox object.
    """

    try:
        with open(path, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path} loaded successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise BoxValueError(f"Invalid yaml file {path}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories.

    Args:
        path_to_directories (list): A list of directories.
        verbose (bool, optional): Whether or not to print the directories that were created. Defaults to True.
    """
    for directory in path_to_directories:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            if verbose:
                logger.info(f"Directory {directory} created successfully")

@ensure_annotations
def  get_size(path: Path) -> str:
    """
    Gets the size of a file.

    Args:
        path (Path): The path to the file.

    Returns:
    str: The size of the file.
    """

    size_in_kb = round(os.path.getsize(path)/1024)

    return f"~ {size_in_kb} kb"
