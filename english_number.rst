.. |br| raw:: html

    <br/>


.. class:: bigtext

From Rome → |br| ← to England
-------------------------------

@drocco007

`source & instructions <https://github.com/drocco007/pyatl-english-numerals>`_


Last Time
---------


slide
-----

| *iteratively* design and build a
| *complex* calculation


slide
-----

| given a positive integer,
| return its equivalent representation
| in *additive* (ca 500BC) Roman numerals


slide
-----

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


slide
-----

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


slide
-----

*problem solving*


slide
-----

problem solving

how developers *approach* problems


slide
-----

problem solving

how developers *design* solutions


slide
-----

problem solving

how developers *implement* software


slide
-----

prefer *general solutions*

to **special cases**


slide
-----

leverage experience

to *anticipate next move*


slide
-----

DRY: pathological abhorrence of **repetition**


slide
-----

prefer *readability*


slide
-----

*maintainability*


slide
-----

*extensibility*


The *Art* of Programming
------------------------

problem contours, experience, language idiom, tools

↓

?

↙  ↘

A        B


This Time
---------


slide
-----

| given a positive integer,
| return its equivalent representation
| in *English numerals*


?
-

.. code-block:: python

    >>> def english_number(n):
    ...     return 'zero'
    >>> english_number(0)
    'zero'


slide
-----

similar problem to Roman


slide
-----

similar problem to Roman,\ |br|
but *more complicated*


Why?
----


slide
-----

Roman numerals are *regular*


slide
-----

| one **rule** to rule them all
|
|


slide
-----

| one **rule** to rule them all
|
| (ahem…)


123
---

123
---

.. code-block:: python

    >>> roman(123)
    'CXXIII'


slide
-----

English numerals are *irregular*


123
---



123
---

one hundred twenty-three


123
---

*units used throughout*

**one** hundred twenty-\ **three**


123
---

*two different separators*

one\ **␣**\ hundred\ **␣**\ twenty\ **⊟**\ three


123
---

*special names for teens & tens*

one hundred **twenty**-three


123
---

(**not** one hundred *two tens* three)


123
---

explicit *place name* vs. *not*

one **hundred** twenty\ **☼**\ -three **☼**


slide
-----

more complicated…


slide
-----

iterative development is a *tool*

we use to **manage complexity**


slide
-----

iterative development:

start small & simple

slide
-----

iterative development:

start small, refine


slide
-----

iterative development:

start small, refine, and test


Why tests?
----------


slide
-----

testing is less about

**correctness**


slide
-----

testing is more about

*confidence & creativity*


slide
-----

tests help you

*define and measure progress*


slide
-----

tests let you

*explore and create*


slide
-----

tests give you the

*confidence*

to work quickly and efficiently


Where to Begin?
---------------

slide
-----

.. code-block:: python

    >>> def english_number(n):
    ...     return 'zero'
    >>> english_number(0)
    'zero'


slide
-----

define progress by

*writing a test*

for it!


slide
-----

.. code-block:: python

    def test_one():
        assert 'one' == english_number(1)


slide
-----

progress


slide
-----

progress:

handling `1`


slide
-----

progress:

handling `1` *without breaking* `0`


slide
-----

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
----

.. code-block:: python

    def english_number(n):
        return 'one'

::

    $ py.test -qx
    F
    1 failed in 0.03 seconds


slide
-----

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


slide
-----

you will be

**tempted**

to work “faster” than this


slide
-----

the *further* you **stretch**

the *more ground* you'll have to


slide
-----

**retrace**


slide
-----

when something goes wrong


slide
-----

and the

**harder**

that retracing will be


slide
-----

(which doesn't sound

**faster**

to me ;)


slide
-----

knowing how far you

can stretch


slide
-----

knowing how much

stretching is wise


slide
-----

the *art* of programming


What's next?
------------


slide
-----

single digits


slide
-----

problem countours


slide
-----

*direct* mapping between

digit and numeral


slide
-----

=== ======
 0   zero
 1   one
 2   two
 ⋮
=== ======


slide
-----

Python has a *data structure* for that!


slide
-----

**list**


slide
-----

.. code-block:: python

    >>> ones = ['zero', 'one', 'two', 'three', 'four',
    ...         'five', 'six', 'seven', 'eight', 'nine']
    >>> def english_number(n):
    ...     return ones[n]


slide
-----

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


slide
-----

===== ========
 0     zero
 1     one
 ⋮
 10    ten
 11    eleven
 ⋮
===== ========


slide
-----

.. code-block:: python

    >>> ones_tens = ['zero', 'one', 'two', 'three',
    ...              'four', 'five', 'six', 'seven',
    ...              'eight', 'nine', 'ten', 'eleven',
    ...              'twelve', 'thirteen', 'fourteen',
    ...              'fifteen', 'sixteen', 'seventeen',
    ...              'eighteen', 'nineteen', ]
    >>> def english_number(n):
    ...     return ones_tens[n]


slide
-----

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
--------------------------

Twenties
--------

slide
-----

continue in same vein…


slide
-----

.. code-block:: python

    >>> ones_tens = ['zero', 'one', 'two', 'three',
    ...              # ...
    ...              'eighteen', 'nineteen', 'twenty',
    ...              'twenty-one', 'twenty-two', ]


slide
-----

(this is going to end badly…)


slide
-----

but notice…


slide
-----

result composed of a

*tens* numeral and a

**ones** numeral


slide
-----

*twenty*-**three**


slide
-----

so, in general,

slide
-----

*tens numeral* + ``'-'`` + **ones numeral**


slide
-----

we *already have* a solution

for the ones…


slide
-----

.. code-block:: python

    >>> def english_number(n):
    ...     return ones_tens[n]


slide
-----

so we *refine*


Refine
------

define progress


Refine
------

define progress, construct solution


Progress
--------

tests for the twenties cases


Detour
------

Python has great tools for

*efficient* testing


slide
-----

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

slide
-----

(uhm…)


slide
-----

“Make me a bunch of tests…”

.. code-block:: python

    @pytest.mark.parametrize


slide
-----

“…each taking an integer ``n`` and an English equivalent ``english``…”

.. code-block:: python

    @pytest.mark.parametrize('n, english',


slide
-----

| “…each of which checks the
| *input* ``n`` against the
| **result** ``english``…”

.. code-block:: python

    @pytest.mark.parametrize('n, english', … )
    def test_twenties(n, english):
        assert english == english_number(n)

slide
-----

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


slide
-----

.. code-block:: python

    >>> def english_number(n):
    ...     return ones_tens[n]


slide
-----

::

    $ py.test -qx
    ....................F
    1 failed, 20 passed in 0.06 seconds


slide
-----

.. code-block:: python

    >>> def english_number(n):
    ...     if n >= 20:
    ...         return 'twenty'
    ...     else:
    ...         return ones_tens[n]


slide
-----

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


slide
-----

*progress*


slide
-----

How do we handle the *ones*?


slide
-----

Does anything about this look…


slide
-----

*familiar*


slide
-----

.. code-block:: python

    >>> def roman(n):
    ...     parts = []
    ...     if n >= 5:
    ...         parts.append('V')
    ...         n -= 5  # n = n - 5
    ...     parts.append('I' * n)
    ...     return ''.join(parts)


slide
-----

We need to

check for a *twenty*


slide
-----

We need to

add it to the *result*


slide
-----

We need to

*remove* it from ``n``


slide
-----

We need to

let the *ones* code do its thing


slide
-----

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


slide
-----

Think it'll work?


slide
-----

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
--------------------

slide
-----

Hmm. I guess we should not

handle the ones if there

aren't any…


slide
-----

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


slide
-----

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
---------


slide
-----

wuzzgoinon?


slide
-----

we *fixed* twenty but *broke* zero…


How?
----

slide
-----

substitute ``0`` for ``n``…


slide
-----

.. code-block:: python

    def english_number(0):
        result = []

        if 0 >= 20:  # nope, skip this bit…
            # …

        if 0:  # nope, skip this bit…
            # …

        return ''.join(result)


slide
-----

In English,

| “*join an empty list with*
| *an empty string…*”


slide
-----

*creativity*


slide
-----

There are

*several*

approaches


slide
-----

Mine: do we have *anything left*?


slide
-----

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


slide
-----

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


slide
-----

*progress*


Double Digits
-------------


slide
-----

pretty much the same as

*twenties*

except we *look up* the tens place


slide
-----

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


slide
-----

::

    $ py.test -qx
    ..................................................
    50 passed in 0.07 seconds


slide
-----

*progress*


slide
-----

(Tivo™ “bedeep bedeep” noise here.

Hundreds are just like tens,

until we get to…)


One Hundred
-----------

.. code-block:: python

    def english_number(n):
        anything_left = True
        result = []

        if n >= 100:
            return 'one hundred'

        if n >= 20:
        # etc.


One Hundred Whatever
--------------------

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
---------


slide
-----

if you were on

*autopilot*


slide
-----

now's the time to

turn it **off**


slide
-----

problem contours


slide
-----

Look at the problem


slide
-----

1000

one thousand


slide
-----

1001

one thousand one


slide
-----

8206

eight thousand two hundred six


slide
-----

16384

sixteen thousand three hundred eighty-four


slide
-----

in other words


slide
-----

split number into

thousands, hundreds, tens


slide
-----

result is

``english_number(thousands) + 'thousand'`` +

``english_number(hundreds) + 'hundred'`` +

``english_number(tens)``


slide
-----

``english_number(thousands)``

becomes

``english_number(16)``


slide
-----

Does anything about this look…


slide
-----

*familiar*


slide
-----

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


slide
-----

replace the numerals…


slide
-----

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


slide
-----

English still more

complicated

than Roman


slide
-----

3 main cases:

ones & teens

double digits

big numbers (>= 100)


slide
-----

big numbers uses *recursion*

to handle the question

“how *many* octillion?”


slide
-----

For learning:

`github: source & instructions <https://github.com/drocco007/pyatl-english-numerals>`_


slide
-----

For fun: command line


slide
-----

::

    $ python english_number.py [#, #, #, …]


slide
-----

for reference


slide
-----

age of the universe *in nanoseconds*

4.354×10\ :sup:`26`


slide
-----

number of atoms in the known universe

10\ :sup:`82`


slide
-----

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

slide
-----

so the next time you need to write a

*102 digit*

check


slide
-----

Thank you!


slide
-----

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
