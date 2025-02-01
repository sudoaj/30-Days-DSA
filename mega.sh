#!/bin/bash

# Output notebook filename
OUTPUT_FILE="merged_notebooks.ipynb"

# Temporary file to store merged content
TEMP_FILE="temp_notebooks.json"

# Start with an empty Jupyter notebook structure
echo '{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}' > "$TEMP_FILE"

# Function to append a notebook to the merged notebook
append_notebook() {
    local file="$1"
    
    # Add a Markdown header with the filename
    jq --arg name "$file" '.cells += [{"cell_type": "markdown", "metadata": {}, "source": ["# " + $name], "outputs": []}]' "$TEMP_FILE" > temp.json && mv temp.json "$TEMP_FILE"

    # Merge notebook content
    jq '.cells' "$file" | jq -c '.[]' | while read -r cell; do
        jq --argjson new_cell "$cell" '.cells += [$new_cell]' "$TEMP_FILE" > temp.json && mv temp.json "$TEMP_FILE"
    done
}

# Find and merge all notebooks recursively from subdirectories
find . -type f -name "00*.ipynb" | sort | while read -r notebook; do
    echo "Merging: $notebook"
    append_notebook "$notebook"
done

# Save the final output
jq '.' "$TEMP_FILE" > "$OUTPUT_FILE"
rm "$TEMP_FILE"

echo "Merged notebook saved as $OUTPUT_FILE"