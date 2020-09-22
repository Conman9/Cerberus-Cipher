# Connor Jurgensen 
# Vigenere Cipher Decoder
# Task 2

def main():
	ciphertext = input()
	key = input()
	#ciphertext = "zinf-f ehp dh!"
	#plaintext = "I KNOW IT WHEN I SEE IT"
	#key = "SECURITY"
	plaintext = decode(ciphertext, key)
	print(plaintext)

def decode(ciphertext, key):
	plaintext = ""
	key_values = []
	key = key.upper()
    
    #Converts the whole key into ascii variables. Key will always be uppercase so 
    # we can subtract 65 (A) from the ascii value
	for char in key:
		key_values.append(ord(char) - 65)

	counter = 0;

	#check letter by letter of the plaintext
	for char in ciphertext:

		#if non-alphabetical letter, then preserve it
		if(char == " " or char < "A" or (char > "Z" and char < "a")):	
			plaintext += char;
		
		#Converts uppercase letter to ascii, manipulates it with the cipher, then
		# appends it to the plaintext
		elif(char >= "A" and char <= "Z"):
			unciphered_letter = chr( ((ord(char) - 65) - (key_values[counter % len(key_values)])) % 26 + 65)
			plaintext += unciphered_letter
			counter+=1;
		
		#Converts lowercase letter to ascii, manipulates it with the cipher, then
		# appends it to the plaintext
		elif(char >= 'a' and char <= 'z'):
			unciphered_letter = chr( ((ord(char) - 97) - (key_values[counter % len(key_values)])) % 26 + 97)
			plaintext += unciphered_letter
			counter+=1;

	return plaintext

if __name__ == "__main__":
	main()