.PHONY: build upload

build:
	rul4 tools/make_pygll.ul4 tools/make_style.ul4 tools/make_light_style.ul4 tools/make_dark_style.ul4 > src/pygll.py
	rm -rf dist/*
	python setup.py sdist --formats=gztar bdist_wheel

upload: build
	twine upload dist/*
