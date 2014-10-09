ones_teens = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
              'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen',]

tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']

not_so_wee_numbers = [
    # This number makes my computer really mad
    # (10**(10**100), 'googolplex'),
    (10**100, 'googol'),
    (1000000000000000000000000000000000000000000000000, 'quindecillion'),
    (1000000000000000000000000000000000000000000000, 'quattuordecillion'),
    (1000000000000000000000000000000000000000000, 'tredecillion'),
    (1000000000000000000000000000000000000000, 'duodecillion'),
    (1000000000000000000000000000000000000, 'undecillion'),
    (1000000000000000000000000000000000, 'decillion'),
    (1000000000000000000000000000000, 'nonillion'),
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


def _handle_big(n):
    result = []

    for place, numeral in not_so_wee_numbers:
        if n < place:
            continue

        number_at_place = n / place
        n = n % place

        result.append('{numeral_at_place} {numeral}{space_for_more}'.format(
            numeral_at_place=english_number(number_at_place),
            numeral=numeral,
            space_for_more=' ' if n else '',
        ))

    return result, n


def english_number(n):
    anything_left = True
    result = []

    if n >= 100:
        result, n = _handle_big(n)
        anything_left = n

    if n >= 20:
        place = n / 10
        anything_left = n = n % 10
        result.append(tens[place])

        if anything_left:
            result.append('-')

    if anything_left:
        result.append(ones_teens[n])

    return ''.join(result)


def main():
    import sys
    import random

    # sys.argv[0] is the name of the script
    args = sys.argv[1:]

    if args:
        for n in (int(number) for number in args):
            print english_number(n)
    else:
        for size in (100, 100000000000, 100*10**100):
            n = random.randint(0, size)
            print '{}: {}\n'.format(n, english_number(n))


if __name__ == '__main__':
    main()
