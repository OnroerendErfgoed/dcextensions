============================
Extensions for dogpile.cache
============================

This library provides extensions for dogpile.cache. For the time being only one extension is provided, a memory backend that can be limited in size (number of items to cache).

.. image:: https://badge.fury.io/py/dcextensions.png
        :target: http://badge.fury.io/py/dcextensions

.. image:: https://travis-ci.org/OnroerendErfgoed/dcextensions.svg?branch=master
        :target: https://travis-ci.org/OnroerendErfgoed/dcextensions

.. image:: https://coveralls.io/repos/OnroerendErfgoed/dcextensions/badge.png?branch=master
        :target: https://coveralls.io/r/OnroerendErfgoed/dcextensions?branch=master

Installation
------------

To install dcextensions, use pip

.. code-block:: bash
    
    pip install dcextensions

Usage
-----

To use the memory backend

.. code-block:: python

.. code-block:: python

    from dogpile.cache import make_region

    region = make_region().configure(
        'dogpile.cache.memory.limited',
        expiration_time = 3600,
        arguments = {
            'cache_size': 100,
            'cache_dict': my_dict
        }
    )


Both arguments are optional. When use my_dict must be an instance of OrderedDict.
