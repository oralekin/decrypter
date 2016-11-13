#!/usr/bin/env python
# -*- coding: utf-8 -*-


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
decoders = ["Ceasar", "A1Z26", "Atbash", "Vigénere", "Ceasar combine"]
soncevap = "abcdefgh"
retry = True


def getvigenere(text, keyword):
    key = []
    result = []
    i = -1
    text = text.lower()
    for keyletter in keyword:
        key.append(numinlistfirst(alphabet, keyletter))
    for cipherletter in text:
        if cipherletter == " ":
            cipherletter = cipherletter
        else:
            i += 1
        keynum = key[i % len(key)]
        decipherletter = getceasar(cipherletter, 25 - keynum)
        result.append(decipherletter)
    return ''.join(result)


def isitin(tosearchin, element):
    if None != numinlistfirst(tosearchin, element):
        return True
    else:
        return False


def combine(tocombine, text):
    if tocombine == "v":
        print(getvigenere(getatbash(geta1z26(text)), input("ciphered word:")))
    elif tocombine == "c":
        ceasar(getatbash(geta1z26(text)))


def getatbash(text):
    results = []

    for letter in text:
        if letter == " ":
            results.append(" ")
        else:
            results.append(alphabet[(numinlistfirst(alphabet, letter)) * -1])
    return ''.join(results)


def geta1z26(text):
    tire = 1
    nums = []
    letters = []
    for character in text:
        if character == "-":
            tire += 1
        elif character == " " or character == "," or character == "." or character == "?" or character == "!":
            nums.append(" ")
            tire += 1
        elif len(nums) < tire:
            nums.append(str(character))
        else:
            nums[tire - 1] += str(character)
    for i in range(0, len(nums)):
        if nums[i] == " ":
            letters.append(" ")
        else:
            letters.append(alphabet[int(nums[i])-1])
    return ''.join(letters)


def numinlistfirst(listtosearch, tosearch):
    nelement = 0
    for element in listtosearch:
        nelement += 1
        if element == tosearch:
            return nelement


def getceasar(harf, displacement):
        if harf == " ":
            return harf
        elif numinlistfirst(alphabet, harf) is None:
            return harf
        else:
            return alphabet[(numinlistfirst(alphabet, harf) + int(displacement)) % len(alphabet)]


def printdecoders():
    n = 0
    for dec in decoders:
        n += 1
        print("[" + str(n) + "]   " + dec)


def ceasar(text):
    text = text.lower()
    for displacement in range(0, len(alphabet)):
        print(displacement + 1, end="")
        if displacement < 9:
            print(" ", end="")
        print(": ", end="")
        for chara in text:
            print(getceasar(chara, displacement), end="")
        if len(text) < 33:
            if displacement % 3 == 2:
                print(end="\n")
            else:
                print("  |  ", end="")
        else:
            print(end="\n")
    for _ in [1, 2]:
        print(end="\n")


def runprog():
    print("-"*10 + "=" + "Decipher methods" + "=" + "-"*10, end='\n')
    printdecoders()
    decoder = input()
    retry = True
    while retry:
        if decoder.lower() == "ceasar" or decoder.lower() == "sezar" or \
                        int(decoder) == numinlistfirst(decoders, "Ceasar"):
            ceasar(input("cipher:"))
        elif decoder.lower() == "numbers" or decoder.lower() == "a1z26" or \
                        int(decoder) == numinlistfirst(decoders, "A1Z26"):
            print(geta1z26(input("cipher")))
        elif decoder.lower() == "vigenere" or decoder.lower() == "vigenére" or int(decoder) == 3:
            print(getatbash(input("cipher:")))
        elif int(decoder) == 4:
            print(getvigenere(input("cipher:"), input("key:")), end="\n")
        elif int(decoder) == numinlistfirst(decoders, "Ceasar "):
            combine("c", input("cipher:"))
        print("continue?:", end="\n")
        reply = input()
        if reply.lower == "no":
            retry = False
        elif reply.lower() == "yes":
            retry = True
            print("\n")
        else:
            retry = False


runprog()
