import sys
from Crypto.Cipher import AES

# Command: python sol_3.1.2.2.py 3.1.2.2_aes_ciphertext.hex 3.1.2.2_aes_key.hex 3.1.2.2_aes_iv.hex sol_3.1.2.2.txt

if len(sys.argv) < 5:
    print("Missing arguments: python your_script.py ciphertext_file key_file iv_file output_file")

with open(sys.argv[1]) as cipher, open(sys.argv[2]) as key, open(sys.argv[3]) as iv, open(sys.argv[4], 'w') as out:
	cipher_content = cipher.read().strip()
	key_content = key.read().strip()
	iv_content = iv.read().strip()

	cipher_content_binary = cipher_content.decode('hex')
	key_content_binary = key_content.decode('hex')
	iv_content_binary = iv_content.decode('hex')

	out.write(AES.new(key_content_binary, AES.MODE_CBC, iv_content_binary).decrypt(cipher_content_binary))
