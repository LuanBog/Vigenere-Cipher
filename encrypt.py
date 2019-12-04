from itertools import cycle
import sys
import pyperclip

alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

def clipboard(text):
	pyperclip.copy(text)
	pyperclip.paste()

def get_value(key):
    for i, v in alphabet.items():
        if v == key:
            return i

def get_proper_index(amount):
	index = 0

	while amount > 0:
		index += 1
		amount -= 1

		if index >= len(alphabet):
			index = 0

	return index

def encrypt(text, key):
    encrypted = ""
    
    sequence = []

    ks = [sq.lower() for sq in key]
    kss = cycle(ks)

    for letter in text:
        if letter.lower() in alphabet:
            if letter.isupper():
                encrypted = encrypted + get_value(get_proper_index(alphabet[letter.lower()] + alphabet[next(kss)])).upper()
            else:
                encrypted = encrypted + get_value(get_proper_index(alphabet[letter.lower()] + alphabet[next(kss)]))
        else:
            encrypted = encrypted + str(letter).lower()

    return encrypted

if __name__ == "__main__":
	if len(sys.argv) > 1:
		text = str(sys.argv[1])
		key = str(sys.argv[2])

		encryption = encrypt(text, key)

		print("\nEncrypted Vigenere Cipher: " + encryption)

		clipboard_choice = input("\nCopy to clipboard?:\n(y/n): ")

		if clipboard_choice.lower() == "y" or clipboard_choice.lower() == "yes":
			clipboard(encryption)

		sys.exit()

	print("Vigenere Cipher Encrypter\n")

	text = input("Enter Plaintext: ")
	key = input("Enter the key: ")

	encryption = encrypt(text, key)

	print("\nEncrypted Vigenere Cipher: " + encryption)

	clipboard_choice = input("\nCopy to clipboard?:\n(y/n): ")

	if clipboard_choice.lower() == "y" or clipboard_choice.lower() == "yes":
		clipboard(encryption)

	sys.exit()

