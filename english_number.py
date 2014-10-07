ones_tens = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
             'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
             'nineteen',]


def english_number(n):
    anything_left = True
    result = []

    if n >= 20:
        result.append('twenty')
        anything_left = n = n % 10

        if anything_left:
            result.append('-')

    if anything_left:
        result.append(ones_tens[n])

    return ''.join(result)


if __name__ == '__main__':
    main()
