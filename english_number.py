ones_teens = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
              'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen',]

tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']

not_so_wee_numbers = [
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


if __name__ == '__main__':
    main()
