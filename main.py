#!/usr/bin/env python
# -*- coding: utf-8 -*-


tralphabet = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "i", "ı", "j", "k", "l",
              "m", "n", "o", "ö", "p", "q", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
enalphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
endecoders = ["Ceasar", "A1Z26", "Atbash", "Vigénere", "combined"]
trdecoders = ["Sezar", "A1Z26", "Atbeş", "Vicenere", "bileşik"]
trstrings = ["şifre:", "anahtar:", "YÖNTEMLER", "devam?", "evet", "hayır"]
enstrings = ["cipher:", "key:", "METHODS", "continue?", "yes", "no"]
# placeholder b4 i learn to do xml's
retry = True


tratbash = {"a": "z", "b": "y", "c": "v", "ç": "ü", "d": "u", "e": "t", "f": "ş", "g": "s", "ğ": "r", "h": "p",
            "ı": "ö", "i": "o", "j": "n", "k": "m", "l": "l", "m": "k", "n": "j", "o": "i", "ö": "ı", "p": "h",
            "r": "ğ", "s": "g", "ş": "f", "t": "e", "u": "d", "ü": "ç", "v": "c", "y": "b", "z": "a"}

enatbash = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r",
            "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i",
            "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}


def enc_ceaser_tr(sentence, num):
    newSentence = ""
    for character in sentence:
        i = -1
        for x in tralphabet:
            i += 1
            if x == character:
                break
        if character in tralphabet:
            if i + num < 29:
                newSentence += tralphabet[i + num]
            else:
                newSentence += tralphabet[(i + num) - 29]
        else:
            newSentence += character
    print("-" * 20)
    print("Cümleniz şuydu: \"", sentence, "\" \nŞifrelenmiş formu: \"", newSentence, "\"")
    print("-" * 20)

def enc_ceaser_en(sentence, num):
    newSentence = ""
    for character in sentence:
        i = -1
        for x in enalphabet:
            i += 1
            if x == character:
                break
        if character in enalphabet:
            if i + num < 26:
                newSentence += enalphabet[i + num]
            else:
                newSentence += enalphabet[(i + num) - 26]
        else:
            newSentence += character
    print("-" * 20)
    print("Your sentence was: \"", sentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

def enc_atbash_tr(userSentence):
    newSentence = ""
    for character in userSentence:
        if character in tratbash:
            newSentence += tratbash[character]
        else:
            newSentence += character
    print("-" * 20)
    print("Cümleniz şuydu: \"", userSentence, "\" \nŞifrelenmiş formu: \"", newSentence, "\"")
    print("-" * 20)

def enc_atbash_en(userSentence):
    newSentence = ""
    for character in userSentence:
        if character in tratbash:
            newSentence += tratbash[character]
        else:
            newSentence += character
    print("-" * 20)
    print("Your sentence was: \"", userSentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

def enc_a1z26_tr(sentence):
    newSentence = ""
    for character in sentence:
        i = -1
        if character in tralphabet:
            for x in tralphabet:
                i += 1
                if x == character:
                    break
            newSentence += "-"
            newSentence += str(i)
        else:
            newSentence += character
    print("-" * 20)
    print("Cümleniz şuydu: \"", sentence, "\" \nŞifrelenmiş formu: \"", newSentence, "\"")
    print("-" * 20)

def enc_a1z26_en(sentence):
    newSentence = ""
    for character in sentence:
        i = -1
        if character in enalphabet:
            for x in enalphabet:
                i += 1
                if x == character:
                    break
            newSentence += "-"
            newSentence += str(i)
        else:
            newSentence += character
    print("-" * 20)
    print("Your sentence was: \"", sentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

def enc_vigenere_en(keyword, sentence):
    keynumbers = []
    for character in keyword:
        i = -1
        for word in enalphabet:
            i += 1
            if character == word:
                break
        keynumbers.append(i)
    y = -1
    newSentence = ""
    for char in sentence:
        if char in enalphabet:
            i = -1
            y += 1
            for word in enalphabet:
                i += 1
                if char == word:
                    break
            i += int(keynumbers[(y % len(keynumbers))])
            if i < 26:
                newSentence += str(enalphabet[i])
            else:
                newSentence += str(enalphabet[(i - 26)])
        else:
            newSentence += char
    print("-" * 20)
    print("Your sentence was: \"", sentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)

def enc_vigenere_tr(keyword, sentence):
    keynumbers = []
    for character in keyword:
        i = -1
        for word in tralphabet:
            i += 1
            if character == word:
                break
        keynumbers.append(i)
    y = -1
    newSentence = ""
    for char in sentence:
        if char in tralphabet:
            i = -1
            y += 1
            for word in tralphabet:
                i += 1
                if char == word:
                    break
            i += int(keynumbers[(y % len(keynumbers))])
            if i < 29:
                newSentence += str(tralphabet[i])
            else:
                newSentence += str(tralphabet[(i - 29)])
        else:
            newSentence += char
    print("-" * 20)
    print("Your sentence was: \"", sentence, "\" \nEncrypted form:: \"", newSentence, "\"")
    print("-" * 20)


def bin2dec(num):
    i = len(str(num))
    num = 0
    for bas in str(num):
        i += -1
        num += int(bas) * (2 ** i)
    return num


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


def getcombined(tocombine, text):
    if isitin(tocombine, "a1"):
        text = geta1z26(text)
    if isitin(tocombine, "at"):
        text = getatbash(text)
    if isitin(tocombine, "vi"):
        print(getvigenere(text, input(strings[1])))
    elif isitin(tocombine, "ce"):
        ceasar(text)
    else:
        return text


def getatbash(text):
    results = []

    for letter in text:
        if isitin(alphabet, letter) is True:
            results.append(alphabet[(numinlistfirst(alphabet, letter)) * -1])
        else:
            results.append(letter)
    return ''.join(results)


def geta1z26(text):
    tire = 1
    nums = []
    letters = []
    for character in text:
        if len(nums) == 0:
            nums.append("")
        if character == "-":
            tire += 1
        elif character == " " or character == "," or character == "." or character == "?" or character == "!" or \
                        character == ":":
            nums.append(character)
            tire += 1
        elif character == "'" or character == '"':
            tire += 1
            nums.append(character)
        elif len(nums) < tire:
            if len(nums) > 0:
                if not nums[-1] == "":
                    nums.append(str(character))
        elif nums[tire - 1] == " ":
            nums.append(str(character))
            tire += 1
        else:
            nums[tire - 1] += str(character)
    for i in range(0, len(nums)):
        if not isint(nums[i]):
            letters.append(nums[i])
        else:
            letters.append(alphabet[int(nums[i]) - 1])
    return ''.join(letters)


def isint(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


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
    retry = True
    while retry:
        print("-" * 10 + "=" + strings[2] + "=" + "-" * 10, end='\n')
        printdecoders()
        print(end="\n")
        decoder = input()
        if int(decoder) == 1:
            ceasar(input(strings[0]))
        elif int(decoder) == 2:
            print(geta1z26(input(strings[0])))
        elif int(decoder) == 3:
            print(getatbash(input(strings[0])))
        elif int(decoder) == 4:
            print(getvigenere(input(strings[0]), input(strings[1])), end="\n")
        elif int(decoder) == 5:
            methodraw = input(strings[2].lower() + ":")
            i = 0
            methods = []
            for _ in methodraw:
                if i % 2 == 1:
                    methods.append(methodraw[i - 1] + methodraw[i])
                i += 1
            print(getcombined(methods, input(strings[0])))
        print(strings[3], end="\n")
        reply = input()
        if reply.lower == strings[5].lower():
            retry = False
        elif reply.lower() == strings[4].lower():
            retry = True
        else:
            retry = False


def getbinary(text, parsenum):
    lastword = []
    for t in range(0, len(text) / parsenum):
        word = ""
        for n in range(1, parsenum):
            word += text[n + parsenum * t]
        lastword.append(word)


lang = input("language/dil:")
print(end="\n")
if lang == "tr":
    alphabet = tralphabet
    decoders = trdecoders
    strings = trstrings
elif lang == "en":
    alphabet = enalphabet
    decoders = endecoders
    strings = enstrings
runprog()
