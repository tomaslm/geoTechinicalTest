import timeit


def check_line_overlap(line1, line2):
    """
     Two lines (l1, l2) overlap if: 
     1) l1 starts before the end of l2 (l1 doesn't start after the end of l2)
     2) l1 ends after the start of l2 (l1 doesn't end before the start of l2)
     """
    return line1[0] <= line2[1] and line1[1] >= line2[0]


if __name__ == '__main__':
    res = check_line_overlap((280, 300), (-100, 8))
    print(res)
    print(timeit.timeit('check_line_overlap((280, 300), (-100, 8))',
                        number=10_000_000, globals=globals()))
