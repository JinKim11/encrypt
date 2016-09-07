import string


alphabet = string.ascii_letters
punctuation = string.punctuation
encrypt = {" ":53}
decrypt = {53: " "}

i = 1
for letter in alphabet:
	encrypt[letter] = i
	decrypt[i] = letter
	i = i + 1 
z = 54
for punc in punctuation:
	encrypt[punc] = z
	decrypt[z] = punc
	z = z + 1

def encrypt_message():
	message = "Talia rules" #raw_input("What message would you like to encrypt?")
	for i in range(len(message)):
		print encrypt[message[i]]

def decrypt_message():
	message = "46 1 12 9 1 53 18 21 12 5 19"  #int(raw_input("Decrypt a message."))\

	for i in message.split(" "):
		print decrypt[int(i)]

	# for i in range(len(message)):
	# 	if encrypt[key] == message[i]:
	# 		print key


encrypt_message()
decrypt_message()
