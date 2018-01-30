.global your_asm_fn
.section .text

your_asm_fn:

push %ebp
mov  %esp,%ebp

push $0x00
push $0x646f6f66
push $0x6c6f6f63
mov  %esp,%ebx

push $0xc105ed
mov  %esp,%ecx

push %ebx
push %ecx
push $0xacce55ed
call practice
pop  %ebx
pop  %ebx
pop  %ebx

leave
ret

// "coolfood\0"
// c: 0x63
// o: 0x6f
// o: 0x6f
// l: 0x6c
// f: 0x66
// o: 0x6f
// o: 0x6f
// d: 0x64
// \: 0x00