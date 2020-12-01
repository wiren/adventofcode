# Reusable functions

def read_nrs_from_file(f):
    file = open(f, 'r')
    return list(map(lambda x: int(x), file.readlines()))
