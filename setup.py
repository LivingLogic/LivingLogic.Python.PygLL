#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Setup script for the LivingLogic Pygments style

import os, re

try:
	import setuptools as tools
except ImportError:
	from distutils import core as tools


DESCRIPTION = """
Pygments style"""

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
Environment :: Plugins
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Text Processing :: Filters
Topic :: Utilities
Topic :: Software Development :: Libraries :: Python Modules
"""

KEYWORDS = "syntax highlighting pygments style"

try:
	news = list(open("docs/NEWS.rst", "r", encoding="utf-8"))
except IOError:
	description = DESCRIPTION.strip()
else:
	# Extract the first section (which are the changes for the current version)
	underlines = [i for (i, line) in enumerate(news) if line.startswith("---")]
	news = news[underlines[0]-1:underlines[1]-1]
	news = "".join(news)
	description = f"{DESCRIPTION.strip()}\n\n\n{news}"

# Get rid of text roles PyPI doesn't know about
description = re.subn(":[a-z]+:`~?([-a-zA-Z0-9_./]+)`", "``\\1``", description)[0]

# Expand tabs (so they won't show up as 8 spaces in the Windows installer)
description = description.expandtabs(2)

args = dict(
	name="pygll",
	version="0.1",
	description="Pygments style for dark and light backgrounds",
	long_description=description,
	author="Walter Doerwald",
	author_email="walter@livinglogic.de",
	url="http://python.livinglogic.de/",
	download_url="http://python.livinglogic.de/DOWNLOAD.html",
	license="MIT",
	classifiers=sorted({c for c in CLASSIFIERS.strip().splitlines() if c.strip() and not c.strip().startswith("#")}),
	keywords=KEYWORDS,
	py_modules="pygll",
	package_dir={"": "src"},
	entry_points={
		"pygments.styles": [
			"livinglogic-light = pygll:LivingLogicLightStyle",
			"livinglogic-dark  = pygll:LivingLogicDarkStyle",
		],
	},
	install_requires=[
		"pygments >= 2.0",
	],
)

if __name__ == "__main__":
	tools.setup(**args)
