from english_number import english_number


def test_zero():
    assert 'zero' == english_number(0)


def test_one():
    assert 'one' == english_number(1)
