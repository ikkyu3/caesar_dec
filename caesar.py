import argparse


def dec(p_sentence, l_key):
    p = p_sentence
    k = l_key
    res = ""

    for c in list(p):
        asc = ord(c)
        tmp = asc - 97
        tmp = (tmp + k) % 26
        asc = tmp + 97
        res += chr(asc)

    return res



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("p_sentence", help="plain sentence")
    parser.add_argument("l_key", type=int, help="key size, int")
    args = parser.parse_args()

    enc = dec(args.p_sentence, args.l_key)
    print(enc)
