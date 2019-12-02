import random
import sys


def gen_key():
    with open("keygen", "w") as f:
        key = random.sample(range(256), 256)
        f.write(str(key))
    return key

def write_file(name, text):
    with open(name, "w") as out:
        out.write(text)

def encrypt(filename, key):
    with open(filename, "r") as f:
        write_file("cipher", ''.join([str(chr(key[ord(ch)])) for ch in f.read()]))

def count_bytes(text):
    count = [0] * 256
    for c in text:
        count[ord(c)] += 1
    return count

def get_frequency(filename):
    with open(filename, "r") as f:
        text = f.read()
        count = count_bytes(text)
        #print(count)
        count = [i/len(text) for i in count]
        return count
'''
[1, 2, 2]
[1, 2, 2]

0:0 0:0
1:1 1:2
2:2 2:1

EPS = 1e-6

def find():
    inds = []
    for i in range(len(p1)):
        if abs(p1[i] - p2[i]) >= EPS:
            inds.append(i)
    
def get_possible_keys(p1, p2):
    ind = j
    for i in range(len(p1)):
        if p1[i] != p2[i]:
'''        

def decrypt(filename_text, filename_cipher):
    p1 = sorted(get_frequency(filename_cipher))
    p2 = sorted(get_frequency(filename_text))

    assert(len(p1)==len(p2))

    #keys = get_possible_keys(p1, p2)
    #write_file("possible_keys", keys)

if __name__ == "__main__":    
    if "-g" in sys.argv and len(sys.argv) == 3:
        encrypt(sys.argv[2], gen_key())
    if "-d" in sys.argv and len(sys.argv) == 4:
        decrypt(sys.argv[2], sys.argv[3])
    