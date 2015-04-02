import os

import stix

project = u'python-stix'
copyright = u'2015, The MITRE Corporation'
version = stix.__version__
release = version

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon',
]

napoleon_use_admonition_for_examples = False

intersphinx_mapping = {'http://docs.python.org/': None}

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

rst_prolog = """
**Version**: {}
""".format(release)

exclude_patterns = ['_build', '_includes', 'api_vs_bindings/*_snippet.rst']

pygments_style = 'sphinx'

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = 'default'

html_sidebars = {"**": ['localtoc.html', 'relations.html', 'sourcelink.html',
'searchbox.html', 'links.html']}

latex_elements = {}
latex_documents = [
  ('index', 'python-stix.tex', u'python-stix Documentation',
   u'The MITRE Corporation', 'manual'),
]
