import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')

args = parser.parse_args()

filename = args.file
with open(filename) as opened_file:
    encoded_text = opened_file.read()  # read the file into a string


def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    # print('Decoded text: "' + text + '"')
    return text


n = -13
result = decode_Caesar_cipher(encoded_text, n)
print(result)
