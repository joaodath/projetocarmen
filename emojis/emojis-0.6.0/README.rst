Emojis
======

|Documentation Status| |Build Status| |PyPI| |PyPI - Python Version|

Emojis for Python

About
-----

This library allows you to emojify content such as:
``This is a message with emojis :smile: :snake:``

Emoji database is based on `gemoji <https://github.com/github/gemoji>`__
library.

See the `Emoji cheat sheet <http://www.emoji-cheat-sheet.com/>`__ for
more examples.

Example
-------

.. code:: python

   >>> import emojis

   >>> emojis.encode('This is a message with emojis :smile: :snake:')
   'This is a message with emojis 😄 🐍'

   >>> emojis.decode('This is a message with emojis 😄 🐍')
   'This is a message with emojis :smile: :snake:'

   >>> emojis.get('Prefix 😄 🐍 😄 🐍 Sufix')
   {'😄', '🐍'}

   >>> emojis.count('😄 🐍 😄 🐍')
   4

   >>> emojis.count('😄 🐍 😄 🐍', unique=True)
   2

   >>> emojis.db.get_emoji_by_alias('snake')
   Emoji(aliases=['snake'], emoji='🐍', tags=[], category='Animals & Nature', unicode_version='6.0')

   >>> emojis.db.get_categories()
   {'Activities', 'Travel & Places', 'Smileys & Emotion', 'Symbols', 'Food & Drink', 'Animals & Nature', 'People & Body', 'Objects', 'Flags'}

Installation
------------

Install ``emojis`` with ``pip``.

``pip3 install -U emojis``

Documentation
-------------

`https://emojis.readthedocs.io/ <https://emojis.readthedocs.io/en/latest/>`__

Missing or wrong emoji?
-----------------------

This library is based on `gemoji <https://github.com/github/gemoji>`__
database, the official GitHub emoji library for Ruby.

If an emoji is missing or labeled wrongly, report to
`gemoji <https://github.com/github/gemoji>`__ project. If gemoji fix it,
this library will be updated as soon as there’s a new gemoji release.

All issues complaining about missing emojis will be closed.

All PRs to include custom emojis will be closed.

License
-------

MIT

.. |Documentation Status| image:: https://readthedocs.org/projects/emojis/badge/?version=latest
   :target: https://emojis.readthedocs.io/en/latest/?badge=latest
.. |Build Status| image:: https://travis-ci.org/alexandrevicenzi/emojis.svg?branch=master
   :target: https://travis-ci.org/alexandrevicenzi/emojis
.. |PyPI| image:: https://img.shields.io/pypi/v/emojis.svg
   :target: https://pypi.org/project/emojis/
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/emojis.svg
   :target: https://pypi.org/project/emojis/
