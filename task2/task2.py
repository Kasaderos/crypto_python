import random
import sys
import argparse
import json


def gen_key(keygen):
    key = random.sample(range(256), 256)
    text = json.dumps({i: key[i] for i in range(256)})
    write_file(keygen, text)


def write_file(name, text):
    with open(name, "w") as out:
        out.write(text)


def get_text(file):
    with open(file, "r") as f:
        return f.read()


def encrypt(filename, keygen):
    try:
        key = get_key(keygen)
        write_file("cipher", ''.join(
            [str(chr(key[ord(ch)])) for ch in get_text(filename)]))
    except:
        print("symbol size() > 1 byte")


def get_key(keygen):
    d = json.loads(get_text(keygen))
    return {int(k): d[k] for k in d}


def get_frequency(filename):
    text = get_text(filename)
    count = {ord(ch): text.count(ch) for ch in text}
    print(sortFreq(count))
    freq = {k: count[k]/len(text) for k in count.keys() if count[k] != 0}
    return freq


def sortFreq(p):
    return sorted(p.items(), key=lambda kv: kv[1])

def decrypt(cipher, keygen):
    keygen = get_key(keygen)
    keys = {keygen[k]: k for k in keygen}
    deciphered = ''.join([str(chr(keys[ord(ch)])) for ch in get_text(cipher)])
    write_file("deciphered.txt", deciphered)


def create_model(inputfile, cipher):
    p1 = get_frequency(inputfile)
    p2 = get_frequency(cipher)
    p1 = sortFreq(p1)
    p2 = sortFreq(p2)
    assert(len(p1) == len(p2))
    text = json.dumps(p1) + '\n' + json.dumps(p2)
    write_file('model', text)


def get_possible_keys(p1, p2):
    l1 = [l[0] for l in p1]
    l2 = [l[0] for l in p2]
    possible = {l1[i]: l2[i] for i in range(len(l1))}
    return possible


def break_key(model):
    p1, p2 = get_text(model).split('\n')
    p1 = json.loads(p1)
    p2 = json.loads(p2)
    keys = get_possible_keys(p1, p2)
    write_file("possible_key", json.dumps(keys))


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--generate', nargs=1)
    parser.add_argument('-e', '--encrypt', nargs=2)
    parser.add_argument('-d', '--decrypt', nargs=2)
    parser.add_argument('-m', '--model', nargs=2)
    parser.add_argument('-b', '--break', nargs=1)
    args = vars(parser.parse_args())

    if args['generate']:
        # python3 task2.py -g keygen
        # генерация и запись ключа в файл keygen
        gen_key(args['generate'][0])
    elif args['encrypt']:
        # python3 task2.py -e in.txt keygen
        # шифрование по ключу keygen
        encrypt(args['encrypt'][0], args['encrypt'][1])
    elif args['decrypt']:
        # python3 task2.py -d cipher keygen
        decrypt(args['decrypt'][0], args['decrypt'][1])

    elif args['model']:
        # python3 task2.py -m in.txt cipher
        # модель
        create_model(args['model'][0], args['model'][1])
    elif args['break']:
        # python3 task2.py -b model
        # взлом
        break_key(args['break'][0])
