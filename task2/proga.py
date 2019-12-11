import random
import sys


EPS = 1e-6

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
        try:
            write_file("cipher", ''.join([str(chr(key[ord(ch)])) for ch in f.read()]))
        except:
            print("symbol size() > 1 byte")


def count_bytes(text):
    count = {i : 0 for i in range(256)}
    for c in text:
        count[ord(c)] += 1
    return count


def get_frequency(filename):
    with open(filename, "r") as f:
        text = f.read()
        count = count_bytes(text)
        count = {k : count[k]/len(text) for k in count.keys() if count[k] != 0}
        return count, text


def get_possible_keys(p1, p2):
    l1 = list(p1.keys())
    l2 = list(p2.keys())
    # сопоставляем
    possible = {l1[i] : [l2[i],] for i in range(len(l1))} 
    return possible


def sortFreq(p):
    return {k: v for k, v in sorted(p.items(), key=lambda item: item[1])}


def decipher_by_first_key(cipher, keys):    
    deciphered = ""
    for ch in cipher:
        deciphered += str(chr(keys[ord(ch)][0]))
    print(deciphered)


def decrypt(text, cipher):
    p1, cipher = get_frequency(cipher)
    p2, text = get_frequency(text)
    p1 = sortFreq(p1)
    p2 = sortFreq(p2)
    assert(len(p1)==len(p2))
    keys = get_possible_keys(p1, p2)
    write_file("possible_keys", str(keys))
    decipher_by_first_key(cipher, keys)

if __name__ == "__main__":    
    if "-g" in sys.argv and len(sys.argv) == 3:
        # python3 proga.py -g in.txt 
        encrypt(sys.argv[2], gen_key())
    if "-d" in sys.argv and len(sys.argv) == 4:
        # python3 proga.py -d in.txt cipher
        decrypt(sys.argv[2], sys.argv[3])
    