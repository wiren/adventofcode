# Reusable functions
import fileinput

def nrs_from_file(f):
    file = open(f, 'r')
    return map(int, file.readlines())

def lines_from_file(f):
    file = open(f, 'r')
    return map(str.rstrip, file.readlines())

def nrs_from_input():
    return map(str.rstrip, fileinput.input())