#!/bin/bash

# Navigate to your Sphinx project directory
# Uncomment and modify the next line if you want the script to change directories
# cd /path/to/your/sphinx/project

# Run make clean and make html
make clean && make html && python scripts/generate_team.py

echo "Sphinx documentation rebuilt successfully!"