from Crypto.Cipher import AES

with open("3.1.2.3_aes_weak_ciphertext.hex") as cipher:
	iv = ("00"*16).decode('hex')

	cipher_content = cipher.read().strip()
	cipher_content_binary = cipher_content.decode('hex')

	# Throws an error after 21, no idea why but it's right after solution
	for key_int in range(0, 31):
		if key_int < 0x10:
			key_str = ("00"*31) + '0' + str(hex(key_int)[2:])
			key = key_str.decode('hex')
		else:
			key_str = ("00"*31) + str(hex(key_int)[2:])
			key = key_str.decode('hex')

		print("Key = " + str(key_int) + ", Key Str = " + key_str + ":  " + AES.new(key, AES.MODE_CBC, iv).decrypt(cipher_content_binary))
