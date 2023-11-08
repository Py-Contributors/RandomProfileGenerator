import sys
sys.path.append('.')

from datetime import datetime

__title__ = 'RandomProfileGenerator'
__package_name__ = 'random_profile'
__version__ = '3.0.2'
__description__ = "Python Module To Generate Random Profile Data"
__email__ = "deepak008@live.com"
__author__ = 'Deepak Raj'
__github__ = 'https://github.com/Py-Contributors/RandomProfileGenerator'
__pypi__ = 'https://pypi.org/project/random-profile/'
__license__ = 'MIT License'

project = __package_name__
description = __description__
author = __author__
release = __version__
year = datetime.now().year
copyright = "{} Deepak Raj".format(year)
source_suffix = ".rst"
source_encoding = "utf-8-sig"

master_doc = "index"
templates_path = ['_templates']
html_static_path = ['_static']
releases_github_path = "Py-Contributors/RandomProfileGenerator"

extensions = [
    'sphinx.ext.autosectionlabel'
]

autosectionlabel_prefix_document = True

html_theme = 'sphinx_rtd_theme'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}

# epub settings
epub_basename = project
epub_theme = 'epub'
epub_description = description
epub_author = author
epub_contributor = 'Py-Contributors'
epub_language = 'en'
epub_publisher = 'Py-Contributors'
epub_copyright = copyright
