import random
import sys

# для сравнения чисел
EPS = 1e-6

def gen_key():
    with open("keygen", "w") as f:
        key = random.sample(range(256), 256)
        f.write(' '.join([str(k) for k in key]))


def write_file(name, text):
    with open(name, "w") as out:
        out.write(text)

def encrypt(filename, key):
    with open(filename, "r") as f:
        try:
            write_file("cipher", ''.join([str(chr(key[ord(ch)])) for ch in f.read()]))
        except:
            print("symbol size() > 1 byte")

def get_key_from_file():
    with open("keygen", "r") as f:
        return [int(k) for k in f.read().split()]


def get_frequency(filename):
    with open(filename, "r") as f:
        text = f.read()
        count = {ord(ch) : text.count(ch) for ch in text}
        freq = {k : count[k]/len(text) for k in count.keys() if count[k] != 0}
        return freq, text


def get_possible_keys(p1, p2):
    l1 = list(p1.keys())
    l2 = list(p2.keys())
    possible = {l1[i] : l2[i] for i in range(len(l1))} 
    return possible


def sortFreq(p):
    return {k: v for k, v in sorted(p.items(), key=lambda item: item[1])}


def write_decipher(cipher, keys):    
    deciphered = ""
    for ch in cipher:
        deciphered += str(chr(keys[ord(ch)]))
    write_file("deciphered.txt", deciphered)


def decrypt(text, cipher):
    p1, cipher = get_frequency(cipher)
    p2, text = get_frequency(text)
    p1 = sortFreq(p1)
    p2 = sortFreq(p2)
    assert(len(p1)==len(p2))
    keys = get_possible_keys(p1, p2)
    write_file("possible_key", str(keys))
    write_decipher(cipher, keys)

if __name__ == "__main__":    
    if "-g" in sys.argv and len(sys.argv) == 2:
        # python3 task2.py -g 
        # генерация и запись ключа в файл keygen
        gen_key()
    if "-e" in sys.argv and len(sys.argv) == 3:
        # python3 task2.py -e in.txt
        # шифрование по ключу keygen
        encrypt(sys.argv[2], get_key_from_file())
    if "-d" in sys.argv and len(sys.argv) == 4:
        # python3 task2.py -d in.txt cipher
        # взлом и запись расшифрованного текста
        decrypt(sys.argv[2], sys.argv[3])
    