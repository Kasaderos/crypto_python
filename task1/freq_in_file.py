import sys

def f(file_names):
    freq = dict()
    for filename in file_names:
        with open(filename, 'r', encoding='utf-8') as f:
            for char in ''.join((''.join(f)).split()):
                 freq[char] = (freq[char] + 1) if char in freq else 1

    return freq
print(f(sys.argv))


