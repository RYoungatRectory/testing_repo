def keystream_gen(plaintext, key):
	keysteam = ""
	j = 0
	for i in range(len(plaintext)):
		keystream += key[j]
		j += 1
		if j >= len(key):
			j = 0
	return keystream

plaintext = input("plaintext(all lowercase): ")
key = input("key(all lowercase): ")
if len(key) == 0:
	print("You didnt put in a key")
keyst = keystream_gen(plaintext, key)

alph = "abcedfghijklmnopqrstuvwxyz"

			
