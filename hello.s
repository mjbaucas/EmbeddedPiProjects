.data

message:
	.ascii	"Hello, ARM64!\n"
len = . - message

.text

.global _start
_start:
	mov x0, #1
	ldr x1, =message
	ldr x2, =len
	mov w8, #64
	svc #0
	
	mov x0, #0
	mov w8, #93
	svc #0
