import itertools
# from profile_decorator import profile_decorator
import cProfile
import pstats
import io


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
    if s1 == s2:  # equal strings
        return 0
    elif s1 is None:  # s1 is none while s2 is not
        return -1
    elif s2 is None:  # s2 is none while s1 is not
        return 1
    # there is no None value
    elif s1 < s2:  # s2 is greather than s1
        return -1
    else:  # s1 is greather than s2
        return 1


if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()

    for i in range(1000000):
        compare_string_version("1.0.2.1.2.3.4.5.6.7.8.9",
                               "1.0.2.1.2.3.4.5.6.7.8.8")
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
