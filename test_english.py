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


@pytest.mark.parametrize('n, english',
    [(102, 'one hundred two'),
     (103, 'one hundred three'),
     (104, 'one hundred four'),
     (105, 'one hundred five'),
     (106, 'one hundred six'),
     (107, 'one hundred seven'),
     (108, 'one hundred eight'),
     (109, 'one hundred nine')]
)
def test_one_hundred_ones(n, english):
    assert english == english_number(n)


@pytest.mark.parametrize('n, english',
    [(123, 'one hundred twenty-three'),
     (124, 'one hundred twenty-four'),
     (125, 'one hundred twenty-five'),
     (126, 'one hundred twenty-six'),
     (127, 'one hundred twenty-seven'),
     (128, 'one hundred twenty-eight'),
     (129, 'one hundred twenty-nine')]
)
def test_one_hundred_twenties(n, english):
    assert english == english_number(n)


@pytest.mark.parametrize('n, english',
    [(130, 'one hundred thirty'),
     (131, 'one hundred thirty-one'),
     (132, 'one hundred thirty-two'),
     (133, 'one hundred thirty-three'),
     (134, 'one hundred thirty-four'),
     (135, 'one hundred thirty-five'),
     (136, 'one hundred thirty-six'),
     (137, 'one hundred thirty-seven'),
     (138, 'one hundred thirty-eight'),
     (139, 'one hundred thirty-nine')]
)
def test_one_hundred_thirties(n, english):
    assert english == english_number(n)


@pytest.mark.parametrize('n, english',
    [(199, 'one hundred ninety-nine'),
     (193, 'one hundred ninety-three'),
     (190, 'one hundred ninety'),
     (182, 'one hundred eighty-two'),
     (178, 'one hundred seventy-eight'),
     (175, 'one hundred seventy-five'),
     (170, 'one hundred seventy'),
     (165, 'one hundred sixty-five'),
     (156, 'one hundred fifty-six'),
     (147, 'one hundred forty-seven'),]
)
def test_other_one_hundreds(n, english):
    assert english == english_number(n)


@pytest.mark.parametrize('n, english',
    [(200, 'two hundred'),
     (201, 'two hundred one'),
     (300, 'three hundred'),
     (301, 'three hundred one'),
     (400, 'four hundred'),
     (401, 'four hundred one'),
     (500, 'five hundred'),
     (501, 'five hundred one'),
     (600, 'six hundred'),
     (601, 'six hundred one'),
     (700, 'seven hundred'),
     (701, 'seven hundred one'),
     (800, 'eight hundred'),
     (801, 'eight hundred one'),
     (900, 'nine hundred'),
     (901, 'nine hundred one'),]
)
def test_other_hundreds_zero_one(n, english):
    assert english == english_number(n)


@pytest.mark.parametrize('n, english',
    [(999, 'nine hundred ninety-nine'),
     (893, 'eight hundred ninety-three'),
     (790, 'seven hundred ninety'),
     (682, 'six hundred eighty-two'),
     (678, 'six hundred seventy-eight'),
     (575, 'five hundred seventy-five'),
     (470, 'four hundred seventy'),
     (365, 'three hundred sixty-five'),
     (256, 'two hundred fifty-six'),
     (147, 'one hundred forty-seven'),]
)
def test_other_hundreds(n, english):
    assert english == english_number(n)


def test_one_thousand():
    assert 'one thousand' == english_number(1000)


def test_one_thousand_one():
    assert 'one thousand one' == english_number(1001)


@pytest.mark.parametrize('n, english',
    [(1002, 'one thousand two'),
     (1003, 'one thousand three'),
     (1004, 'one thousand four'),
     (1005, 'one thousand five'),
     (1006, 'one thousand six'),
     (1007, 'one thousand seven'),
     (1008, 'one thousand eight'),
     (1009, 'one thousand nine'),
     (1010, 'one thousand ten'),
     (1011, 'one thousand eleven'),
     (1012, 'one thousand twelve'),
     (1013, 'one thousand thirteen'),
     (1014, 'one thousand fourteen'),
     (1015, 'one thousand fifteen'),
     (1016, 'one thousand sixteen'),
     (1017, 'one thousand seventeen'),
     (1018, 'one thousand eighteen'),
     (1019, 'one thousand nineteen')]
)
def test_one_thousand_ones(n, english):
    assert english == english_number(n)


def test_party_like_its():
    assert 'one thousand nine hundred ninety-nine' == english_number(1999)


def test_sobering_social_commentary():
    assert 'one thousand nine hundred eighty-four' == english_number(1984)


def test_inception_of_dan():
    assert 'one thousand nine hundred seventy-eight' == english_number(1978)


def test_war_of():
    assert 'one thousand eight hundred twelve' == english_number(1812)


def test_spirit_of():
    assert 'one thousand seven hundred seventy-six' == english_number(1776)


def test_happy_birthday_Bach():
    assert 'one thousand six hundred eighty-five' == english_number(1685)


def test_two_thousand():
    assert 'two thousand' == english_number(2000)


def test_two_thousand_one():
    assert 'two thousand one' == english_number(2001)


def test_ten_thousand():
    assert 'ten thousand' == english_number(10000)


@pytest.mark.parametrize('n, english',
    [(99999, 'ninety-nine thousand nine hundred ninety-nine'),
     (80000, 'eighty thousand'),
     (65536, 'sixty-five thousand five hundred thirty-six'),
     (32768, 'thirty-two thousand seven hundred sixty-eight'),
     (16384, 'sixteen thousand three hundred eighty-four'),
     (8192, 'eight thousand one hundred ninety-two'),
     (4096, 'four thousand ninety-six'),
     (2048, 'two thousand forty-eight'),
     (1024, 'one thousand twenty-four'),]
)
def test_other_thousands(n, english):
    assert english == english_number(n)


def test_one_hundred_thousand():
    assert 'one hundred thousand' == english_number(100000)


@pytest.mark.parametrize('n, english',
    [(200000, 'two hundred thousand'),
     (300000, 'three hundred thousand'),
     (400000, 'four hundred thousand'),
     (500000, 'five hundred thousand'),
     (600000, 'six hundred thousand'),
     (700000, 'seven hundred thousand'),
     (800000, 'eight hundred thousand'),
     (900000, 'nine hundred thousand'),]
)
def test_other_hundred_thousands(n, english):
    assert english == english_number(n)


def test_one_million():
    assert 'one million' == english_number(1000000)


def test_big_million():
    assert ('eight hundred sixty-seven million three hundred twenty-four '
            'thousand eight hundred seventy-six') == english_number(867324876)


def test_one_billion():
    assert 'one billion' == english_number(1000000000)


def test_big_billion():
    assert ('four hundred thirty-five billion seven hundred twenty million '
            'one hundred one thousand nine hundred forty-three') \
        == english_number(435720101943)


def test_one_trillion():
    assert 'one trillion' == english_number(1000000000000)


def test_big_trillion():
    assert ('one hundred eleven trillion one hundred ten million one hundred '
            'one') == english_number(111000110000101)


def test_one_quadrillion():
    assert 'one quadrillion' == english_number(1000000000000000)


def test_googol():
    assert 'two googol' == english_number(2*10**100)
