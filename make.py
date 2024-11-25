

# pylint: disable=missing-function-docstring, invalid-name

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime
import shutil
import random

# Local
# import custom_constants as cons

from git import Repo

# Get the current repository name dynamically
repo = Repo(os.getcwd())
FOLDER_NAME = os.path.basename(repo.working_dir)

# Directories
NOTEBOOK_DIR        = "./notebooks"  # Directory containing .ipynb files
OUTPUT_DIR          = "./content"     # Directory for .md files (Pelican content directory)
DOCS_FOLDER         = "./docs"
GLOBAL_IMAGES_DIR   = os.path.join(OUTPUT_DIR, "images")  # Central images directory

def is_recently_modified(source_file, target_file):
    """
    Check if the source file is more recent than the target file.
    Returns True if the source file is new or has been modified.
    """
    if not target_file.exists():
        # If the target file doesn't exist, the source is considered new
        return True
    return source_file.stat().st_mtime > target_file.stat().st_mtime

# Step 1: Convert notebooks to Markdown recursively
def convert_notebooks_to_markdown(notebook_dir, output_dir, fresh = False):
    notebook_dir = Path(notebook_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    slugs = set()  # Track slugs to ensure uniqueness

    for notebook in notebook_dir.rglob("*.ipynb"):  # Recursively find .ipynb files
        # Skip hidden directories like .ipynb_checkpoints
        if any(part.startswith('.') for part in notebook.parts):
            # print(f"Skipping hidden folder or file: {notebook}")
            continue

        # Determine relative path for content organization
        print(f"Converting {notebook} to markdown...")
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

         # Get the generated Markdown file path
        md_file = output_subdir / f"{notebook.stem}.md"

        # Skip if not recently modified
        if not fresh:
            if not is_recently_modified(notebook, md_file):
            #     # print(f"Skipping {notebook}: No changes detected.")
                continue

        # Ensure unique slug (filename)
        new_md_file = ensure_unique_slug(md_file, slugs)

        # print(f"Converting {notebook} to markdown...")

        # Convert notebook to markdown
        # cmd = [
        #     "jupyter",
        #     "nbconvert",
        #     "--to",
        #     "markdown",
        #     "--output-dir",
        #     str(output_subdir),
        #     str(notebook),
        # ]
        # subprocess.run(cmd, check=True)

        # Count cells in the notebook
        cell_count = count_cells_in_notebook(notebook)
        score = calculate_score(cell_count)

        # Add metadata to the generated Markdown file
        # Add metadata and cell count to the Markdown file

        add_metadata_to_markdown(new_md_file, cell_count, score)

        # Update image references in Markdown
        update_image_references(new_md_file)

def ensure_unique_slug(md_file, slugs):
    """
    Ensure the filename (slug) is unique by renaming if necessary.
    """
    slug = md_file.stem
    new_md_file = md_file

    while slug in slugs:
        # Generate a new slug with a random 4-digit number
        slug = f"{md_file.stem}-{random.randint(1000, 9999)}"
        new_md_file = md_file.with_name(f"{slug}.md")

    # If the file was renamed, perform the renaming
    if new_md_file != md_file:
        os.rename(md_file, new_md_file)
        print(f"Renamed {md_file.name} to {new_md_file.name}")

    # Add the slug to the set of slugs
    slugs.add(slug)
    return new_md_file

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

# New Step: Copy all images to the global images directory
def copy_images_to_global_folder(content_dir, global_images_dir):
    """
    Scan the content directory for image files and copy them to the global images directory.
    """
    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".webp"}
    global_images_dir = Path(global_images_dir)
    global_images_dir.mkdir(parents=True, exist_ok=True)

    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.lower().endswith(tuple(image_extensions)):
                source = Path(root) / file
                target = global_images_dir / file
                if not target.exists():  # Avoid overwriting existing files
                    shutil.copy2(source, target)
                    print(f"Copied: {source} -> {target}")

# Step 3: Resolve Duplicate Slugs
def resolve_duplicate_slugs(content_dir):
    """
    Detect and resolve duplicate slugs in Markdown files by appending a random 4-digit number.
    """
    slugs = {}
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                filepath = Path(root) / file
                slug = filepath.stem  # Use the filename without the extension as the slug

                # Read the file to confirm the slug in metadata
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.readlines()

                # Find and validate the slug in the metadata
                for i, line in enumerate(content):
                    if line.strip().startswith("slug:"):
                        file_slug = line.strip().split(":", 1)[1].strip()
                        if file_slug != slug:
                            slug = file_slug
                        break

                # If slug is already seen, rename the file and update the slug in metadata
                if slug in slugs:
                    new_slug = f"{slug}-{random.randint(1000, 9999)}"
                    new_filename = f"{new_slug}.md"
                    new_filepath = filepath.parent / new_filename

                    # Rename the file
                    os.rename(filepath, new_filepath)

                    # Update the slug inside the .md file
                    for i, line in enumerate(content):
                        if line.strip().startswith("slug:"):
                            content[i] = f"slug: {new_slug}\n"
                            break
                    with open(new_filepath, "w", encoding="utf-8") as f:
                        f.writelines(content)

                    print(f"Renamed {file} to {new_filename} and updated slug.")
                else:
                    slugs[slug] = filepath

# Step 4: Update image references in Markdown
def update_image_references(markdown_file):
    """
    Update image references in the Markdown file to point to the global 'images' folder.
    Replaces paths like 'two_files/two_0_0.png' with 'images/two_0_0.png'.
    """
    with open(markdown_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Process each line and replace image paths
    updated_content = []
    for line in content.splitlines():
        if "![png](" in line:  # Look for image references
            # Extract the current image path
            start_idx = line.find("![png](") + len("![png](")
            end_idx = line.find(")", start_idx)
            current_path = line[start_idx:end_idx]

            # Get the image filename only (strip subdirectories)
            file_name = current_path.split("/")[-1]

            # Update to the global 'images' directory
            new_path = f"/{FOLDER_NAME}/images/{file_name}"
            line = line.replace(current_path, new_path)

        updated_content.append(line)

    # Write back the updated content to the file
    with open(markdown_file, "w", encoding="utf-8") as f:
        f.write("\n".join(updated_content))

# Step 3: Generate site with Pelican
def generate_site_with_pelican(content_dir):
    print("Generating site with Pelican...")
    cmd = ["pelican", str(content_dir)]
    subprocess.run(cmd, check=True)

# def clean_output_dir(output_dir, unlink = False):
#     """
#     Clean the output directory before generating the site.
#     """
#     output_path = Path(output_dir)
#     if output_path.exists():
#         for file in output_path.glob("**/*"):
#             if file.is_file():
#                 file.unlink()
#             elif file.is_dir():
#                 if unlink:
#                     for sub_file in file.glob("**/*"):
#                         sub_file.unlink()
#                 file.rmdir()
#         print(f"Cleaned the output directory: {output_dir}")

def clean_output_dir(output_dir):
    """
    Recursively delete the output directory and all its contents, then recreate it.
    """
    output_path = Path(output_dir)
    if output_path.exists():
        shutil.rmtree(output_path)  # Remove the directory and all its contents
        print(f"Deleted the output directory and its contents: {output_dir}")
    output_path.mkdir(parents=True, exist_ok=True)  # Recreate the directory
    print(f"Recreated the output directory: {output_dir}")

if __name__ == "__main__":

    # Ensure required directories exist
    Path(NOTEBOOK_DIR).mkdir(parents=True, exist_ok=True)
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    # fresh = True if (len(sys.argv) > 1 and sys.argv[1] == "fresh") else False
    fresh = True

    print(f'fresh: {fresh}')

    if fresh:
        clean_output_dir(OUTPUT_DIR)
        clean_output_dir(DOCS_FOLDER)

    # # Convert notebooks and generate site
    convert_notebooks_to_markdown(NOTEBOOK_DIR, OUTPUT_DIR, fresh = fresh)

    # Handle duplicate slugs after conversion
    resolve_duplicate_slugs(OUTPUT_DIR)

    copy_images_to_global_folder(OUTPUT_DIR, GLOBAL_IMAGES_DIR)

    # Generate site with Pelican
    try:
        generate_site_with_pelican(OUTPUT_DIR)
        print("Site generated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error generating site: {e}")
