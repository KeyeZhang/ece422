import sys, random

# Command: python sol_3.1.3.2.py 3.1.3.2_input_string.txt sol_3.1.3.2.hex

def wha(inStr):
	mask = 0x3FFFFFFF
	outHash = 0

	for byte in inStr:
		byte = ord(byte)
		intermediate_value = ((byte ^ 0xCC) << 24) | ((byte ^ 0x33) << 16) | ((byte ^ 0xAA) << 8) | (byte ^ 0x55)
		outHash = (outHash & mask) + (intermediate_value & mask)

	return outHash

if len(sys.argv) < 3:
    print("Missing arguments: python your_script.py file.txt output_file")

with open(sys.argv[1]) as f, open(sys.argv[2], 'w') as out:
	out.write(hex(wha(bytes(f.read()))))
	
