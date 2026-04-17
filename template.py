import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

list_of_file = [
    '.github/workfows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.yaml",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name

    # if filedir != "":
    #     os.makedirs(filedir, exist_ok=True)
    #     logging.info(f"Creating directory: {filedir} for the file: {filename}")
    filedir.mkdir(parents=True, exist_ok=True)
    logging.info(f"Creating directory {filedir} for the file {filename}")

    
    # if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    #     with open(filepath, 'w') as f:
    #         pass
    #         logging.info(f"Creating empty file: {filepath}")
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")