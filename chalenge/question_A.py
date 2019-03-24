"""
Lines can overlap in 3 ways:
l1 line contains l2:

l1 -----------
     *****
l2   -----

l2 contains l1:

l1   -----
     *****
l2 -----------

l1 contains start of l2:

l1 -----
     ***
l2   -----

l1 contains end of l2:

l1    -----
      **
l2 -----

Summing up, two lines overlap if one contains the end or beginning of another
"""


def check_line_overlap(l1, l2):
    return True in (
        line_contains_point(l1, l2[0]),
        line_contains_point(l1, l2[1]),
        line_contains_point(l2, l1[0]),
        line_contains_point(l2, l1[1]),
    )


def line_contains_point(line, p):
    return line[0] <= p and line[1] >= p
