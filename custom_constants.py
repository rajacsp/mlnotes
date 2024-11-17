

import os
from git import Repo

# Get the current repository name dynamically
repo = Repo(os.getcwd())
FOLDER_NAME = os.path.basename(repo.working_dir)
