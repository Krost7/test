while(True):
	plaintext = input("input: ")
	key = abs(int (input("Key: ")))

	def checkCase(ch):
	
		if (ch.islower()):			#check upper case or lower case     
			return ((ord(ch) + key-97) % 26+97)  #mod the char ascii number lower case a + total words
		
		else:
			return ( (ord(ch) + key-65) % 26+65)	#mod the char ascii number upper case a + total words
	

	asciiValue = []

	for ch in plaintext :
 		asciiValue.append(checkCase(ch))
	print("Plaintext: ", plaintext)
	print("Ciphertext: ", ''.join(chr(i) for i in asciiValue))
