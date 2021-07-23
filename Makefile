.PHONY: build dist upload livinglogic

build:
	rul4 tools/make_pygll.ul4 tools/make_style.ul4 tools/make_light_style.ul4 tools/make_dark_style.ul4 > src/pygll.py
	rm -rf dist/*
	python setup.py sdist --formats=gztar bdist_wheel

dist: build
	LL_URL_SSH_PYTHON=python3.2 python$(PYVERSION) -mll.scripts.ucp -vyes -ulivpython -glivpython dist/*.tar.gz dist/*.whl ssh://livpython@python.livinglogic.de/~/public_downloads/pygll/

upload: build
	twine upload dist/*

livinglogic: build
	python$(PYVERSION) -mll.scripts.ucp -vyes dist/*.tar.gz dist/*.whl ssh://intranet@intranet.livinglogic.de/~/documentroot/intranet.livinglogic.de/python-downloads/
