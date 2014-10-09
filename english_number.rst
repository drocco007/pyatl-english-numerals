.. |br| raw:: html

    <br/>


.. |----| raw:: html

    </div><div class="section">


.. class:: bigtext

From Rome → |br| ← to England
===============================

@drocco007


Last Time
=========


|----|

| *iteratively* design and build a
| *complex* calculation


|----|

| given a positive integer,
| return its equivalent representation
| in *additive* (ca 500BC) Roman numerals


|----|

.. code-block:: python

    >>> numerals = [('D', 500), ('C', 100),  # etc.
    ...             ('L', 50), ('X', 10),
    ...             ('V', 5), ('I', 1)]
    >>> def roman(n):
    ...     parts = []
    ...     for numeral, decimal in numerals:
    ...         count = n / decimal
    ...         parts.append(numeral * count)
    ...         n %= decimal
    ...     return ''.join(parts)


|----|

.. code-block:: python

    >>> print '\n'.join(roman(n) for n in
    ...                 (99, 75, 51, 49, 42, 25, 11))
    LXXXXVIIII
    LXXV
    LI
    XXXXVIIII
    XXXXII
    XXV
    XI


|----|

*problem solving*


|----|

problem solving

how developers *approach* problems


|----|

problem solving

how developers *design* solutions


|----|

problem solving

how developers *implement* software


|----|

prefer *general solutions*

to **special cases**


|----|

leverage experience

to *anticipate next move*


|----|

DRY: pathological abhorrence of **repetition**


|----|

prefer *readability*


|----|

*maintainability*


|----|

*extensibility*


The *Art* of Programming
========================

problem contours, experience, language idiom, tools

↓

?

↙  ↘

A        B


This Time
=========


|----|

| given a positive integer,
| return its equivalent representation
| in *English numerals*


?
=

.. code-block:: python

    >>> def english_number(n):
    ...     return 'zero'
    >>> english_number(0)
    'zero'


|----|

similar problem to Roman


|----|

similar problem to Roman,\ |br|
but *more complicated*


Why?
====


|----|

Roman numerals are *regular*


|----|

| one **rule** to rule them all
|
|


|----|

| one **rule** to rule them all
|
| (ahem…)


123
===

123
===

.. code-block:: python

    >>> roman(123)
    'CXXIII'


|----|

English numerals are *irregular*


123
===



123
===

one hundred twenty-three


123
===

*units used throughout*

**one** hundred twenty-\ **three**


123
===

*two different separators*

one\ **␣**\ hundred\ **␣**\ twenty\ **⊟**\ three


123
===

*special names for teens & tens*

one hundred **twenty**-three


123
===

(**not** one hundred *two tens* three)


123
===

explicit *place name* vs. *not*

one **hundred** twenty\ **☼**\ -three **☼**


|----|

more complicated…


|----|

the computer

*does what you tell it to*


|----|

the computer does

*exactly*

what you tell it to


|----|

the computer *only* does

*exactly*

what you tell it to,


|----|

**no more, no less!**


|----|

iterative development is a *tool*

we use to **manage complexity**


|----|

iterative development:

start small & simple

|----|

iterative development:

start small, refine


|----|

iterative development:

start small, refine, and test


Why tests?
==========


|----|

testing is less about

**correctness**


|----|

testing is more about

*confidence & creativity*


|----|

tests help you

*define and measure progress*


|----|

tests let you

*explore and create*


|----|

tests give you the

*confidence*

to work quickly and efficiently


Where to Begin?
===============

|----|

.. code-block:: python

    >>> def english_number(n):
    ...     return 'zero'
    >>> english_number(0)
    'zero'


|----|

define progress by

*writing a test*

for it!


|----|

.. code-block:: python

    def test_one():
        assert 'one' == english_number(1)


|----|

progress


|----|

progress:

handling `1`


|----|

progress:

handling `1` *without breaking* `0`


|----|

.. code-block::

    $ py.test -qx
    .F
    =================== FAILURES ===================
    ___________________ test_one ___________________

        def test_one():
    >       assert 'one' == english_number(1)
    E       assert 'one' == 'zero'
    E         - one
    E         + zero

    test_english.py:8: AssertionError
    !!!! Interrupted: stopping after 1 failures !!!!
    1 failed, 1 passed in 0.03 seconds


Nope
====

.. code-block:: python

    def english_number(n):
        return 'one'

::

    $ py.test -qx
    F
    1 failed in 0.03 seconds


|----|

.. code-block:: python

    def english_number(n):
        if n:
            return 'one'
        else:
            return 'zero'

::

    $ py.test -qx
    ..
    2 passed in 0.01 seconds


|----|

you will be

**tempted**

to work “faster” than this


|----|

the *further* you **stretch**

the *more ground* you'll have to


|----|

**retrace**


|----|

when something goes wrong


|----|

and the

**harder**

that retracing will be


|----|

(which doesn't sound

**faster**

to me ;)


|----|

the *art* of programming


What's next?
============


|----|

single digits


|----|

problem countours


|----|

problem countours

*direct* mapping between digit and numeral


|----|

=== ======
 0   zero
 1   one
 2   two
 ⋮
=== ======


|----|

countours and language tools

Python has a *data structure* for that!


|----|

**list**


|----|

.. code-block:: python

    >>> ones = ['zero', 'one', 'two', 'three', 'four',
    ...         'five', 'six', 'seven', 'eight', 'nine']
    >>> def english_number(n):
    ...     return ones[n]


|----|

.. code-block:: python

    >>> print '\n'.join(english_number(n)
    ...                 for n in range(10))
    zero
    one
    two
    three
    four
    five
    six
    seven
    eight
    nine


|----|

===== ========
 0     zero
 1     one
 ⋮
 10    ten
 11    eleven
 ⋮
===== ========


|----|

.. code-block:: python

    >>> ones_tens = ['zero', 'one', 'two', 'three',
    ...              'four', 'five', 'six', 'seven',
    ...              'eight', 'nine', 'ten', 'eleven',
    ...              'twelve', 'thirteen', 'fourteen',
    ...              'fifteen', 'sixteen', 'seventeen',
    ...              'eighteen', 'nineteen', ]
    >>> def english_number(n):
    ...     return ones_tens[n]


|----|

.. code-block:: python

    >>> print '\n'.join(english_number(n)
    ...                 for n in range(10, 20))
    ten
    eleven
    twelve
    thirteen
    fourteen
    fifteen
    sixteen
    seventeen
    eighteen
    nineteen


So Much for the Easy Part…
==========================

Twenties
========

|----|

continue in same vein…


|----|

.. code-block:: python

    >>> ones_tens = ['zero', 'one', 'two', 'three',
    ...              # ...
    ...              'eighteen', 'nineteen', 'twenty',
    ...              'twenty-one', 'twenty-two', ]


|----|

(this is going to end badly…)


|----|

but…


|----|

result composed of a

*tens* numeral and a

**ones** numeral


|----|

*twenty*-**three**


|----|

so, in general,

|----|

*tens numeral* + ``'-'`` + **ones numeral**


|----|

we *already have* a solution

for the ones…


|----|

.. code-block:: python

    >>> def english_number(n):
    ...     return ones_tens[n]


|----|

so we *refine*


Refine
======

define progress


Refine
======

define progress, construct solution


Progress
========

tests for the twenties cases


Detour
======

Python has great tools for

*efficient* testing


|----|

.. code-block:: python

    @pytest.mark.parametrize('n, english',
        [(23, 'twenty-three'),
         (24, 'twenty-four'),
         (25, 'twenty-five'),
         (26, 'twenty-six'),
         (27, 'twenty-seven'),
         (28, 'twenty-eight'),
         (29, 'twenty-nine')]
    )
    def test_twenties(n, english):
        assert english == english_number(n)

|----|

(uhm…)


|----|

“Make me a bunch of tests…”

.. code-block:: python

    @pytest.mark.parametrize


|----|

“…each taking an integer ``n`` and an English equivalent ``english``…”

.. code-block:: python

    @pytest.mark.parametrize('n, english',


|----|

| “…each of which checks the
| *input* ``n`` against the
| **result** ``english``…”

.. code-block:: python

    @pytest.mark.parametrize('n, english', … )
    def test_twenties(n, english):
        assert english == english_number(n)

|----|

“…and here's the data!”

.. code-block:: python

    @pytest.mark.parametrize('n, english',
        [(23, 'twenty-three'),
         (24, 'twenty-four'),
         (25, 'twenty-five'),
         (26, 'twenty-six'),
         (27, 'twenty-seven'),
         (28, 'twenty-eight'),
         (29, 'twenty-nine')]
    )
    def test_twenties(n, english):
        assert english == english_number(n)


|----|

.. code-block:: python

    >>> def english_number(n):
    ...     return ones_tens[n]


|----|

::

    $ py.test -qx
    ....................F
    1 failed, 20 passed in 0.06 seconds


|----|

.. code-block:: python

    >>> def english_number(n):
    ...     if n >= 20:
    ...         return 'twenty'
    ...     else:
    ...         return ones_tens[n]


|----|

::

    $ py.test -qx
    .....................F
    =================== FAILURES ===================
    _______________ test_twenty_one ________________

        def test_twenty_one():
    >       assert 'twenty-one' == english_number(21)
    E       assert 'twenty-one' == 'twenty'
    E         - twenty-one
    E         ?       ----
    E         + twenty

    test_english.py:49: AssertionError
    !!!! Interrupted: stopping after 1 failures !!!!
    1 failed, 21 passed in 0.06 seconds


|----|

*progress*


|----|

How do we handle the *ones*?


|----|

Does anything about this look…


|----|

*familiar*


|----|

.. code-block:: python

    >>> def roman(n):
    ...     parts = []
    ...     if n >= 5:
    ...         parts.append('V')
    ...         n -= 5  # n = n - 5
    ...     parts.append('I' * n)
    ...     return ''.join(parts)


|----|

We need to

check for a *twenty*


|----|

We need to

add it to the *result*


|----|

We need to

*remove* it from ``n``


|----|

We need to

let the *ones* code do its thing


|----|

.. code-block:: python

    def english_number(n):
        result = []

        # check for a twenty
        if n >= 20:

            # add it to the result
            result.append('twenty')

            # remove it from n
            n %= 20

        # handle the ones
        result.append(ones_tens[n])

        return ''.join(result)


|----|

Think it'll work?


|----|

::

    $ py.test -qx
    ....................F
    =================== FAILURES ===================
    _________________ test_twenty __________________

        def test_twenty():
    >       assert 'twenty' == english_number(20)
    E       assert 'twenty' == 'twentyzero'
    E         - twenty
    E         + twentyzero
    E         ?       ++++

    test_english.py:45: AssertionError
    !!!! Interrupted: stopping after 1 failures !!!!
    1 failed, 20 passed in 0.06 seconds

**Twentyzero??!?!?**
====================

|----|

Hmm. I guess we should not

handle the ones if there

aren't any…


|----|

.. code-block:: python

    def english_number(n):
        result = []

        # check for a twenty
        if n >= 20:

            # add it to the result
            result.append('twenty')

            # remove it from n
            n %= 20

        # handle the ones
        if n:
            result.append(ones_tens[n])

        return ''.join(result)


|----|

::

    $ py.test -qx
    F
    =================== FAILURES ===================
    __________________ test_zero ___________________

        def test_zero():
    >       assert 'zero' == english_number(0)
    E       assert 'zero' == ''
    E         - zero

    test_english.py:7: AssertionError
    !!!! Interrupted: stopping after 1 failures !!!!
    1 failed in 0.04 seconds


AHHHHH!!!
=========


|----|

wuzzgoinon?


|----|

we *fixed* twenty but *broke* zero…


How?
====

|----|

substitute ``0`` for ``n``…


|----|

.. code-block:: python

    def english_number(0):
        result = []

        if 0 >= 20:  # nope, skip this bit…
            # …

        if 0:  # nope, skip this bit…
            # …

        return ''.join(result)


|----|

*creativity*


|----|

There are

*several*

approaches


|----|

Mine: do we have *anything left*?


|----|

.. code-block:: python

    def english_number(n):
        anything_left = True
        result = []

        if n >= 20:
            result.append('twenty')

            n %= 20
            anything_left = n

        if anything_left:
            result.append(ones_tens[n])

        return ''.join(result)


|----|

::

    $ py.test -qx
    .....................F
    =================== FAILURES ===================
    _______________ test_twenty_one ________________

        def test_twenty_one():
    >       assert 'twenty-one' == english_number(21)
    E       assert 'twenty-one' == 'twentyone'
    E         - twenty-one
    E         ?       -
    E         + twentyone

    test_english.py:49: AssertionError
    !!!! Interrupted: stopping after 1 failures !!!!
    1 failed, 21 passed in 0.06 seconds


|----|

*progress*


|----|
|----|
|----|
|----|
|----|

Thank you!


|----|

♥

@drocco007

.. raw:: html

    <!-- single quote: ’
    double quotes: x“”x
    em-dash: —
    vertical ellipsis: ⋮
    arrows: ←, ↑, →, ↓, ↔, ↕, ↖, ↗, ↘, ↙ -->
    <script>
        window.slide_transition_time = 200;
    </script>
    <script src="static/jquery-1.6.2.min.js"></script>
    <script src="static/jquery.url.min.js"></script>
    <script src="static/slides2.js"></script>
