Pygments__ syntax highlighting styles for dark and light backgrounds

__ https://pygments.org/

.. image:: https://github.com/LivingLogic/LivingLogic.Python.PygLL/blob/master/PygLL.png


Installation
============

Install with::

	$ pip install pygll


After installation, two new styles are available:

=============================== =====================
Python class                    Style name
=============================== =====================
``pygll.LivingLogicLightStyle`` ``livinglogic-light``
``pygll.LivingLogicDarkStyle``  ``livinglogic-dark``
=============================== =====================


Usage with Sphinx
=================

If you want to use this Pygments style with Sphinx put the following in your
``conf.py``::

	pygments_style = 'livinglogic-light'

Whether and how you can specify to use the theme matching the current OS color
scheme depends on the HTML theme you're using.


History
=======

HEAD (2021-06-??)
-----------------

Initial release.