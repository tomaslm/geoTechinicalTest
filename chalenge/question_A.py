def check_line_overlap(l1, l2):
     """
     Two lines (l1, l2) overlap if: 
     1) l1 starts before the end of l2 (l1 doesn't start after the end of l2)
     2) l1 ends after the start of l2 (l1 doesn't end before the start of l2)
     """
     return starts_before_end(l1,l2) and ends_after_start(l1,l2)


def starts_before_end(line1, line2):
     return get_start(line1) <= get_end(line2)

def ends_after_start(line1, line2):
     return get_end(line1) >= get_start(line2)

def get_start(line):
     return line[0]

def get_end(line):
     return line[1]