from english_number import english_number

import pytest


def test_zero():
    assert 'zero' == english_number(0)


def test_one():
    assert 'one' == english_number(1)


@pytest.mark.parametrize('n, english',
    [(2, 'two'),
     (3, 'three'),
     (4, 'four'),
     (5, 'five'),
     (6, 'six'),
     (7, 'seven'),
     (8, 'eight'),
     (9, 'nine')]
)
def test_ones(n, english):
    assert english == english_number(n)
