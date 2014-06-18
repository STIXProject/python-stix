import stix

project = u'python-stix'
copyright = u'2014, The MITRE Corporation'
version = stix.__version__
release = version

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.napoleon',
]

intersphinx_mapping = {'http://docs.python.org/': None}

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

rst_prolog = """
.. warning::

    This documentation is still a work in progress. If you have any issues or
    questions, please ask on the stix-discussion mailing list or file a bug
    in our `issue tracker`_.

.. _issue tracker: https://github.com/STIXProject/python-stix/issues
"""

exclude_patterns = ['_build']
pygments_style = 'sphinx'

html_theme = 'default'
html_style = 'stix_doc.css'
html_static_path = ['_static']
htmlhelp_basename = 'python-stixdoc'

html_theme_options = {
    'codebgcolor': '#EEE',
    'footerbgcolor': '#FFF',
    'footertextcolor': '#666',
    'headbgcolor': '#CCC',
    'headtextcolor': '#666',
    'headlinkcolor': '#ED1C24',
    'linkcolor': '#ED1C24',
    'relbarbgcolor': '#666',
    'relbartextcolor': '#ED1C24',
    'sidebarbgcolor': '#EEE',
    'sidebarlinkcolor': '#ED1C24',
    'sidebartextcolor': '#000',
    'visitedlinkcolor': '#ED1C24',
}
html_sidebars = {"**": ['localtoc.html', 'relations.html', 'sourcelink.html',
'searchbox.html', 'links.html']}

latex_elements = {}
latex_documents = [
  ('index', 'python-stix.tex', u'python-stix Documentation',
   u'The MITRE Corporation', 'manual'),
]
