from pathlib import Path

path = Path(__file__).parent / 'data' / 'secret'

file = open(path / '1testsmallmessy.in', 'r')
n = int(file.readline())
lines = ' '.join([line.rstrip() for line in file.readlines()])
arr = [int(x) for x in lines.split()]
