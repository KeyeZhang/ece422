import sys
from Crypto.Hash import SHA256

# Command: python sol_3.1.3.1.py 3.1.3.1_input_string.txt 3.1.3.1_perturbed_string.txt sol_3.1.3.1.hex

if len(sys.argv) < 4:
    print("Missing arguments: python your_script.py file_1.txt file_2.txt output_file")

with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2, open(sys.argv[3], 'w') as out:
	f1_content = f1.read()
	f2_content = f2.read()

	f1_bin = bin(int(SHA256.new(f1_content).hexdigest(), 16))[2:]
	f2_bin = bin(int(SHA256.new(f2_content).hexdigest(), 16))[2:]

	# zero extend the strings if one is shorter
	f1_bin = f1_bin.zfill(max(len(f1_bin), len(f2_bin)))
	f2_bin = f2_bin.zfill(max(len(f1_bin), len(f2_bin)))

	hamming_dist = 0

	for idx in range(0, len(f1_bin)):
		if f1_bin[idx] != f2_bin[idx]:
			hamming_dist += 1

	out.write(str(hex(hamming_dist)[2:]))

	# print(f1_bin)
	# print(f2_bin)
	# print(str(hamming_dist) + ' ' + str(hex(hamming_dist)[2:]))
