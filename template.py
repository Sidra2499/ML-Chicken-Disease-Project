import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init_.py",  
    f"src/{project_name}/components/_init_.py",  
    f"src/{project_name}/utils/_init_.py", 
    f"src/{project_name}/config/_init_.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/_init_.py", 
    f"src/{project_name}/entity/_init_.py", 
    f"src/{project_name}/constants/_init_.py", 
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    # suppose you want to add more files just add it below
    "test.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file: {filename}")

    if(not os.path.exists(filename)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating Empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
