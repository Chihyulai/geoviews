# -*- coding: utf-8 -*-

from nbsite.shared_conf import *

project = u'GeoViews'
authors = u'PyViz Developers'
copyright = u'2018 ' + authors
description = 'Geographic visualizations for HoloViews.'

import geoviews
version = release = str(geoviews.__version__)

html_static_path += ['_static']
html_theme = 'sphinx_ioam_theme'
html_theme_options = {
    'logo':'geoviews-logo.png',
    'favicon':'favicon.ico',
    'custom_css':'geoviews.css'
}

_NAV =  (
        ('User Guide', 'user_guide/index'),
        ('Gallery', 'gallery/index'),
        ('About', 'about')
)

nbsite_gallery_conf = {
    'backends': ['bokeh', 'matplotlib'],
    'galleries': {
        'gallery': {'title': 'Gallery'}
    },
    'github_org': 'pyviz',
    'github_project': 'geoviews'
}

extensions += ['nbsite.gallery']

templates_path = ['_templates']

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    'WEBSITE_SERVER': 'https://geoviews.org',
    'VERSION': version,
    'NAV': _NAV,
    'LINKS': _NAV,
    'SOCIAL': (
        ('Gitter', '//gitter.im/pyviz/pyviz'),
        ('Twitter', '//twitter.com/holoviews'),
        ('Github', '//github.com/pyviz/geoviews'),
    )
})
