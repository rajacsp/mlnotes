
import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

# Directories
NOTEBOOK_DIR = "./notebooks"  # Directory containing .ipynb files
OUTPUT_DIR = "./content"     # Directory for .md files (Pelican content directory)

# Step 1: Convert notebooks to Markdown recursively
def convert_notebooks_to_markdown(notebook_dir, output_dir):
    notebook_dir = Path(notebook_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for notebook in notebook_dir.rglob("*.ipynb"):  # Recursively find .ipynb files
        # Skip hidden directories like .ipynb_checkpoints
        if any(part.startswith('.') for part in notebook.parts):
            print(f"Skipping hidden folder or file: {notebook}")
            continue

        print(f"Converting {notebook} to markdown...")
        # Determine relative path for content organization
        relative_path = notebook.relative_to(notebook_dir)
        output_subdir = output_dir / relative_path.parent
        output_subdir.mkdir(parents=True, exist_ok=True)

        # Convert notebook to markdown
        cmd = [
            "jupyter",
            "nbconvert",
            "--to",
            "markdown",
            "--output-dir",
            str(output_subdir),
            str(notebook),
        ]
        subprocess.run(cmd, check=True)

        # Count cells in the notebook
        cell_count = count_cells_in_notebook(notebook)
        score = calculate_score(cell_count)

        # Add metadata to the generated Markdown file
        # Add metadata and cell count to the Markdown file
        md_file = output_subdir / f"{notebook.stem}.md"
        add_metadata_to_markdown(md_file, cell_count, score)

def calculate_score(cell_count):
    """
    Calculate the score based on the number of cells.
    For every 5 cells, add 5 points. Score starts at 0 if less than 5 cells.
    """
    if cell_count < 5:
        return 0
    return (cell_count // 5) * 5

def count_cells_in_notebook(notebook_path):
    """
    Count the number of cells in the .ipynb file.
    """
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_data = json.load(f)
    # Count the cells in the notebook
    return len(notebook_data.get("cells", []))

# Step 2: Add metadata to Markdown
def add_metadata_to_markdown(markdown_file, cell_count, score):
    """
    Add metadata and the cell count to the .md file.
    """

    # Read the current content of the Markdown file
    with open(markdown_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Get file modification time and format it as YYYY-MM-DD
    file_mtime = datetime.fromtimestamp(Path(markdown_file).stat().st_mtime)
    formatted_date = file_mtime.strftime("%Y-%m-%d")

    metadata = f"""---
title: {markdown_file.stem.replace('_', ' ').title()}
date: {formatted_date}
author: Your Name
cell_count: {cell_count}
score: {score}
---
"""

    # Append cell count information at the end of the file
    # cell_info = f"\n\n---\n**This notebook contains {cell_count} cells.**\n"

    # Append score information at the end of the file
    score_info = f"\n\n---\n**Score: {score}**\n"

    print(f"Adding metadata and cell count to {markdown_file}...")
    with open(markdown_file, "w", encoding="utf-8") as f:
        f.write(metadata + "\n" + content + score_info)

# Step 3: Generate site with Pelican
def generate_site_with_pelican(content_dir):
    print("Generating site with Pelican...")
    cmd = ["pelican", str(content_dir)]
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    # Ensure required directories exist
    Path(NOTEBOOK_DIR).mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    # Convert notebooks and generate site
    convert_notebooks_to_markdown(NOTEBOOK_DIR, OUTPUT_DIR)
    generate_site_with_pelican(OUTPUT_DIR)

    print("Site generated successfully!")
