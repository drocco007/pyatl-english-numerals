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


@pytest.mark.parametrize('n, english',
    [(10, 'ten'),
     (11, 'eleven'),
     (12, 'twelve'),
     (13, 'thirteen'),
     (14, 'fourteen'),
     (15, 'fifteen'),
     (16, 'sixteen'),
     (17, 'seventeen'),
     (18, 'eighteen'),
     (19, 'nineteen')]
)
def test_tens(n, english):
    assert english == english_number(n)


def test_twenty():
    assert 'twenty' == english_number(20)


def test_twenty_one():
    assert 'twenty-one' == english_number(21)


def test_twenty_two():
    assert 'twenty-two' == english_number(22)


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


@pytest.mark.parametrize('n, english',
    [(30, 'thirty'),
     (31, 'thirty-one'),
     (32, 'thirty-two'),
     (33, 'thirty-three'),
     (34, 'thirty-four'),
     (35, 'thirty-five'),
     (36, 'thirty-six'),
     (37, 'thirty-seven'),
     (38, 'thirty-eight'),
     (39, 'thirty-nine')]
)
def test_thirties(n, english):
    assert english == english_number(n)


@pytest.mark.parametrize('n, english',
    [(99, 'ninety-nine'),
     (93, 'ninety-three'),
     (90, 'ninety'),
     (82, 'eighty-two'),
     (78, 'seventy-eight'),
     (75, 'seventy-five'),
     (70, 'seventy'),
     (65, 'sixty-five'),
     (56, 'fifty-six'),
     (47, 'forty-seven'),]
)
def test_double_digit(n, english):
    assert english == english_number(n)


def test_one_hundred():
    assert 'one hundred' == english_number(100)


def test_one_hundred_one():
    assert 'one hundred one' == english_number(101)
