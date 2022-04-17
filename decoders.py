# Ceasar Cryptography decoder with option to adjust offset

def decoder(input, offset):
    alphabet= "abcdefghijklmnopqrstuvwxyz"
    decode = ""
    for letter in input:
        if letter in alphabet:
            new_letter = (alphabet.find(letter) + offset) % 26
            decode += alphabet[new_letter]
        else:
            decode += letter
    return decode