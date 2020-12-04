# Reusable functions
import fileinput


def nrs_from_file(f):
    # return map(int, open(f).readlines())
    return [int(x) for x in open(f).readlines()]


def lines_from_file(f):
    # return map(str.rstrip, open(f).readlines())
    return [x.rstrip() for x in open(f).readlines()]


def nrs_from_input():
    return [x.rstrip() for x in fileinput.input()]