#!/usr/bin/env python
# -*- coding: utf-8 -*-


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
decoders = ["Ceasar", "A1Z26", "Atbash", "Vigénere", "Ceasar + Atbash"]
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
    if numinlistfirst(tosearchin, element) is not None:
        return True
    else:
        return False


def combine(tocombine, text):
    if isitin(tocombine, "a1"):
        text = geta1z26(text)
    if isitin(tocombine, "at"):
        text = getatbash(text)
    if isitin(tocombine, "v"):
        print(getvigenere(text, input("anahtarı giriniz:")))
    elif isitin(tocombine, "c"):
        ceasar(text)
    else:
        return text


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
            letters.append(alphabet[int(nums[i]) - 1])
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
    print("-" * 10 + "=" + "YÖNTEMLER" + "=" + "-" * 10, end='\n')
    printdecoders()
    decoder = input()
    retry = True
    while retry:
        if decoder.lower() == "ceasar" or decoder.lower() == "sezar" or \
                        int(decoder) == numinlistfirst(decoders, "Ceasar"):
            ceasar(input("Şifrenizi giriniz:"))
        elif decoder.lower() == "numbers" or decoder.lower() == "a1z26" or \
                        int(decoder) == numinlistfirst(decoders, "A1Z26"):
            print(geta1z26(input("Şifrenizi giriniz:")))
        elif decoder.lower() == "vigenere" or decoder.lower() == "vigenére" or int(decoder) == 3:
            print(getatbash(input("Şifrenizi giriniz:")))
        elif int(decoder) == 4:
            print(getvigenere(input("Şifrenizi giriniz:"), input("Çözücü kelimeyi giriniz:")), end="\n")
        elif int(decoder) == numinlistfirst(decoders, "Ceasar + Atbash"):
            result = combine(["c", "at"], input("şifrenizi giriniz"))
            if result is not None:
                print(result)
        print("Devam (evet/hayır):", end="\n")
        reply = input()
        if reply.lower == "quit":
            retry = False
        elif reply.lower() == "evet":
            retry = True
            print("\n")
        else:
            retry = False


runprog()
