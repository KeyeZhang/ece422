import sys

# Command: python sol_3.1.2.1.py 3.1.2.1_sub_ciphertext.txt 3.1.2.1_sub_key.txt sol_3.1.2.1.txt

if len(sys.argv) < 4:
    print("Missing arguments: python your_script.py ciphertext_file key_file output_file")

with open(sys.argv[1]) as ciper, open(sys.argv[2]) as key, open(sys.argv[3], 'w') as out:
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	cipher_content = ciper.read()
	key_content = key.read()

	for char in cipher_content:
		alpha_idx = key_content.find(char)
		if alpha_idx >= 0:
			out.write(alphabet[alpha_idx])
		else:
			out.write(' ')
