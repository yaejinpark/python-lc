def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    position = {char: i for i, char in enumerate(alphabet)}
    newString = ''

    for char in s:
        if char.lower() in alphabet:
            newStringIndex = (position[char.lower()] + k) % 26
            if char.islower():
                newString += alphabet[newStringIndex]
            else:
                newString += alphabet[newStringIndex].upper()
        else:
            newString += char

    return newString