tens = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
        'seventy', 'eighty', 'ninety']
ones_teens = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
              'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen',]


def english_number(n):
    anything_left = True
    result = []

    if n >= 1000:
        return 'one thousand'

    if n >= 100:
        hundreds = n / 100
        anything_left = n = n % 100
        result.append(english_number(hundreds))
        result.append(' hundred')

        if anything_left:
            result.append(' ')

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
