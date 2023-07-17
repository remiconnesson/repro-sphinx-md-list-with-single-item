from pathlib import Path
import sys

ROOT_DIR = Path(__file__).parents[1]
sys.path.append(str(ROOT_DIR / 'src'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    # 'sphinx.ext.napoleon',
    'sphinxarg.ext',
    "sphinx_markdown_builder",
]

source_suffix = ['.rst']
