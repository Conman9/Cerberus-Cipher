# Connor Jurgensen 
# Vigenere Cipher Decoder
# Task 3

import re
from Task2 import decode


def main():
	ciphertext = input()
	key_length = int(input())

	key = findKey(ciphertext, key_length)
	#plaintext = decode(ciphertext, key)
	print(key)
	print(plaintext)


def findKey(ciphertext, key_length):
	frequency_array = [0.0820011,0.0106581,0.0344391,0.0363709,0.124167,
		0.0235145,0.0181188,0.0350386,0.0768052,0.0019984,0.00393019,
		0.0448308,0.0281775,0.0764055,0.0714095,0.0203171,0.0009325,
		0.0668132,0.0706768,0.0969225,0.028777,0.0124567,0.0135225,
		0.00219824,0.0189182,0.000599]
	
	shifted_text = ""
	split_cipher = []
	shifted_cipher = []
	smallest_chi = 999999
	key = [None] * key_length
	key_diff = [None] * key_length
	chi_calc = 0
	closest_string = ""
	chi_diff = 0.0
	smallest_chi_diff = 999999
	closest_string_diff = ""
	small_key_diff = ""

	new_cipher = re.sub("[^a-zA-Z]+", "", ciphertext).lower()

 	#splits cipher text into different parts based on key length
	for x in range(0, key_length):
		val = new_cipher[x::key_length]
		split_cipher.append(val)
	
	shifted_cipher = split_cipher.copy()

	for q in range(0, key_length):
		for x in range(0, 26):
			for char in split_cipher[q]:
				cipherletter = chr(((ord(char)-97 + x) % 26 + 97))
				shifted_text += cipherletter

			for z in range(0, 26):
				count = shifted_text.count(chr(z+97))
				expected_freq_calc = len(split_cipher[q]) * frequency_array[z] #length of text * expected frequency
				chi_calc += pow(count - expected_freq_calc, 2.0) / expected_freq_calc
				chi_diff += pow(count - expected_freq_calc, 2.0)

			if(chi_calc < smallest_chi):
				smallest_chi = chi_calc
				closest_string = shifted_text
				small_key = x

			if(chi_diff < smallest_chi_diff):
				smallest_chi_diff = chi_diff
				closest_string_diff = shifted_text
				small_key_diff = x
			
			shifted_text = ""
			chi_calc = 0
			chi_diff = 0

		key[q] = small_key

		key_diff[q] = small_key_diff

		split_cipher[q] = closest_string
		smallest_chi = 99999
		smallest_chi_diff = 99999
		str_key = ""

	##print(key)
	#print(key_diff)
	str_key_diff = ""
	for x in range(0, key_length):
		key_letter = chr((-key[x] % 26) + 97)
		str_key += key_letter
	
	for x in range(0, key_length):
		key_letter = chr((-key_diff[x] % 26) + 97)
		str_key_diff += key_letter

	key = str_key.upper()
	key_diff = str_key_diff.upper()

	#print(key)
	#print(str_key_diff)

	if(key == str_key_diff):
		return key

	plaintext = decode(ciphertext, key)
	plaintext_diff = decode(ciphertext, key_diff)
	#print(plaintext)
	#print(plaintext_diff)
	count = 0
	count_diff = 0
	ic_diff = 0
	ic = 0
	for z in range(0, 26):
		count = plaintext.count(chr(z+97))
		count_diff = plaintext_diff.count(chr(z+97))
		ic +=  (count * (count - 1)) / (len(plaintext) * (len(plaintext) - 1))
		ic_diff +=  (count_diff * (count_diff - 1)) / (len(plaintext_diff) * (len(plaintext_diff) - 1))

	#print(ic)
	#print(ic_diff)
	if(ic > ic_diff):
		return key
	elif(ic == 0.0):
		return key
	else:
		return key_diff




if __name__ == "__main__":
	main()