''' https://www.codingame.com/ide/puzzle/encryptiondecryption-of-enigma-machine '''
abc = [chr(i) for i in range(65, 91)]
operation = input()
key = int(input())
rotors = [input() for _ in range(3)]
message = input()

def encryption():
    text_out = ''
    factor = 0
    for c in message:
        if c in abc:
            c = abc[(abc.index(c) + key + factor) % len(abc)]
            for rotor in rotors:
                c = rotor[abc.index(c)]
        text_out += c
        factor += 1
    return text_out

def decryption():
    text_out = ''
    factor = 0
    for c in message:
        if c in abc:
            for rotor in reversed(rotors):
                c = abc[rotor.index(c)]
            c = abc[(abc.index(c) - key - factor) % len(abc)]
        text_out += c
        factor += 1
    return text_out

if operation == 'ENCODE':
    print(encryption())
else:
    print(decryption())