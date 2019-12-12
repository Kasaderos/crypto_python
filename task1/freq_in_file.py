import sys

def f(file_names):
    freq = dict()
    for filename in file_names:
        with open(filename, 'r', encoding='utf-8') as f:
            symbols = f.read().replace(' ', '')
            symbols = symbols.replace('\n', '')
            freq = {ch : symbols.count(ch) for ch in symbols}
            return freq

if len(sys.argv) > 1:
    print(f(sys.argv[1:]))
else:
    print("files no found")

