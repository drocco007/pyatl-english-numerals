----------------------
 From Rome to England
----------------------

| Python Atlanta—October 9, 2014
| Daniel Rocco
| *@drocco007*


Iterative Development and Testing
---------------------------------

    “tests help you *define and measure progress*, enable *exploration
    and creativity*, and give you the *confidence* to work quickly and
    efficiently”


My October talk was a spiritual successor to September's `Party Like
it's 500BC <https://github.com/pyatl/talks/tree/master/2014-09/roman>`_.
This month I emphasized the testing aspect of the development process
as we explored the creation of a solution from a mere problem statement
to a complete and well tested implementation.

Problem statement:

    | given a positive integer,
    | return its equivalent representation
    | in *English numerals*


Try It Out
----------

If you just want to play with the number generator, you can `download
the source <https://raw.githubusercontent.com/drocco007/pyatl-english-numerals/master/english_number.py>`_
and run it on your local machine::

    wget https://raw.githubusercontent.com/drocco007/pyatl-english-numerals/master/english_number.py
    python english_number.py 123

If everything is working, you should see the output::

    one hundred twenty-three

You can also run ``english_number.py`` with no arguments to see the
numeral equivalents of three randomly generated numbers.


Examine The Source
------------------

You can view the source for the project from the comfort of your web browser:

* `Implementation of the solution and commandline interface <english_number.py>`_
* `The py.test test suite for the implementation <test_english.py>`_

The `source code for the slides <english_number.rst>`_ includes doctests
for several of the intermediate steps in the construction process.


Digging Deeper
--------------

This repository includes a full test suite and the complete history of
the steps I took to construct the final program. To explore further,
you'll need

* Python 2
* a text editor
* Git
* virtualenvwrapper and virtualenv
* py.test

If you need help getting any of these tools set up, ask for help on the
list or send me a note.

Once you have everything set up, get the source repository::

    git clone git@github.com:drocco007/pyatl-english-numerals.git

at which point you should be able to run the test suite::

    py.test

which should show, in a nice friendly green, something like::

    ============= test session starts ==============
    platform linux2 -- Python 2.7.5 -- py-1.4.20 -- pytest-2.5.2
    plugins: xdist
    collected 168 items

    test_english.py ................................
    ................................................
    ................................................
    ........................................

    ========== 168 passed in 0.48 seconds ==========

Try changing something and see if the tests break! :)


Working Backward
----------------

The repository includes marker branches at many interesting points along
my development process::

    git branch

which yields::

    master
    busted-refactor
    big-numbers
    thousands
    hundreds
    better-twenty
    double-digit
    naïve-twenty
    tens
    ones
    one
    zero

To see the implementation and tests at any of these points::

    git checkout double-digit
