from system import system
from heapq import nlargest


def get_biggest_files (n, path='.'):
    lines = system(f'du -a {path}').splitlines()
    pairs = [line.split('\t') for line in lines]
    return [name for size, name in nlargest(n, pairs)]

