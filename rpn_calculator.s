.global _start

.section .bss
buffer: .skip 256

.section .text
_start:
	mov x0, 0
	ldr x1, =buffer
	mov x2, 255
	mov x8, 63
	svc 0
	
	mov x1, x1
	mov x0, 1
	mov x8, 64
	svc 0
	
	mov x0, 0
	mov x8, 93
	svc 0
	
	
