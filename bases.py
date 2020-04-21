#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= int(base) <= 36, 'base is out of range: {}'.format(base)
    base = int(base)
    digits = digits.upper()
    # TODO: Decode digits from binary (base 2)
    if base == 2:
        digits = digits[::-1]
        decoded = 0
        for i in range(len(digits)):
            if digits[i] == "1":
                decoded += 2**i
        return decoded

    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    elif base == 16:
        convert = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        digits = digits[::-1]
        decoded = 0 
        for i in range(len(digits)):
            if digits[i] in convert.keys():
                decoded += (16**i) * convert[digits[i]]
            else:
                decoded += (16**i) * int(digits[i])
        return decoded
    # # ...
    # # TODO: Decode digits from any base (2 up to 36)
    else:
        value = 10
        convert = {}
        for letter in string.ascii_uppercase:
            convert[letter] = value
            value += 1 
        digits = digits[::-1]
        decoded = 0 
        for i in range(len(digits)):
            if digits[i] in convert.keys():
                decoded += (base**i) * convert[digits[i]]
            else:
                decoded += (base**i) * int(digits[i])
        return decoded

    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    chars = string.digits + string.ascii_lowercase
    chars = chars[0:base]
    encoded = ""
    while True:
        remainder = number % base
        number = number // base
        encoded += chars[remainder]
        if number == 0:
            return encoded[::-1]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base ? to base 10
    if base2 == 10:
        return decode(digits, base1)
    # TODO: Convert digits from base 10 to base ? (and vice versa)
    elif base1 == 10: 
        return encode(int(digits), base2)
    # TODO: Convert digits from any base to any base (2 up to 36)
    else:
        decoded = decode(digits, base1)
        return str(encode(decoded, base2))


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    # print(decode("3a45f", 16))