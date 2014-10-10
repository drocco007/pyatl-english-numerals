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

knowing how far you

can stretch


|----|

knowing how much

stretching is wise


|----|

the *art* of programming


What's next?
============


|----|

single digits


|----|

problem countours


|----|

*direct* mapping between

digit and numeral


|----|

=== ======
 0   zero
 1   one
 2   two
 ⋮
=== ======


|----|

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

but notice…


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

In English,

| “*join an empty list with*
| *an empty string…*”


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


Double Digits
=============


|----|

pretty much the same as

*twenties*

except we *look up* the tens place


|----|

.. code-block:: python

    def english_number(n):
        anything_left = True
        result = []

        if n >= 20:
            place = n / 10
            anything_left = n = n % 10
            result.append(tens[place])

            if anything_left:
                result.append('-')

        if anything_left:
            result.append(ones_teens[n])

        return ''.join(result)


|----|

::

    $ py.test -qx
    ..................................................
    50 passed in 0.07 seconds


|----|

*progress*


|----|

(Tivo™ “bedeep bedeep” noise here.

Hundreds are just like tens,

until we get to…)


One Hundred
===========

.. code-block:: python

    def english_number(n):
        anything_left = True
        result = []

        if n >= 100:
            return 'one hundred'

        if n >= 20:
        # etc.


One Hundred Whatever
====================

.. code-block:: python

    def english_number(n):
        anything_left = True
        result = []

        if n >= 100:
            anything_left = n = n % 100
            result.append('one hundred')

            if anything_left:
                result.append(' ')

        if n >= 20:
        # etc.



thousands
=========


|----|

if you were on

*autopilot*


|----|

now's the time to

turn it **off**


|----|

problem contours


|----|

Look at the problem


|----|

1000

one thousand


|----|

1001

one thousand one


|----|

8206

eight thousand two hundred six


|----|

16384

sixteen thousand three hundred eighty-four


|----|

in other words


|----|

split number into

thousands, hundreds, tens


|----|

result is

``english_number(thousands) + 'thousand'`` +

``english_number(hundreds) + 'hundred'`` +

``english_number(tens)``


|----|

``english_number(thousands)``

becomes

``english_number(16)``


|----|

Does anything about this look…


|----|

*familiar*


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

replace the numerals…


|----|

.. code-block:: python

    not_so_wee_numbers = [
        # This number makes my computer really mad
        # (10**(10**100), 'googolplex'),
        (10**100, 'googol'),
        # …
        (1000000000000000000000000000, 'octillion'),
        (1000000000000000000000000, 'septillion'),
        (1000000000000000000000, 'sextillion'),
        (1000000000000000000, 'quintillion'),
        (1000000000000000, 'quadrillion'),
        (1000000000000, 'trillion'),
        (1000000000, 'billion'),
        (1000000, 'million'),
        (1000, 'thousand'),
        (100, 'hundred'),
    ]


|----|

English still more

complicated

than Roman


|----|

3 main cases:

ones & teens

double digits

big numbers (>= 100)


|----|

big numbers uses *recursion*

to handle the question

“how *many* octillion?”


|----|

For learning:

github


|----|

For fun: command line


|----|

::

    $ python english_number.py [#, #, #, …]


|----|

for reference


|----|

age of the universe *in nanoseconds*

4.354×10\ :sup:`26`


|----|

number of atoms in the known universe

10\ :sup:`82`


|----|

::

    $ python english_number.py
    5352358218037910232050249409994268755976737569
    6365547821314866015615056550844069481866044289
    5167702150: fifty-three googol five thousand two
    hundred thirty-five quindecillion eight hundred
    twenty-one quattuordecillion eight hundred three
    tredecillion seven hundred ninety-one duodecillion
    twenty-three undecillion two hundred five decillion
    twenty-four nonillion nine hundred forty octillion
    nine hundred ninety-nine septillion four hundred
    twenty-six sextillion eight hundred seventy-five
    quintillion five hundred ninety-seven quadrillion
    six hundred seventy-three trillion seven hundred
    fifty-six billion nine hundred sixty-three million
    six hundred fifty-five thousand four hundred
    seventy-eight quindecillion two hundred thirteen…

|----|

so the next time you need to write a

*102 digit*

check


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
