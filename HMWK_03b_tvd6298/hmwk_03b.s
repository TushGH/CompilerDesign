.global main
.text
main:

# Prologue
pushq   %rbp
movq    %rsp, %rbp

.data
STRLIT0: .asciz "simpleWrite" 
.text
movq $STRLIT0, %rdi
call  writeString
call  writeNewLine

.data
.align 4
INTLIT0: .int 1 
.text
movq $INTLIT0, %edi
call  writeInteger
call  writeNewLine

.data
.align 8
REALIT0: .double 2.3 
.text
movq $REALIT0, %xmm0
call  writeReal
call  writeNewLine


.data
STRLIT1: .asciz "Integer : " 
.text
movq $STRLIT1, %rdi
call  writeString
call  writeNewLine

.data
.align 4
INTLIT1: .int 4 
.text
movq $INTLIT1, %edi
call  writeInteger
call  writeNewLine


.data
STRLIT2: .asciz "Real    : " 
.text
movq $STRLIT2, %rdi
call  writeString
call  writeNewLine

.data
.align 8
REALIT1: .double 5.6 
.text
movq $REALIT1, %xmm0
call  writeReal
call  writeNewLine


# exit value
movl    $0, %eax

# Epilogue
leave
ret
