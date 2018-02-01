.global your_asm_fn
.section .text

your_asm_fn:

push	%ebp
mov	%esp,%ebp

# push arg 1
push $00
push $0x646f6f66
push $0x6c6f6f63
mov %esp, %ebx

# push arg 2
push $0xc105ed
mov %esp, %ecx

push %ebx
push %ecx
push $0xacce55ed

call practice

leave
ret