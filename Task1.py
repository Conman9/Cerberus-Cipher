# Connor Jurgensen 
# Vigenere Cipher Encoder
# Task 1

def main():
	plaintext = input()
	key = input()
	#plaintext = "hell-o wor ld!"
	#key = "SECURITY"
	ciphertext = ""
	key_values = []
	key = key.upper()
    #Converts the whole key into ascii variables. Key will always be uppercase so 
    # we can subtract 65 (A) from the ascii value
	for char in key:
		key_values.append(ord(char) - 65)

	counter = 0;

	#check letter by letter of the plaintext
	for char in plaintext:

		#if non-alphabetical letter, then preserve it
		if(char == " " or char < "A" or (char > "Z" and char < "a")):	
			ciphertext += char;
		
		#Converts uppercase letter to ascii, manipulates it with the cipher, then
		# appends it to the ciphertext
		elif(char >= "A" and char <= "Z"):
			ciphered_letter = chr( ((ord(char) - 65) + (key_values[counter % len(key_values)])) % 26 + 65)
			ciphertext += ciphered_letter
			counter+=1;
		
		#Converts lowercase letter to ascii, manipulates it with the cipher, then
		# appends it to the ciphertext
		elif(char >= 'a' and char <= 'z'):
			ciphered_letter = chr( ((ord(char) - 97) + (key_values[counter % len(key_values)])) % 26 + 97)
			ciphertext += ciphered_letter
			counter+=1;

	print(ciphertext)	

main()
