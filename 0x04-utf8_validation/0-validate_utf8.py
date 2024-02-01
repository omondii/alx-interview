#!/usr/bin/python3
""" Checks if a passed string is utf-8 compliant """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding.
        >>> s = Solution()
        >>> s.validUtf8([197, 130, 1])
        True
        >>> s.validUtf8([235, 140, 4])
        False
    """
    data = iter(data)
    for leadingByte in data:
        leadingOnes = count_leading_ones(leadingByte)
        if leadingOnes in [1, 7, 8]:
            return False
        for _ in range(leadingOnes - 1):
            try:
                trailingByte = next(data)
            except StopIteration:
                return False
            if trailingByte is None or trailingByte >> 6 !=0b10:
                return False
    return True

def count_leading_ones(byte):
    for i in range(8):
        if byte >> (7 - i) == 0b11111111 >> (7 -1) & ~1:
            return i
        return 8