

AUTHOR          = '<your name>'  # use your name
SITENAME        = 'title' # use title
GITHUB_USERNAME = 'tactlabs' # use your username


# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/<yourusername>/"),
    ("LinkedIn", "<linkedin handle>"),
)

######## Advanced Settings (not recommended to to edited; take your own risk to touch the settings below) #############

import os
from git import Repo

# Get the current repository name dynamically
repo = Repo(os.getcwd())
FOLDER_NAME = os.path.basename(repo.working_dir)

# Check if the 'local' argument is provided
if os.getenv("PELICAN_ENV") == "local":
    # Local settings
    SITEURL         = ''
    RELATIVE_URLS   = True
    print("Running Pelican in LOCAL mode")
else:
    # Remote settings for GitHub Pages
    SITEURL         = f'https://{GITHUB_USERNAME}.github.io/{FOLDER_NAME}'
    RELATIVE_URLS   = False
    print(f"Running Pelican in REMOTE mode with SITEURL: {SITEURL}")

OUTPUT_PATH     = 'docs'
PATH            = "content"
TIMEZONE        = 'America/Toronto'
DEFAULT_LANG    = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM               = None
CATEGORY_FEED_ATOM          = None
TRANSLATION_FEED_ATOM       = None
AUTHOR_FEED_ATOM            = None
AUTHOR_FEED_RSS             = None

DEFAULT_PAGINATION          = 10

# Uncomment following line if you want document-relative URLs when developing
# Use SITEURL for absolute paths; RELATIVE_URLS is typically for local preview
RELATIVE_URLS = False

THEME               = 'themes/zurb-F5-basic'

IGNORE_FILES        = [".*", "*.swp", "*~"]  # Ignore hidden files and temporary files

