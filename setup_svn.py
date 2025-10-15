# setup.py

import os
import sys

def start_setup(base_dir="skatlaznet_svn"):
    """
    Creates the base directory and its required subdirectories.
    """
    print(f"--- Starting Setup for: {base_dir} ---")
    
    # List of directories to create inside the base_dir
    directories = [
        '_skatlaz__forks',
        '_skatlaz__postmail',
        '_skatlaz_talk',
        '_skatlaz_svn',
        '_skatlaz__auth',
        '_skatlaz__data',
        '_skatlaz__db',
        '_skatlaz__www',
        '_skatlaz_genai',
        '_skatlaz_software',
        '_skatlaz_office',
        '_config',
        '_policy',
        '_log',
        '_cash'
    ]
    
    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Created base directory: {base_dir}")
    else:
        print(f"Base directory already exists: {base_dir}")

    # Create subdirectories
    for d in directories:
        path = os.path.join(base_dir, d)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")
        else:
            print(f"Directory already exists: {path}")
    
    print("--- Setup Complete ---")

if __name__ == '__main__':
    # Execute setup to create the file structure
    start_setup()
