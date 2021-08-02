boxie
=====

A command line utility to put text in a box.

Installation
------------

.. code:: bash

    pip install boxie

If you are on Linux you may need to use sudo to access this globally.

Usage
-----

.. code:: bash

    boxie "Hello World"

Or...

.. code:: bash

    python -m boxie "Hello World"

Or in your code:

.. code:: python

    from boxie import box_borders

    @box_borders
    def print_console(txt):
        print(txt)

    print_console("Hello World")

Check `test.py <./test.py>`__

Screenshot
~~~~~~~~~~

.. image:: ./assets/screenshot.png
   :alt: Screenshot

LICENSE
~~~~~~~

`MIT <./LICENSE>`__
