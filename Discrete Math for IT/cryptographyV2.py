import string
import re

correspondingLetter = list(string.ascii_uppercase)
key = {}
keySwapped = {}

for i in range(len(correspondingLetter)):
    key[f"{i+1:02d}"] = correspondingLetter[i]
    keySwapped[correspondingLetter[i]] = f"{i+1:02d}"


def encrypt(text):
    encryptedMessage = ""
    for letter in text:
        encryptedMessage += str(keySwapped[letter.upper()])
    return encryptedMessage


def decrypt(message):
    decryptedMessage = ""
    messageSplit = re.findall("..", message)
    for split in messageSplit:
        decryptedMessage += key[split]
    return decryptedMessage


print(decrypt("2018050519"))
