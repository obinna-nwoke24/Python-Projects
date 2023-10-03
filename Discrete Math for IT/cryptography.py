import string

correspondingLetter = list(string.printable)
key = {}
keySwapped = {}

for i in range(len(correspondingLetter)):
    key[i] = correspondingLetter[i]
    keySwapped[correspondingLetter[i]] = i


def encrypt(text):
    encryptedMessage = ""
    for letter in text:
        encryptedMessage += str(keySwapped[letter])
    return encryptedMessage

