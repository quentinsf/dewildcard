# Dewildcard

A not-very-sophisticated script to replace Python wildcard import statements.

## Background

In Python, wildcard import statements, such as:

    from foo import *
    from bar import *

can be very convenient, but are now usually considered bad practice.  If, later in your code, you encounter a symbol you don't recognise, how do you know whether it came from *foo* or *bar*?  And if you install an updated version of *bar*, it may define a new name that clashes with one in *foo* that you were using in your code.

It's much better, therefore, to say:

    from foo import item1, item2
    from bar import item3, item4, item5

even though it's more verbose.  

Tools like *pylint* of *pyflakes* can also let you know if you can safely delete, say, 'item5', because it isn't used in your code.  If you have a good text editor, it may have a plugin which can highlight this fact.

This little script reads some python code on stdin and, when it finds a wildcard import statement, does the import and replaces the line with a full multi-line import statement:

    from bar import (item3,
                     item4,
                     item5,
                     item6)

You can then easily go through and delete any items that pylint tells you aren't needed.

If you prefer a single (possibly long) import line, you can use the `--single-line` option.
One advantage is that some tools such as autoflake and autopep8 handle this format better.

The parentheses are there to allow it to span multiple lines, but it shouldn't be too difficult to change the code to make it a single line or to use backslashes for line continuation if you prefer that.

NOTE: This has many limitations, the main one being that dewildcard must actually *perform* the imports in order to extract the symbol names, so you must run this in an environment where the appropriate modules exist, are on the Python path, and can be imported without unfortunate side-effects.


## Installation

    pip install dewildcard

Note that dewildcard makes use of importlib, so Python 2.7 or later will be needed.

## Example usage

    dewildcard my_code.py

This outputs the modified file to stdout.  If you wish to modify it in place, add a `-w` option:

    dewildcard -w my_code.py

## Acknowledgements

Dewildcard is based on an initial idea from Alexandre Fayolle - thanks, Alexandre!

Other contributors include Jan Bieroń and Jakub Wilk - thanks!

## To Do

Lots of room for improvements here, including:

* Options to change the output format

## Licence

Such a simple script is barely worth a licence, but, for what it's worth, it's released under GNU General Public Licence v2.  Use at your own risk, etc.

(c) 2015 Quentin Stafford-Fraser
