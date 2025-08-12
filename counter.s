.global counter_function
.extern interrupt_function

.section .rodata
message: .ascii	"Counter: "
newline: .ascii "\n"

.text
counter_function:
	mov x19, #0
	mov x20, #10
	
loop_start: 
	cmp x19, x20 
	bge	loop_end
	
	mov x0, x19
	bl interrupt_function
	
	mov x2, x19
	
	// Print "Counter: "
	mov x0, #1
	ldr x1, =message
	mov x2, #9
	mov w8, #64
	svc #0
	
	// Print number
	mov x2, x19
	bl print_int
	
	mov x0, #1
	ldr x1, =newline
	mov x2, #1
	mov w8, #64
	svc #0
	
	add x19, x19, #1
	b loop_start

loop_end:
	mov x0, #0
	mov w8, #93
	svc #0

print_int:
	sub sp, sp, #32
	mov x4, sp
	mov x3, x2
	mov x5, #10

	cmp x3, #0
	bne convert_loop
	
	mov x6, #'0'
	strb w6, [x4, #-1]!
	b convert_done
	
convert_loop:
	udiv x6, x3, x5
	msub x7, x6, x5, x3
	add x7, x7, #'0'
	strb w7, [x4, #-1]!
	mov x3, x6
	cbnz x3, convert_loop
	
convert_done:
	mov x0, #1
	mov x1, x4
	sub x2, sp, x4
	mov w8, #64
	svc #0
	
	add sp, sp, #32
	ret

