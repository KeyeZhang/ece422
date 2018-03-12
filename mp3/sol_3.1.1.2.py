# Decimal
with open("3.1.1.2_value.hex") as f:
	file_content = f.read().strip()
	integer_parsed = int(file_content,16)
	print(str(integer_parsed))

# Binary
with open("3.1.1.2_value.hex") as f:
	file_content = f.read().strip()
	integer_parsed = int(file_content,16)
	binary_parsed = bin(integer_parsed)[2:]
	print(str(binary_parsed))
