.global _main
.section .text

_main:

push	%ebp
mov	%esp,%ebp

sub $0x8, %esp

mov $filename, %ebx

mov $0x0, %ecx
mov $0x0, %edx

mov $11, %eax

int $0x80

leave
ret

filename:
	.string "/bin/sh"