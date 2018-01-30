.global _main
.section .text

_main:

push %ebp
mov  %esp,%ebp

mov  $0xb,%eax //execve

// /* /bin/sh\0 */
// / 2f
// b 62
// i 69
// n 6e
// / 2f
// s 73
// h 68
// \ 00

push $0x0068732f
push $0x6e69622f

mov  %esp,%ebx

mov  $0x0,%ecx
mov  $0x0,%edx
int  $0x80

leave
ret