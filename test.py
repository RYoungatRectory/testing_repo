def keystream_gen(plaintext, key):
	keystream = ""
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
def viginere(plaintext, keyst):
	encrypt = ""
	for i in range(len(plaintext)):
		charIndex = alph.index(plaintext[i])
		keyIndex = alph.index(keyst[i])
		x = charIndex + keyIndex
		if x > len(alph)-1:
			x -= len(alph)
		encrypt += alph[x]
	return encrypt
print(viginere(plaintext, keyst))
			
