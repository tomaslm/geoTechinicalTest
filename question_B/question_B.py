import itertools
# from profile_decorator import profile_decorator
import cProfile, pstats, io


def compare_string_version(v1, v2, version_separator="."):
    if v1 == v2:
        return 0

    v1_list = v1.split(version_separator) if v1 is not None else ()
    v2_list = v2.split(version_separator) if v2 is not None else ()
    comparison_result = compare_string_version_list(v1_list, v2_list)
    return comparison_result


def compare_string_version_list(v1_list, v2_list):
    for i1, i2 in itertools.zip_longest(v1_list, v2_list):
        if i1 != i2:
            result = compare_string_version_string(i1, i2)
            if result != 0:
                return result
    return 0


def compare_string_version_string(s1, s2):
    if None in (s1, s2):
        if s1 is None and s2 is None:
            result = 0
        if s2 is None:
            result = 1
        elif s1 is None:
            result = -1
    else:
        if s1 == s2:
            result = 0
        elif s1 > s2:
            result = 1
        elif s1 < s2:
            result = -1
    return result


if __name__ == '__main__':    
    # compare_string_version("1.0.2.1.2.3.4.5.6.7.8.9", "1.0.2.1.2.3.4.5.6.7.8.8")
    
    pr = cProfile.Profile()
    pr.enable()


    for i in range(100000):
        compare_string_version("1.0.2.1.2.3.4.5.6.7.8.9", "1.0.2.1.2.3.4.5.6.7.8.8")
    # print(timeit.timeit('compare_string_version("1.0.2.1.2.3.4.5.6.7.8.9", "1.0.2.1.2.3.4.5.6.7.8.8")',
                        # number=1_000_000, globals=globals()))

                        
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
